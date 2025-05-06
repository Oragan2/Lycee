import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

with open("intent_data.txt","r") as file:
    messages = []
    intents = []
    for ligne in file:
        ms = ligne.split("\t")
        messages.append(ms[0].split(":")[1])
        intents.append(ms[1].split("\n")[0])

# Convert intents to numerical labels
unique_intents = sorted(list(set(intents)))
intent_to_index = {intent: index for index, intent in enumerate(unique_intents)}
index_to_intent = {index: intent for intent, index in intent_to_index.items()}
numerical_intents = np.array([intent_to_index[intent] for intent in intents])

# Tokenize the text data
tokenizer = Tokenizer(num_words=100)  # Consider adjusting num_words based on your vocabulary size
tokenizer.fit_on_texts(messages)
sequences = tokenizer.texts_to_sequences(messages)

# Pad sequences to ensure uniform length
max_len = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=max_len, padding='post')

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, numerical_intents, test_size=0.2, random_state=42)

# Convert numerical labels to one-hot encoding for categorical cross-entropy loss
from tensorflow.keras.utils import to_categorical
y_train_one_hot = to_categorical(y_train, num_classes=len(unique_intents))
y_test_one_hot = to_categorical(y_test, num_classes=len(unique_intents))

print("Padded Sequences (Training Data Example):")
print(X_train[0])
print("\nOne-Hot Encoded Intent (Training Data Example):")
print(y_train_one_hot[0])

embedding_dim = 16  # Dimensionality of the word embeddings
lstm_units = 32     # Number of LSTM units

model = Sequential([
    Embedding(input_dim=len(tokenizer.word_index) + 1,  # Vocabulary size + 1 for unknown words
              output_dim=embedding_dim,
              input_length=max_len),
    LSTM(units=lstm_units),
    Dense(units=len(unique_intents), activation='softmax')  # Output layer with softmax for multi-class classification
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

epochs = 20
batch_size = 14

history = model.fit(X_train, y_train_one_hot, epochs=epochs, batch_size=batch_size, validation_split=0.1)

loss, accuracy = model.evaluate(X_test, y_test_one_hot)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")

# Make predictions on new data
new_messages = ["A joke please", "Sup How are you"]
new_sequences = tokenizer.texts_to_sequences(new_messages)
new_padded_sequences = pad_sequences(new_sequences, maxlen=max_len, padding='post')
predictions = model.predict(new_padded_sequences)
predicted_indices = np.argmax(predictions, axis=1)
predicted_intents = [index_to_intent[index] for index in predicted_indices]
print(f"\nPredictions for new messages: {predicted_intents}")
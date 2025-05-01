from sklearn.datasets import load_digits

digits = load_digits()
X_digits, y_digits = digits.data, digits.target
print("Digits X shape:", X_digits.shape)
print("Digits y shape:", y_digits.shape)

from sklearn.model_selection import train_test_split
import NN
X_digits_train, X_digits_test, y_digits_train, y_digits_test = train_test_split(X_digits, y_digits, test_size=0.2, random_state=42)

print("\nDigit Training:", X_digits_train.shape, y_digits_train.shape)
print("Digit Testing:", X_digits_test.shape, y_digits_test.shape)

n = NN.Neurol_Network([64,64,64,10])
n.train(X_digits_train, y_digits_train, 0.1, 1000, 100)

output = n.forward(X_digits_test)
print("Returned prediction : ")
print(output)
print("Expected Values")
print(y_digits_test)
print(f"Final accuracy : {n.calculate_accuracy(output,y_digits_test)}")
n.save("8*8_digits")

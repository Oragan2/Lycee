import numpy as np
np.random.seed(0)

class Layer_Dense:
    def __init__(self,n_inputs:int,n_neurons:int):
        self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.dot(inputs, self.weights) + self.biases
    def backward(self, dvalues):
        # Gradients on parameters
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        # Gradient on values
        self.dinputs = np.dot(dvalues, self.weights.T)

class Activation_ReLU:
    def forward(self,inputs):
        self.inputs = inputs
        self.output = np.maximum(0,inputs)
    def backward(self, dvalues):
        self.dinputs = dvalues.copy()
        self.dinputs[self.inputs <= 0] = 0

class Activation_Softmax:
    def forward(self,inputs):
        self.inputs = inputs
        exp_values = np.exp(inputs - np.max(inputs,axis=1, keepdims=True))
        self.output = exp_values / np.sum(exp_values, axis=1, keepdims=True)
    def backward(self, dvalues):
        self.dinputs = np.empty_like(dvalues)
        for index, (single_output, single_dvalues) in enumerate(zip(self.output, dvalues)):
            single_output = single_output.reshape(-1, 1)
            jacobian_matrix = np.diagflat(single_output) - np.dot(single_output, single_output.T)
            self.dinputs[index] = np.dot(jacobian_matrix, single_dvalues)

class Loss_CategoricalCrossentropy:
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)
        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)
        negative_log_likelihoods = -np.log(correct_confidences)
        return np.mean(negative_log_likelihoods)
    def backward(self, dvalues, y_true):
        samples = len(dvalues)
        labels = np.array(y_true)
        if len(y_true.shape) == 1:
            y_true = np.zeros((samples, dvalues.shape[1]))
            y_true[range(samples), labels] = 1
        self.dinputs = -y_true / dvalues
        self.dinputs = self.dinputs / samples
        return self.dinputs

class Optimizer_SGD:
    def __init__(self, learning_rate=1.0):
        self.learning_rate = learning_rate
    def update_params(self, layer):
        layer.weights += -self.learning_rate * layer.dweights
        layer.biases += -self.learning_rate * layer.dbiases

class Neurol_Network:
    def __init__(self, neurons):
        self.layers = []
        for i in range(len(neurons) - 1):
            self.layers.append(Layer_Dense(neurons[i], neurons[i+1]))
            if i < len(neurons) - 2:
                self.layers.append(Activation_ReLU())
        self.layers.append(Activation_Softmax())
        self.loss_function = Loss_CategoricalCrossentropy()
        self.optimizer = None

    def forward(self, data):
        self.output = data
        for layer in self.layers:
            layer.forward(self.output)
            self.output = layer.output
        return self.output

    def backward(self, output, y_true):
        # Calculate loss gradient
        dvalues = self.loss_function.backward(output, y_true)

        # Backpropagate through layers in reverse order
        for layer in reversed(self.layers):
            layer.backward(dvalues)
            dvalues = layer.dinputs

    def train(self, X, y, learning_rate=0.01, epochs=100, print_every=10):
        self.optimizer = Optimizer_SGD(learning_rate=learning_rate)
        for epoch in range(epochs):
            # Forward pass
            output = self.forward(X)

            # Calculate loss
            loss = self.loss_function.forward(output, y)

            # Backward pass
            self.backward(output, y)

            # Update parameters
            if self.optimizer:
                for layer in self.layers:
                    if hasattr(layer, 'weights'):
                        self.optimizer.update_params(layer)

            if epoch % print_every == 0:
                accuracy = self.calculate_accuracy(output, y)
                print(f'epoch: {epoch}, loss: {loss:.4f}, acc: {accuracy:.4f}')

    def calculate_accuracy(self, y_pred, y_true):
        predictions = np.argmax(y_pred, axis=1)
        if len(y_true.shape) == 2:
            y_true = np.argmax(y_true, axis=1)
        accuracy = np.mean(predictions == y_true)
        return accuracy
    
    def save(self,name="neural_network"):
        with open(name+".nn", "w") as file:
            for j in range(0,len(self.layers),2):
                for i in range(len(self.layers[j].weights)):
                    file.write(str(weights_to_list(self.layers[j].weights[i])) + "\n")
                file.write(f"biases = {biases_to_list(self.layers[j].biases)}\n")
                file.write("New Layer\n")
    
    def load(self,name="neural_network"):
        file = open(name+".nn", "r", encoding="utf-8")
        n = 0
        l = 0
        for ligne in file:
            if ligne == "New Layer\n":
                l += 2
                n = 0
            elif ligne[:6] == "biases":
                self.layers[l].biases[0] = str_to_array(ligne[9:len(ligne)-1])
            else:
                self.layers[l].weights[n] = str_to_array(ligne[:len(ligne)-1])
                n += 1

def biases_to_list(b):
    res = []
    for val in b[0]:
        res.append(float(val))
    return res

def weights_to_list(w):
    res = []
    for val in w:
        res.append(float(val))
    return res

def str_to_array(s):
    res = []
    for val in s:
        if val == "[":
            n = 0
            l = 0
            lo = False
            neg = False
        elif val in ",]":
            if neg:
                n *= -1
            res.append(n)
            n = 0
            l = 0
            lo = False
        elif val == ".":
            lo = True
        elif val == "-":
            neg = True
        elif val != " ":
            n += int(val)*10**l
        if lo:
            l-=1
    return np.array(res)
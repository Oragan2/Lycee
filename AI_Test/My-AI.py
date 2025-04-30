import numpy as np
np.random.seed(0)

def create_data(points,classes):
    X = np.zeros((points*classes,2))
    y = np.zeros(points*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0,1,points)
        t = np.linspace(class_number*4,(class_number+1)*4, points) + np.random.randn(points)*0.2
        X[ix] = np.c_[r*np.sin(t*2.5),r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y

X,y = create_data(100,3)

class Layer_Dense:
    def __init__(self,n_inputs:int,n_neurons:int):
        self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
    def forward(self,inputs):
        self.output = np.maximum(0,inputs)

class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs,axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

class Loss:
    def calculate(self,output,y):
        samples_losses = self.forward(output,y)
        data_loss = np.mean(samples_losses)
        return data_loss

class Loss_CategoricalCrossentropy(Loss):
    def forward(self,y_pred,y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)
        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), y_true]
        else:
            correct_confidences = np.sum(y_pred_clipped*y_true, axis=1)
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods
        
class Neurol_Network:
    def __init__(self,neurons):
        self.layers = [Layer_Dense(neurons[max(0,i-1)],neurons[i]) for i in range(len(neurons))]
    
    def forward(self,data):
        res = data
        activate = Activation_ReLU()
        finish = Activation_Softmax()
        loss = Loss_CategoricalCrossentropy()
        for layer in self.layers:
            layer.forward(res)
            res = layer.output
            if not self.layers.index(layer) == len(self.layers)-1:
                activate.forward(res)
                res = activate.output
            else:
                finish.forward(res)
                res = finish.output
        self.res = res
        return res
    
    def loss(self,y):
        loss = Loss_CategoricalCrossentropy()
        return loss.calculate(self.res,y)

X,y = create_data(100,3)

n = Neurol_Network([2,9,9,3])
print(n.forward(X))
print(n.loss(y))

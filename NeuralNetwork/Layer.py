import numpy as np

class Layer():
    def __init__(self, inputs, neurons):
        self.weights = np.clip(np.random.randn(inputs,neurons), -1,1)
        self.biases = np.clip(np.random.randn(1,neurons),-1 ,1)

    def Calculate(self,input):
        self.output= np.dot(input, self.weights)+ self.biases
    
    def ReLu(self):
        self.output = np.clip(self.output, 0, None)
    
    def Update(self,input):
        self.Calculate(input)
        self.ReLu()

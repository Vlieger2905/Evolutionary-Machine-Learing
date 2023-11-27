import numpy as np
from .Layer import *

# Input needed for the Circly:
# x.self location
# y.self location
# x.center safezone location
# y.center safezone location
# safezone radius
# Brain must have 5 inputs
# Brain must have 5 outputs
# Brain should return the highest output as a movement.

class Brain:
    def __init__(self, neuronsLayer, Genes=None):
        self.layers = []
        self.layerdata = []
        if Genes:
            self.ChildConstruction(neuronsLayer,Genes)
        else:
            # Creating the hidden layers:
            for i in range(0,len(neuronsLayer)-1):
                self.layers.append(Layer(neuronsLayer[i],neuronsLayer[i+1]))
            self.SavingSperm()

    
    # Constructing the brain according to a given gene input
    def ChildConstruction(self,neuronsLayer,genes):
        index = 0
        for layer in genes:
            new_layer = Layer(neuronsLayer[index], neuronsLayer[index+1])
            for gene in layer:
                weights = np.array(gene["weights"])
                biases = np.array(gene["biases"])
                new_layer.weights = weights
                new_layer.biases = biases
            self.layers.append(new_layer)
            index+=1
        self.SavingSperm()


    # Function to calculate the results after going through each layer and neuron
    def Thinking(self,inputData):
        currentInput = inputData
        # Going through each layer and calculating the output of that layer to ue as input for the next layer
        for layer in self.layers:
            layer.Update(currentInput)
            currentInput = layer.output
        # Returning the final output of the entire brain
        return currentInput
    
    def SavingSperm(self):
        for layer in self.layers:
                genes =[{
                    "weights":layer.weights.copy(),
                    "biases": layer.biases.copy()
                }]
                self.layerdata.append(genes)

from numpy import *
import random
from .Settings import *


def GeneSelector(Geneslist):
    index = random.randint(0,len(Geneslist)-1)
    selectedGene = Geneslist[index]
    return selectedGene,index

def Mutation(Gene):
    for layer in Gene:
        for keys in layer:
            # Mutation for weights
            rows, cols = keys["weights"].shape
            for i in range(rows):
                for j in range(cols):
                    if random.uniform(0, 1) <= MutationRate:
                        keys["weights"][i, j] += random.uniform(min(MutationSize), max(MutationSize))

            # Mutation for biases
            for elements in keys["biases"]:
                for i in range(len(elements)):
                    if random.uniform(0, 1) <= MutationRate:
                        elements[i] += random.uniform(min(MutationSize), max(MutationSize))

    return Gene




# def Mutation(Gene):
#     for layer in Gene["layerData"]:
#         for keys in layer:
#             # Looping through each element in the gene in the weights
#             rows, cols=keys["weights"].shape
#             for i in range(rows):
#                 for j in range(cols):
#                     if random.uniform(0,1) <= MutationRate:
#                         keys["weights"][i,j] += random.uniform(min(MutationSize),max(MutationSize))

#             # Looping through each element in the gene in the biases
#             for elements in keys["biases"]:
#                 for i in range(len(elements)):
#                     if random.uniform(0,1) <= MutationRate:
#                         elements[i] += random.uniform(min(MutationSize),max(MutationSize))
#     return Gene
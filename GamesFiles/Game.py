import pygame, sys, time, math,random, datetime,json
from collections import Counter
from .Settings import *
from .Entity import *
from .SafeZone import *
from .GeneManipulation import *
from .Encoder import *
from .Functions import *


class Game:
    def __init__(self, File=None):
#Setting up the game class 
        pygame.init()
        self.screen = pygame.display.set_mode((XDisplay, YDisplay))
        pygame.display.set_caption('Python final program')
        self.population = []
        self.survivors = []
        self.genePool = []
        self.colourPool = []
        self.HighestPerforming = []
        self.safezone = SafeZone()
        
        
        self.font = pygame.font.Font(None, 36)
        if File:
            self.Load(File)
            self.population = [Circly(gene) for gene in self.genePool]
        else:
            self.generation = 0
            self.HighestSurvival = 0  
            self.mostCommon = []  
            for i in range(AmountCreatures) :
                self.population.append(Circly(self.safezone))
                
# Function that updates all of the 
    def UpdateCreatures(self):
        for Circly in self.population:  
            Circly.Update(self.screen)
            self.FittnessCheck(Circly)

# Adding fittness to the circly
    def FittnessCheck(self,circly):
        distance = Distance(self.safezone.x,self.safezone.y, circly.x,circly.y)
# The fitness increases if the circly moves towards the circle
        if distance < circly.lastDistance:
            circly.fitness +=1
#The fitness decrease if the circly moves away from the safezone  
        if distance > circly.lastDistance:
            circly.fitness -=1

        circly.lastDistance = distance

# Eliminating all the Circlys that are outside of the safezon
    def EthnicCleansing(self):
        self.survivors = []
        self.genePool = []
        self.colourPool = []
        self.HighestPerforming = sorted(self.population, key=lambda Circly: Circly.fitness, reverse=True)[:25]
        print(self.HighestPerforming)
#Checking whether the Circly are in the safezon and if they survive 
        for Circly in self.population:
            distance = Distance(Circly.x, Circly.y, self.safezone.x, self.safezone.y)
            if distance <= SafeZoneRadius:
                self.survivors.append(Circly)
                self.colourPool.append(Circly.colour)
                self.genePool.append(Circly.brain.layerdata)
# Update the population with the survivors
        if len(self.survivors)> self.HighestSurvival:
            self.HighestSurvival = len(self.survivors)

            
# Repopulating with the survivors #WORK IN PROGRESS
    def NeukenInDeKeuken(self):
        newPopulation = []
        
        if len(self.genePool) == 0:
            for i in range(AmountCreatures):
                newPopulation.append(Circly())
        else:
# Creating children with the exact same dna as their parents
            for i in range(int(Clones * AmountCreatures)):
                Gene, index = GeneSelector(self.genePool)
                newPopulation.append(Circly(self.safezone,Gene,self.colourPool[index]))
            
    # Creating Children that have mutated
            for i in range(int(Mutated * AmountCreatures)):
                Gene, index = GeneSelector(self.genePool)
                MutatedGene = Mutation(Gene)
                newPopulation.append(Circly(self.safezone,MutatedGene,self.colourPool[index],True))
                
    # Creating Children with completely random gene
            for i in range(int(Random * AmountCreatures)):
                newPopulation.append(Circly(self.safezone))
        
        self.population = newPopulation
# Drawing the Generation
    def Drawtext(self, position, info):
        text_surface = self.font.render(str(info), True, (255,0,0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = position
        self.screen.blit(text_surface, text_rect)
# Updating the screen
    def update(self):
        self.screen.fill('white')
        self.safezone.Draw(self.screen)
        self.UpdateCreatures()
        self.Drawtext((10,10),self.generation)
        self.Drawtext((10,40),self.HighestSurvival)
        pygame.display.update()

# Loading the current genepool to a file to save the current state.
    def Save(self):
        self.genePool = []
        for creatures in self.population:
            self.genePool.append(creatures.brain.layerdata)
# Making a library to store the data in for export.
        data = {
            'generation': self.generation,
            'HighestSurvival': self.HighestSurvival,
            'Best survivors each few generation': self.mostCommon,
            'Genes': self.genePool
        }
# Creating string of the current time and date.
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# Creating filename
        fileName = f"SaveFiles/Savedata_{timestamp}.json"
        with open(fileName, 'w') as file:
            json.dump(data, file, indent=4, cls=NumpyArrayEncoder)

# Loading a save file to the simulation
    def Load(self, filename):
# Opening the selected file
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
# Reading the data from the file
        self.generation = data['generation']
        self.HighestSurvival = data['HighestSurvival']
        self.mostCommon = data['Best survivors each few generation']
        self.genePool = []
        for gene_data_list in data['Genes']:
            gene_list = []
            for gene_data in gene_data_list:
                brain_layers = []
                for layer_data in gene_data:
                    weights = np.array(layer_data['weights'])
                    biases = np.array(layer_data['biases'])
                    brain_layers.append({'weights': weights, 'biases': biases})
                gene_list.append(brain_layers)
            self.genePool.append(gene_list)

        

# Running the actual simulation
    def Run(self):
        counter = 0
        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.Save()
                        pygame.quit()
                        sys.exit()
                # This is one simulation of a generation
                for i in range(MaxStep):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.Save()
                            pygame.quit()
                            sys.exit()
                    self.update()
                # After a certain amount of time all the Circlies that are outside of the safezone will die 
                self.safezone = SafeZone()
                self.EthnicCleansing()
                # The surviving population will reproduce
                self.NeukenInDeKeuken()
                self.generation +=1
                counter +=1
                if counter % 5 == 0:
                    bestSurvivor = Counter(self.colourPool).most_common(1)[0][0]
                    bestSurvivorList = list(bestSurvivor)
                    self.mostCommon.append(bestSurvivorList)
                    
                if counter == 500:
                    counter = 0
                    self.Save()
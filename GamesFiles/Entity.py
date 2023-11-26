import pygame, random
import numpy as np
from .Settings import *
from NeuralNetwork.Brain import Brain
from .Functions import Distance



class Circly:
    def __init__(self, safezone, Gene=None,Colour = None, Mutations = False):
        self.x = random.randint(0,XDisplay)
        self.y = random.randint(0,YDisplay)
        # self.x = 0.5*XDisplay
        # self.y = 0.5*YDisplay
        self.colour = self.ColourPicker(Colour,Mutations)
        self.size = 5
        self.decision = ''
        self.fitness = 0
        self.lastDistance = Distance(safezone.x, safezone.y, self.x,self.y)
        self.input = [self.x, self.y,Xsafecenter, Ysafecenter, SafeZoneRadius]
        self.inputSize = len(self.input)
        self.outputSize = len(possibilities)
        self.neuronLayer =[self.inputSize,16,16,16,self.outputSize]
        self.brain = Brain(self.neuronLayer, Gene)

    
    def decisionMaking(self):
        # This optimization is only possible if the safezone is not moving
        # Small optimization to make it that Entities where there state is not chancing are not calulated
        if self.decision == "idle":
            pass
        elif self.decision == "right" and self.x >= XDisplay:
            pass
        elif self.decision == "left" and self.x <= 0:
            pass
        elif self.decision == "down" and self.y >= YDisplay:
            pass
        elif self.decision == "up" and self.y <= 0:
            pass
        # If the Creature would move then let is think
        else:
            self.input = [self.x, self.y,Xsafecenter, Ysafecenter, SafeZoneRadius]
            output =self.brain.Thinking(self.input)
            decisionIndex = np.argmax(output)
            self.decision = possibilities[decisionIndex]
        

    def Move(self):
        if self.decision == 'idle':
            pass
        elif self.decision == 'up':
            self.y -=1
            self.y=np.clip(self.y, 0, YDisplay)
        elif self.decision == 'down':
            self.y += 1
            self.y=np.clip(self.y, 0, YDisplay)
        elif self.decision == 'left':
            self.x -= 1
            self.x=np.clip(self.x, 0, XDisplay)
        elif self.decision == 'right':
            self.x += 1
            self.x=np.clip(self.x, 0, XDisplay)

    def Draw(self, display):
        pygame.draw.circle(display, self.colour, (self.x,self.y), self.size)
    
    def Update(self,display):
        self.decisionMaking()
        self.Move()
        self.Draw(display)
    
    def ColourPicker(self, GeneColour, Mutations):
        if GeneColour:
            colour = GeneColour
            if Mutations == True:
                colourList = list(colour)
                index = random.randint(0,2)
                colourList[index] = np.clip(colourList[index] + random.randint(-25,25),0,255)
                colour = tuple(colourList)
            return colour
        else:
            colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            return colour

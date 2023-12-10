import random, pygame, math
from .Settings import *


class SafeZone:
    def __init__(self, position, generation):
        if position == 'center':
            self.x = Xsafecenter
            self.y = Ysafecenter
        if position == 'yAxis': 
            self.x = Xsafecenter
            # Change self.y to be a sin wave between 0 and Ydisplay dependend on the generation. one period should equate to hundred generations
            self.y = random.randint(0, YDisplay)
            self.y = (YDisplay / 2) * math.sin(2 * math.pi * 0.01 * generation) + (YDisplay / 2)
        if position == 'random': 
            self.x = random.randint(0+ SafeZoneRadius, XDisplay-SafeZoneRadius)
            self.y = random.randint(0+ SafeZoneRadius, YDisplay-SafeZoneRadius)
        
        self.radius = SafeZoneRadius
        self.colour = (0,255,0)

    def Draw(self,display):
        pygame.draw.circle(display, self.colour, (self.x,self.y), self.radius, 10)
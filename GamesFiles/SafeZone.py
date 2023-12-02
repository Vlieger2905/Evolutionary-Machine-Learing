import random, pygame
from .Settings import *


class SafeZone:
    def __init__(self):
        self.x = random.randint(0+ SafeZoneRadius, XDisplay-SafeZoneRadius)
        self.y = random.randint(0+ SafeZoneRadius, YDisplay-SafeZoneRadius)
        # self.x = Xsafecenter
        # self.y = Ysafecenter
        self.radius = SafeZoneRadius
        self.colour = (0,255,0)

    def Draw(self,display):
        pygame.draw.circle(display, self.colour, (self.x,self.y), self.radius, 2)
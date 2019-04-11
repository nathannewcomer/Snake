#Apple class

import pygame
import random

red = (255, 0, 0)

class apple:

    #constructor
    def __init__(self, screenSize, pixelSize):
        self.pos = (random.randrange(0, screenSize[0], pixelSize), random.randrange(0, screenSize[1], pixelSize))
        self.screenSize = screenSize
        self.pixelSize = pixelSize

    #return position of apple to do collision checking
    def position(self):
        return self.pos

    #draw the apple on screen
    def draw(self, screen):
        rect = pygame.Rect(self.pos, (self.pixelSize, self.pixelSize))
        pygame.draw.rect(screen, red, rect)
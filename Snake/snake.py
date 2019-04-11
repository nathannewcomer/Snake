#Snake class

import pygame
import random

clock = pygame.time.Clock()
white = (255, 255, 255)
green = (0, 255, 0)

class player:

    #constructor
    def __init__(self, screenSize, pixelSize):
        self.screenSize = screenSize
        self.pixelSize = pixelSize
        self.body = [(screenSize[0] // 2, screenSize[1] // 2)]
        self.nextMove = (self.pixelSize, 0)
        
    def position(self):
        return self.body[len(self.body) - 1]

    #changes the direction of the snake when an arrow key is pressed
    def changeDirection(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.nextMove = (0, -self.pixelSize)
            elif event.key == pygame.K_DOWN:
                self.nextMove = (0, self.pixelSize)
            elif event.key == pygame.K_LEFT:
                self.nextMove = (-self.pixelSize, 0)
            elif event.key == pygame.K_RIGHT:
                self.nextMove = (self.pixelSize, 0)

    #moves the snake by updating the coordinate of each section
    def move(self, time):
        coordinate = self.body[len(self.body) - 1]
        x = coordinate[0]
        y = coordinate[1]

        #wraps section when it goes off screen
        if coordinate[0] > self.screenSize[0]:
            x = 0
        if coordinate[0] < 0:
            x = self.screenSize[0]
        if coordinate[1] > self.screenSize[1]:
            y = 0
        if coordinate[1] < 0:
            y = self.screenSize[1]

        coordinate = (x + self.nextMove[0], y + self.nextMove[1])
        self.body.append(coordinate)
        self.body.pop(0)
        clock.tick_busy_loop(time)

    #append snake when apple is eaten
    def eatApple(self):
        #coordinate = self.body[len(self.body) - 1]
        coordinate = self.body[0]
        
        coordinate = (coordinate[0] - self.nextMove[0], coordinate[1] - self.nextMove[1])

        self.body.insert(0, coordinate)

    #checks for collisions with itself    
    def checkCollision(self):
        for i in range(1, len(self.body)):
            if self.body[0] == self.body[i]:
                return True
        return False
    

    #draws each section of the snake on screen
    def draw(self, screen):
        for coordinate in self.body:
            rect = pygame.Rect(coordinate, (self.pixelSize, self.pixelSize))
            pygame.draw.rect(screen, green, rect)
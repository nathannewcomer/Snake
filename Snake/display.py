#Handles everything visual

import pygame

white = (255, 255, 255)
black = (0, 0, 0)

#Beginning title screen
def startScreen(screen, screenSize):
    #create fonts
    font1 = pygame.font.Font("upheavtt.ttf", screenSize[1] // 3)
    font2 = pygame.font.Font("upheavtt.ttf", screenSize[1] // 15)
    font3 = pygame.font.Font("upheavtt.ttf", screenSize[1] // 30)
    #put text into font objects
    text1 = font1.render("SNAKE", True, white)
    text2 = font2.render("Written by Nathan Newcomer", True, white)
    text3 = font3.render("Press any key start", True, white)
    #put text on the screen and position it
    screen.blit(text1, (screenSize[0] // 2 - text1.get_width() // 2, screenSize[1] // 4 - text1.get_height() // 2))
    screen.blit(text2, (screenSize[0] // 2 - text2.get_width() // 2, screenSize[1] // 2))
    screen.blit(text3, (screenSize[0] // 2 - text3.get_width() // 2, screenSize[1] // 2 + text3.get_height() * 5))

    #stay on screen until any button is pressed
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                done = True
        pygame.display.flip()


#draw the "UI" a.k.a. the score
def drawUI(screen, score, font, screenSize):
    text = font.render(str(score), True, white)
    #I'm a programmer not graphic designer
    screen.blit(text, (screenSize[0] - screenSize[0] // 10, screenSize[1] // 40))

#game over screen when the snake collides with itself
def gameOver(screen, screenSize):

    #reset the screen (a.k.a. fill it with black)
    screen.fill(black)

    #create fonts
    font1 = pygame.font.Font("upheavtt.ttf", screenSize[1] // 5)
    font2 = pygame.font.Font("upheavtt.ttf", screenSize[1] // 15)
    #create texts
    text1 = font1.render("Game Over", True, white)
    text2 = font2.render("Press any key to play again", True, white)
    #draw text on screen
    screen.blit(text1, (screenSize[0] // 2 - text1.get_width() // 2, screenSize[1] // 4 - text1.get_height() // 2))
    screen.blit(text2, (screenSize[0] // 2 - text2.get_width() // 2, screenSize[1] // 2))

    #stay on screen until button is pressed
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                done = True
        pygame.display.flip()
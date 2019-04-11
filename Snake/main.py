import pygame
from items import apple
from snake import player
import display

done = False
clock = pygame.time.Clock()

#colors used for drawing on screen
black  = (0, 0, 0)
white = (255, 255, 255)

#variables for game
screenSize = (640, 480)
pixelSize = 20
startTime = 10
score = 0

#initialize modules
pygame.init()
pygame.font.init()

#create screen
screen = pygame.display.set_mode(screenSize)

display.startScreen(screen, screenSize)
clock.tick_busy_loop(10)

#text for the score
font = pygame.font.Font("upheavtt.ttf", screenSize[1] // 10)
text = font.render(str(score), True, white)

#create snake and apple
app = apple(screenSize, pixelSize)
play = player(screenSize, pixelSize)

#main loop
while not done:

    #draws everything
    screen.fill(black)
    display.drawUI(screen, score, font, screenSize)
    app.draw(screen)
    play.draw(screen)

    #when snake eats apple
    if play.position() == app.position():
        score += 1
        app = apple(screenSize, pixelSize)
        play.eatApple()

    #checks for collision with itself
    if play.checkCollision():
        display.gameOver(screen, screenSize)

    #moves snake
    play.move(startTime)

    #checks events
    for event in pygame.event.get():

        #changes direction of snake when button is pressed
        play.changeDirection(event)

        if event.type == pygame.QUIT:
            done = True

    #updates screen
    pygame.display.flip()
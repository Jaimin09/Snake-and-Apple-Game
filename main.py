import pygame
import random
import time


pygame.init()
gameDisplay=pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
gameicon = pygame.image.load('gameicon.png')
pygame.display.set_icon(gameicon)
pygame.display.set_caption("Slither")

block_size = 20
display_width = 800
display_height = 600
white=(255,255,255)
black=(0,0,0)
red = (255,0,0)
greyBlue = (155,155,255)
green = (0,155,0)
img = pygame.image.load('snakehead.png')
appleimg = pygame.image.load('apple.png')
snakebody = pygame.image.load('snakebody.png')
slitherbackground2= pygame.image.load('slitherbackground2.png')
slitherimp= pygame.image.load('slitherimp.png')
title_edited = pygame.image.load('title_edited.png')

smallfont = pygame.font.SysFont("comicsansms", 25, bold=False, italic= True)
mediumfont = pygame.font.SysFont("comicsansms", 30, bold=False, italic= True)
largefont = pygame.font.SysFont("None", 100, bold=True, italic= False)

def pause():
    paused= True
    if paused == True:
        message_to_screen("PAUSED", red, -100, font_size="large")
        message_to_screen("Press C to continue or Q to quit", black, 25, font_size="small")
        pygame.display.update()
    while paused :
        #gameDisplay.fill(greyBlue)

        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def score(score):
    #score_txt= smallfont.render("Score : "+str(score), True, black)
    #gameDisplay.blit(score_txt, [0,0])
    message_to_screen("Score: "+ str(score), black, -250, font_size= "small")

def gameIntro():
    intro = True
    while intro:
        gameDisplay.fill(black)
        gameDisplay.blit(slitherimp, (130,50))
        gameDisplay.blit(title_edited, (280, 50))
        #message_to_screen("SLITHER", green, y_coordinate=-100, font_size="large")
        message_to_screen("The objective of the game is to eat apples", green, y_coordinate=-30, font_size="small")
        message_to_screen("The more you eat, the longer you become", green, y_coordinate=10, font_size="small")
        message_to_screen("If you hit yourself or the bounderies,you die!", green, y_coordinate=50, font_size="small")
        message_to_screen("Press C to play, P to pause or Q to quit", red, y_coordinate=180, font_size="small")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
        clock.tick(15)


def text_Object (msg, color, font_size):
    if font_size=="small":
        textSurf = smallfont.render(msg, True, color)
    if font_size=="medium":
        textSurf = mediumfont.render(msg, True, color)
    if font_size=="large":
        textSurf = largefont.render(msg, True, color)
    textRect= textSurf.get_rect()
    return textSurf, textRect

def message_to_screen(msg,color,y_coordinate, font_size):
    textSurf, textRect = text_Object(msg, color, font_size)
    textRect.center = display_width/2,display_height/2+y_coordinate
    gameDisplay.blit(textSurf,textRect)

   #text=font.render(msg, True, color)
   #gameDisplay.blit(text,[display_width/2,display_height/2])

def snake(block_size, snakeList):
    if direction=="right":
        head = pygame.transform.rotate(img, 270)
    if direction=="left":
        head = pygame.transform.rotate(img, 90)
    if direction=="up":
        head = img
    if direction=="down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakeList[-1][0],snakeList[-1][1] ))
    for XnY in snakeList[:-1]:
    #gameDisplay.blit(snakebody, [XnY[0],XnY[1]])
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def gameLoop():
    global direction
    direction = "right"
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = block_size
    lead_y_change = 0

    snakeList = []
    snakeLength  = 1
    randomAppleX = round(random.randrange(0, display_width-block_size)/20.0)*20.0
    randomAppleY = round(random.randrange(0, display_height-block_size)/20.0)*20.0


    gameExit = False
    gameOver = False
    while not gameExit:
        while gameOver ==  True:
            #time.sleep(1)
            gameDisplay.fill(black)
            message_to_screen("GAME OVER", red, y_coordinate=-75, font_size="large")
            message_to_screen("Press C to play again or Q to quit", green, y_coordinate=50, font_size='medium')
            message_to_screen("Your Score : " + str(snakeLength-1), green, -250, font_size= "small")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit=True
                        gameOver= False
                        pygame.display.update()
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit = True
            if event.type== pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = +block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change =0
                if event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = +block_size
                    lead_x_change = 0
                if event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver=True

        if lead_x == randomAppleX and lead_y == randomAppleY:
            randomAppleX = round(random.randrange(0, display_width - block_size) / 20.0) * 20.0
            randomAppleY = round(random.randrange(0, display_height - block_size) / 20.0) * 20.0
            snakeLength += 1



        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.blit(slitherbackground2, (0,0))

        snakeHead = [lead_x, lead_y]
        #snakeHead.append(lead_x)
        #snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        snake(block_size, snakeList)
        if len(snakeList) >= snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment==snakeHead:
                gameOver=True
        #pygame.draw.rect(gameDisplay, red,[randomAppleX,randomAppleY,block_size, block_size])
        gameDisplay.blit(appleimg, (randomAppleX,randomAppleY))

        score(snakeLength-1)
        pygame.display.update()
        clock.tick(15)


    pygame.quit()
    quit()
gameIntro()
gameLoop()

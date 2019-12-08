import pygame

#Init the pygame
pygame.init()
#Init Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
windowRunning = True

#Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg,(playerX,playerY))


#Tick Game-Loop
while windowRunning:
    screen.fill((0, 0, 0))  # Fill with black background first
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowRunning = False
    
    player()
    pygame.display.update()

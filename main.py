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
playerX = 370.0
playerY = 480.0
playerX_change = 0
def player(x,y):
    screen.blit(playerImg, (x, y))


#Tick Game-Loop
while windowRunning:
    screen.fill((0, 0, 0))  # Fill with black background first
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()

import pygame

#Init the pygame
pygame.init()
#Init Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
windowRunning = True



#Tick Game-Loop
while windowRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowRunning = False
    screen.fill((0,0,0)) #Fill with black background
    pygame.display.update()

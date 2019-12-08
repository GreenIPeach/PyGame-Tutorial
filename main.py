import pygame

#Init the pygame
pygame.init()
#Init Screen
screen = pygame.display.set_mode((800, 600))
windowRunning = True

#Tick Game-Loop
while windowRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowRunning = False
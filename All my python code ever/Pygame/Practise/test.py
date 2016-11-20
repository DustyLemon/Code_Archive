import pygame, sys
from pygame.locals import *

DISPLAY_SURFACE = pygame.display.set_mode((400,702),0,32)
DISPLAY_SURFACE.fill((255,255,255))
pygame.draw.polygon(DISPLAY_SURFACE, (100,84,82),((200,112),(206,532),(300,123)))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

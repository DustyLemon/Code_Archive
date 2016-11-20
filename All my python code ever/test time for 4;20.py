import time
import tkinter
import pygame, sys
from pygame.locals import *

while int(time.strftime('%H', time.gmtime())) < 16 or int(time.strftime('%M', time.gmtime())) < 20:
    pass

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('420 Blaze it!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

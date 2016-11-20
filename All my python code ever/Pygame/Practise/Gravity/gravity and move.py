import sys,pygame, time
from pygame.locals import *
x_coord = 200
y_coord = 100
width = 100
height = 90
speed = 10
FPS = 30
fpsClock = pygame.time.Clock()

pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode((400,500),0,32)
DISPLAY_SURFACE.fill((255,255,255))



while True:
    acceleration = (pygame.time.get_ticks()/1000)**1.0001      
    y_coord = y_coord + acceleration
    DISPLAY_SURFACE.fill((255,255,255))
    pygame.draw.rect(DISPLAY_SURFACE, (232,222,87),(x_coord,y_coord,width,height))
    for event in pygame.event.get():
        print(y_coord)
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x_coord = x_coord - speed
            elif event.key == K_RIGHT:
                x_coord = x_coord +speed
            elif event.key == K_UP:
                y_coord = y_coord - speed
            elif event.key == K_DOWN:
                y_coord = y_coord + speed
            elif event.key == K_SPACE:
                x_coord = 200
                y_coord = 100
                width = 100
                height = 90
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)

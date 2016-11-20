import sys,pygame, time
from pygame.locals import *
x_coord = 200
y_coord = 0
width = 100
height = 90
speed = 10
FPS = 30
fpsClock = pygame.time.Clock()
direction = 'down'
velocity = 1
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode((400,500),0,32)
DISPLAY_SURFACE.fill((255,255,255))

while True:
    print(y_coord)
    if y_coord < 200 and direction == 'down':
        acceleration = (pygame.time.get_ticks()/1000)**1.0001      
        y_coord = y_coord + acceleration
    else:
        y_coord = y_coord - acceleration
        direction = 'up'
        if y_coord < 20 * velocity:
            direction = 'down'
            velocity = velocity *2
        
    
    DISPLAY_SURFACE.fill((255,255,255))
    pygame.draw.rect(DISPLAY_SURFACE, (232,222,87),(x_coord,y_coord,width,height))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)

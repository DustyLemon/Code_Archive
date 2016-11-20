import sys,pygame, time
from pygame.locals import *
x_coord = 200
y_coord = 0
width = 100
height = 90
FPS = 100
fpsClock = pygame.time.Clock()
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode((400,500),0,32)
DISPLAY_SURFACE.fill((255,255,255))
dgravity = 0
ugravity = 0
ground = 200
nd_y_coord = 0
st_y_coord = 0
direction  = 'down'
while True:
    speed = nd_y_coord - st_y_coord
    if y_coord < ground and direction == 'down':
        dgravity = dgravity +0.01
        nd_y_coord = y_coord
        y_coord = y_coord + dgravity + speed
        st_y_coord = y_coord
        speed = nd_y_coord - st_y_coord      
        print(speed)
        ugravity = 0
        if speed < 0:
            direction = 'down'
    else:
        print(speed)
        direction = 'up'
        ugravity = ugravity +0.01
        y_coord = y_coord + ugravity + speed

    
    DISPLAY_SURFACE.fill((255,255,255))
    pygame.draw.rect(DISPLAY_SURFACE, (232,222,87),(x_coord,y_coord,width,height))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)

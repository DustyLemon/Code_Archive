import sys,pygame, time
from pygame.locals import *
x_coord = 200
y_coord = 400
width = 100
height = 90
FPS = 100
st_y_coord = 0
nd_y_coord = 0
gravity = 0
ground = 400
acceleration = 0.002
fpsClock = pygame.time.Clock()

pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode((400,500),0,32)
DISPLAY_SURFACE.fill((255,255,255))

while True:

    speed = nd_y_coord - st_y_coord
    print(speed)
    gravity = gravity + acceleration

    st_y_coord = y_coord

    y_coord = y_coord -1 + gravity
    if y_coord > ground:
        gravity = 0

    nd_y_coord = y_coord

    
    DISPLAY_SURFACE.fill((255,255,255))
    pygame.draw.rect(DISPLAY_SURFACE, (232,222,87),(x_coord,y_coord,width,height))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)

#distanced travelled = 200
    

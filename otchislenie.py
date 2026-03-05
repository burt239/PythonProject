import pygame
import random
window=pygame.display.set_mode((1280,823))
class person:
    x=0
    y=0
    img = ''

    def __init__(self,x_pers,y_pers,way):
        self.x = x_pers
        self.y = y_pers
        self.img = pygame.image.load(way)

    
bg=pygame.image.load('petya1.jpg')
pashalko=person(0,0,'239.png')
belka=person(50,50,'otch.png')

k = random.randint(0, 700)
speed = random.randint(10, 100)
while 1:
    window.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_LEFT:
                x=x-20

            if event.key == pygame.K_RIGHT:
                x=x+20

            if event.key == pygame.K_DOWN:
                y=y+20

            if event.key == pygame.K_UP:
                y=y-20




    if x<=0:
        x1=x+1280
        if x1<=1100:
            x=x+1280
    elif x>=1280-150:
        x1 = x - 1280
        if x1 >= 200:
            x = x1-1280
    else:
        x1=x


    if y<=0:
        y1=y+823
        if y1<=700:
            y=y+823
    elif y>=823-194:
        y1 = y - 823
        if y1 >= 200:
            y = y1-823
    else:
        y1=y

    print(x1,y1, "    ",x,y)

    window.blit(belka, (x, y))
    window.blit(belka, (x1, y1))


    if x2<1280-150:
       x2=x2+(speed//10)
    else:
        d=0-(speed//10)
        y2 = random.randint(0, 700)
        speed = random.randint(10, 100)

    window.blit(pashalko, (x2, y2))
    pygame.display.update()

    if pygame.mask.from_surface(pashalko).overlap(pygame.mask.from_surface(belka), ( x - p2.x, )):




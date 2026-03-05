import pygame
import random

from pygame.examples.go_over_there import screen

pygame.font.init()
window=pygame.display.set_mode((1280,823))
x = 50
y = 50
x2 = (1240-150)//2
y2 = (700-210)//2
xkol = x2
ykol = y2
count = 0
fx = True
fy = True
cont = False
bg=pygame.image.load('petya1.jpg')
pashalko=pygame.image.load('239.png')
belka=pygame.image.load('otch.png')
kol = pygame.image.load('kol tozhe ozenka.png')
bgifpas = pygame.image.load('фон если пасхалко.png')
bott = pygame.image.load('continue bottom.png')

k = random.randint(0, 700)
speed = 0.5
while 1:
    window.blit(bg,(0,0))
    window.blit(pygame.font.SysFont("Arial",100).render('очки: '+str(count),0,(0,0,0),None),(10,600))
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



    window.blit(belka, (x, y))
    window.blit(belka, (x1, y1))

    if fx:
        xkol=xkol+(speed)
        if xkol>=1240-32:
            fx=False
    else:
        xkol=xkol-(speed)
        if xkol<=0:
            fx=True

    if fy:
        ykol=ykol+(speed)
        if ykol>=700-76:
            fy=False
    else:
        ykol=ykol-(speed)
        if ykol<=0:
            fy=True





    window.blit(pashalko, (x2, y2))
    window.blit(kol, (xkol, ykol))


    if (pygame.mask.from_surface(pashalko).overlap(pygame.mask.from_surface(belka), ( x - x2, y-y2))) or (pygame.mask.from_surface(pashalko).overlap(pygame.mask.from_surface(belka), ( x1 - x2, y1-y2))):
        count += 1
        y2 = random.randint(0, 700 - 150)
        x2 = random.randint(0, 1240 - 210)

    if (pygame.mask.from_surface(kol).overlap(pygame.mask.from_surface(belka), (x - xkol, y - ykol))) or (pygame.mask.from_surface(kol).overlap(pygame.mask.from_surface(belka), ( x1 - xkol, y1-ykol))):
        count -= 239
        speed += 0.5
        ykol = random.randint(0, 700 - 76)
        xkol = random.randint(0, 1240 - 32)

    if count == 1:
        cont = True
        while cont:
            x = 50
            y = 50
            x2 = (1240 - 150) // 2
            y2 = (700 - 210) // 2
            xkol = x2
            ykol = y2
            count = 0
            fx = True
            fy = True
            window.blit(bgifpas,(0,0))
            window.blit(pygame.font.SysFont("Arial", 60).render('67', 0, (0, 0, 0), None), (150, 420))
            window.blit(bott, ((1280-360)//2, (823-270)//2))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        xb, yb = event.pos
                        if (xb<1280//2) and (xb>1280//2-360) and (yb > 823//2-270) and (yb < 823//2):
                            cont = False
            pygame.display.update()
        count -= 1
    count += 1

    pygame.display.update()



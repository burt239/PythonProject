import pygame
import random


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
oth = False
bg=pygame.image.load('petya1.jpg')
pashalko=pygame.image.load('239.png')
belka=pygame.image.load('otch.png')
kol = pygame.image.load('kol tozhe ozenka.png')
bgifpas = pygame.image.load('фон если пасхалко.png')
bgifoth = pygame.image.load('bg if oth.png')
bott = pygame.image.load('continue bottom.png')
bottagain = pygame.image.load('еще раз.png')
m = pygame.image.load('mouse.png')
smeme = pygame.image.load('closedmeme.png')
pic67 = pygame.image.load('size_m.jpg')
pic52 = pygame.image.load('52.jpg')
pic239 = pygame.image.load('239 meme.jpg')
meme52cond = False
meme67cond = False
meme239cond = False
abscount = 0
speed = 0.5

k = random.randint(0, 700)

while 1:
    window.blit(bg,(0,0))
    window.blit(pygame.font.SysFont("Arial",100).render('очки: '+str(count),0,(255,255,255),None),(10,600))
    if abs(count) > 239:
        abscount = 239
    else:
        abscount = abs(count)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_LEFT:
                x=x-20-abscount

            if event.key == pygame.K_RIGHT:
                x=x+20+abscount

            if event.key == pygame.K_DOWN:
                y=y+20+abscount

            if event.key == pygame.K_UP:
                y=y-20-abscount




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

    if count>=0:
        speed = 0.5 + count // 10

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

    if count == 52 and meme52cond == False:
        cont = True
        while cont:

            fx = True
            fy = True
            window.blit(bgifpas,(0,0))
            window.blit(pic52, (100, 400))
            window.blit(smeme, ((1280 - 100) // 2, 400))
            window.blit(smeme, (1080, 400))
            window.blit(bott, ((1280-360)//2, 500))
            pygame.display.update()
            for event in pygame.event.get():
                xb, yb = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    xb, yb = event.pos
                    window.blit(m,(xb,yb))

                    if pygame.mask.from_surface(m).overlap(pygame.mask.from_surface(bott), ((1280-360)//2 - xb, 500 - yb)):
                            cont = False

        meme52cond = True

    if count == 67 and meme67cond == False:
        cont = True
        while cont:

            fx = True
            fy = True
            window.blit(bgifpas,(0,0))
            window.blit(pic52, (100, 400))
            window.blit(pic67, ((1280 - 100) // 2, 400))
            window.blit(smeme, (1080, 400))
            window.blit(bott, ((1280-360)//2, 500))
            pygame.display.update()
            for event in pygame.event.get():
                xb, yb = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    xb, yb = event.pos
                    window.blit(m,(xb,yb))

                    if pygame.mask.from_surface(m).overlap(pygame.mask.from_surface(bott), ((1280-360)//2 - xb, 500 - yb)):
                            cont = False

        meme67cond = True


    if count == 239 and meme239cond == False:
        cont = True
        while cont:

            fx = True
            fy = True
            window.blit(bgifpas,(0,0))
            window.blit(pic52, (100, 400))
            window.blit(pic67, ((1280 - 100) // 2, 400))
            window.blit(pic239, (1080, 400))
            window.blit(bott, ((1280-360)//2, 500))
            pygame.display.update()
            for event in pygame.event.get():
                xb, yb = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    xb, yb = event.pos
                    window.blit(m,(xb,yb))

                    if pygame.mask.from_surface(m).overlap(pygame.mask.from_surface(bott), ((1280-360)//2 - xb, 500 - yb)):
                            cont = False

        meme239cond = True

    if count <= -2390:
        oth = True
        while oth:
            x = 50
            y = 50
            x2 = (1240 - 150) // 2
            y2 = (700 - 210) // 2
            xkol = x2
            ykol = y2
            count = 0
            fx = True
            fy = True
            window.blit(bgifoth,(0,0))
            window.blit(bottagain, ((1280-360)//2, 500))
            pygame.display.update()
            for event in pygame.event.get():
                xb, yb = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    xb, yb = event.pos
                    window.blit(m,(xb,yb))

                    if pygame.mask.from_surface(m).overlap(pygame.mask.from_surface(bottagain), ((1280-360)//2 - xb, 500 - yb)):
                            oth = False


    pygame.display.update()



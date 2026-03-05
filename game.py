import pygame
import random

f=True
x=True
window=pygame.display.set_mode((500,700))
dvdkartinka=pygame.image.load('otch.png')
fisica=pygame.image.load('fisicaa.png')
pashalco=pygame.image.load('239.png')
a=50
b=50
c=0
d=0
n = random.randint(0, 700)
k = random.randint(0, 700)
w = random.randint(10, 100)
bg=pygame.image.load('66e0357c171d4356220333.jpg')
while 1:
    window.blit(bg,(0,0))








    if f:
       a=a+0.5
       if a==350:
        f=False
    else:
        a=a-0.5
        if a==0:
            f=True

    if x:
       b=b+0.5
       if b==506:
        x=False
    else:
        b=b-0.5
        if b==0:
            x=True

    if c<500:
       c=c+0.5
    else:
        c=0-c
        n = random.randint(0, 700)
    if d<500:
       d=d+(w//10)
    else:
        d=0-(w//10)
        k = random.randint(0, 700)
        w = random.randint(10, 100)


    window.blit(fisica,(c,n))
    window.blit(pashalco, (d, k))
    window.blit(dvdkartinka, (a, b))
    pygame.display.update()
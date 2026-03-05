from operator import truediv

a=int(input())
b=a//100000
c=(a//10000)%10
d=a//1000%10
e=a//100%10
f=a//10%10
g=a%10
x=bool()
if b+c+d==e+f+g:
    x=True
else:
    x=False
print(x)

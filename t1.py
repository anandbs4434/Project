from turtle import *

def square(d):
    for i in range(4):
        fd(d)
        lt(90)



def polygon(side=3, dis=100):
    for i in range(side):
      fd(dis)
      lt(360/side)


square(100)
for i in range(1,50):
    polygon(i)



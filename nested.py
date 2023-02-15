from turtle import *
speed(0)

fillcolor('blue')
pencolor('black')
pensize(3)
side = 6
pu()
goto(-150, 200)
pd()
for i in range(side):
    fd(100)
    for i in range(side):
        fd(90)
        begin_fill()
        for i in range(side):
            fd(50)
            dot(10)
            for i in range(side):
                fd(25)
                lt(360/side)
            lt(360/side)
        end_fill()
        lt(360/side)
    rt(360/side)

hideturtle()
mainloop()


'''
it needs comments

I would use variables for the window's size,
such that, the robot could work on any window size.


Ilay down bricks  play row by row,
maybe with shift for each row.


The laying cycle would be done when the top is reached.

The advantage of having variables instead of hard coded numbers
is that the adjustment is done "automaticaly' ,
so, the number of layers, size of bricks, would be determined before
starting working.


Just a comment to check how gist works!
'''


import turtle

b = turtle.Screen()
a = turtle.Turtle()

b.setup(width=0.5, height=0.5, startx=None, starty=None)
# turtle.speed("fastest")
b.tracer(5, 0)
turtle.setheading(0)
turtle.pu()
turtle.setx(-960)
turtle.sety(-480)
turtle.pd()


def whereInX():
    global meeyo
    meeyo = turtle.xcor()
    return (meeyo)


def whereInY():
    global yuyo
    yuyo = turtle.ycor()
    return (yuyo)


def drawBrick():
    troodat = 1
    rowa = 1

    while troodat == 1:
        if rowa == 1:
            turtlesx = turtle.xcor()
            turtlesy = turtle.ycor()
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.update()
            if turtlesx >= 960:
                turtle.update()
                turtle.setx(-1010)
                turtle.sety(turtle.ycor() + 50)
            if turtlesy >= 0:
                break

    '''    for halfBrick in range(0,1):

        turtle.update()
        whereInX()
        whereInY()'''


def masterbuilder():
    drawBrick()


masterbuilder()

turtle.update()
b.mainloop()

'''
        if meeyo >= 980:
            if ww % 2 != 0:
                turtle.setx(-960)
                turtle.sety(yuyo+50)
            else:
                turtle.setx(-890)
                turtle.sety(yuyo+50)'''
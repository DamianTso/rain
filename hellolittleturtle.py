'''
Turtle

import turtle

You should start by defining the window(screen, stage)
window = turtle.Screen()



and , to keep the window open, finish with

window.mainloop()

'''

import tkinter as tk

import turtle



window =turtle.Screen()
window.screensize(1200,800,bg='green')


alex =turtle.Turtle()
alex.shape("turtle")
# alex.forward(50)
# alex.circle(50)
# alex.pencolor(0.5,0,0)
# alex.forward(50)
# alex.circle(50)
# alex.left(90)
# alex.forward(100)
# alex.pencolor(1,1,0)
# alex.left(90)
for i in range(6):
    alex.right(60)
    alex.circle(50)

window.mainloop()
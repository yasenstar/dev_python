# -*- coding: UTF-8 -*-
import turtle
# from turtle import *

wn = turtle.Screen()
tt = turtle.Turtle()

def draw(x,y):
    tt.clear()
    tt.reset()
    tt.hideturtle()
    turtle.pensize(4)
    turtle.pencolor('red')

    edges = int(input("please input how many edge you want to draw: "))
    angle = 360/edges
    for i in range (1,edges+1):
        turtle.forward(60*20/edges)
        turtle.left(angle)

draw(0,0)

wn.onclick(draw)
wn.onkey(wn.bye, "q")

wn.listen()
turtle.mainloop()
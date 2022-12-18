# -*- coding: UTF-8 -*-
import turtle
# from turtle import *

edges = int(input("please input how many edge you want to draw: "))
angle = 360/edges

turtle.pensize(4)
turtle.pencolor('red')
for i in range (1,edges+1):
    turtle.forward(60)
    turtle.left(angle)

input()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 16:50:49 2019
Name: Chinese Knot
@author: yasen
"""

import turtle as t
t.bgcolor('white')
t.hideturtle()

def draw(d,r):
    t.penup()
    t.goto(-d,0)
    t.seth(45)
    t.color('red')
    t.pensize(3)
    t.pendown()
    for i in range(5):
        t.fd(d)
        if i%2==0:
            t.circle(-r,180)
        else:
            t.circle(r,180)
    else:
        t.circle(-r,90)
    for i in range(5):
        t.fd(d)
        if i%2==0:
            t.circle(r,180)
        else:
            t.circle(-r,180)
    else:
        t.circle(r,90)
    
draw(100,10)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:36:29 2020

@author: yasen, thanks for Luo Hao @jackfrued/github
title: 绘制小猪佩奇

"""

# 导入海龟
from turtle import *

def head(x,y):
    pass

def nose(x,y):
    pass

def ears(x,y):
    pass

def eyes(x,y):
    pass

def cheek(x,y):
    pass

def mouth(x,y):
    color(239, 69, 19)
    penup()
    goto(x,y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)

# 设置海龟参数
def setting():
    # pensize(4)
    # 隐藏海龟
    hideturtle()
    colormode(255)
    color((255,155,192), "pink")
    setup(840,500)
    speed(15)

# 定义主函数
def main():
    """主函数"""
    setting()   # 海龟的基本设置
    head(-69.167)
    nose(-100,100)
    ears(0,160)
    eyes(0,140)
    cheek(80,10)
    mouth(-20,30)
    done()

# 确定主函数
if __name__ == '__main__':
    main()
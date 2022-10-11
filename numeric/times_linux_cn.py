# -*- coding: utf-8 -*-
import sys
import random
print("10以内（含10）的乘法练习")
k=1
count=0
correct=0
want_to_quit = 0
first_time_correct = 1
while want_to_quit != 1:

    if k == 1:
        a = int(round(random.random()*10,0))
        b = int(round(random.random()*10,0))

        print("请计算：", a, " x ", b, " = ?")
        if int(input()) == a * b:
            print("正确\n")
            k=1
            count = count + 1
            if first_time_correct == 1:
                correct=correct+1
            first_time_correct = 1
            if count % 5 == 0:
                print("继续?(y or n)")
                if input() == "n":
                    want_to_quit = 1
                    exit
        else:
            print("再想想")
            k=0
            first_time_correct = 0

    else:

        print("请计算：", a, " x ", b, " = ?")
        if int(input()) == a * b:
            print("正确")
            k=1
            count = count + 1
            if first_time_correct == 1:
                correct=correct+1
            first_time_correct = 1
            if count % 5 == 0:
                print("继续?(y or n)")
                if input() == "n":
                    want_to_quit = 1
                    exit                   
        else:
            print("再想想")
            k=0
            first_time_correct = 0
print("共做了",count, "题，正确答对了",correct,"题，正确率达到：",round(correct/count,3)*100,"%,祝贺")
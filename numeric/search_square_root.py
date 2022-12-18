# -*- coding: utf-8 -*-
"""
Spyder Editor
Using bisection search to approximate square root
Date: 2020-07-21
Author: Yasen Zhao
"""
print("="*50)
print("Using bisection search to approximate square root")
x = int(input("Please give one integer: "))
print("="*50)

print("...now searching...")

epsilon = 0.00000001
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2-x)>= epsilon:
    numGuesses += 1
    if ans**2<x:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
print("numGuesses = ", numGuesses)
print(ans, " is close to square root of ", x)
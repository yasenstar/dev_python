# Function: input three edges' length, check whether them can form one valid triangle
# Author: Xiaoqi Zhao (xiaoqizhao@outlook.com)
# Date: 2023-06-11

import math


def triangle_check(a, b, c):
    # print(a+b > c)
    if (a+b > c and a+c > b and b+c > a and abs(a-b) < c and abs(a-c) < b and abs(c-b) < a):
        return True
    else:
        return False


print("please input length of three edges:")
a = int(input("edge 1: "))
b = int(input("edge 2: "))
c = int(input("edge 3: "))
result = triangle_check(a, b, c)
# print(result)

if result:
    print("yes, this is one triangle")
else:
    print("sorry, they cannot form one triangle")

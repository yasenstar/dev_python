from math_xiaoqi import *
from vector_drawing import *
from random import *

z = (-2,1)
v = (1,1)
def random_r():
    return uniform(-3,5)
def random_s():
    return uniform(-2,1)

possibilities = [vector_add(vector_scale(random_r(),z),vector_scale(random_s(),v))
                    for i in range(0,100)]

draw(
    Points(*possibilities)
)
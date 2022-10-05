from vector_drawing import *
from math_xiaoqi import *

v1 = (6,3)
v2 = (3,4)
x = 5

print(vector_add(v1,v2))
print(vector_minus(v1,v2))
print(v1, x, vector_multiply(x,v1), v2, x, vector_multiply(x,v2))

print("length of v1 is", vector_length(v1))
print("length of v2 is", vector_length(v2))

draw(
    Points(v1, v2),
    Arrow(v1, color= red),
    Arrow(v2, color= red),
    Arrow(v1, v2, color= red)
)
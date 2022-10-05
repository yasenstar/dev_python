from math_xiaoqi import *
from vector_drawing import *

length_inside = 4
edges = 17

rp = regular_polygon(length_inside, edges)

print(rp)

draw(
    Polygon(*rp)
)
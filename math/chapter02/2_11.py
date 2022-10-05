from math import *
from math_xiaoqi import *
from vector_drawing import *

polar_coords = [(cos(5*x*pi/500.0), 4*pi*x/1000.0) for x in range(0,1000)]

# print([polar_coords])

vectors = [to_cartesian(p) for p in polar_coords]

draw(
    Polygon(*vectors, color=red)
)

# change the number of 5 or 4, you can get different shape of flowers
# see 2_11_Figure.png for the current output
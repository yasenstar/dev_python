from vector_drawing import *
from math_xiaoqi import *

draw(
    Points(*[(x,square(x)) for x in range(-10,20)]),
    Polygon(*[(x,square(x)) for x in range(-10,20)]),
    grid=(1,10),
    nice_aspect_ratio=False
)

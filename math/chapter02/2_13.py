from math import *
from math_xiaoqi import *
from vector_drawing import *

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
                (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0),
                (0,-3), (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)]

new_dino1 = translate((8,8), rotate(-45,dino_vectors))
new_dino2 = rotate(-45, translate((8,8), dino_vectors))

draw(
    Polygon(*dino_vectors, color=gray),
    Polygon(*new_dino1, color=red),
    Polygon(*new_dino2, color=blue)
)
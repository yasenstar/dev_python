from math_xiaoqi import *
from vector_drawing import *

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
                (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0),
                (0,-3), (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)]

print([vector_length(v) for v in dino_vectors])

print(max(dino_vectors, key=vector_length))

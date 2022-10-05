from draw3d import *
from math import *

dots = [(a,b,c)
        for a in (-1,1)
        for b in (-1,1)
        for c in (-1,1)
        ]

edges = [((-1,b,c),(1,b,c)) for b in (-1,1) for c in (-1,1)] +\
        [((a,-1,c),(a,1,c)) for a in (-1,1) for c in (-1,1)] +\
        [((a,b,-1),(a,b,1)) for a in (-1,1) for b in (-1,1)]

print(dots)
print(edges)

draw3d(
    Points3D(*dots, color=blue),
    *[Segment3D(*edge) for edge in edges]
)
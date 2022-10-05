from draw3d import *
from math_xiaoqi import *

v = (1,2,3)
t = 3
w = vector_multiply3D(v,t)

draw3d(
    Points3D(v),
    Box3D(*v),
    # Arrow3D(v),
    Points3D(w),
    Box3D(*w),
    # Arrow3D(w)
    Segment3D(v,w)
)
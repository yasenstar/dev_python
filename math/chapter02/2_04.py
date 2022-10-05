from math_xiaoqi import *

u, v, w = (-2,0), (1.5,1.5), (4,1)

print("u =",u,"v =",v,"w =",w)

print("u+v =", vector_add(u,v))

print("v+w =", vector_add(v,w))

print("u+w =", vector_add(u,w))

print("u+v+w =", vector_add(vector_add(u,v),w))

print("u+v+w =", vector_add_all(u,v,w))

print(vector_scale(5,u))

trans = (1,1)

vectors = [(1,1), (0,-3), (-3,-3)]

print(translate(trans,vectors))

print(distance(u,v))
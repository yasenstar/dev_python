from math_xiaoqi import *

print(list(zip(*[(1,1,3),(2,4,-4),(4,2,-2)])))

zipped = list(zip(*[(1,1,3),(2,4,-4),(4,2,-2)]))

print(list(sum(coords) for coords in zipped))

print(tuple(sum(coords) for coords in zipped))
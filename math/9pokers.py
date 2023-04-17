import random
import time

start = [0,0,0,0,0,0,0,0,0]

end = [1,1,1,1,1,1,1,1,1]

i = 1

while start != end and i <= 10:
    x1 = random.randrange(0,8)
    x2 = random.randrange(0,8)
    while x2 == x1:
        x2 = random.randrange(0,8)
    print(x1,x2)
    if start[x1] == 0:
        start[x1] = 1
    else:
        start[x1] = 0
    if start[x2] == 0:
        start[x2] = 1
    else:
        start[x2] = 0
    print(start)
    time.sleep(0.5)
    i = i + 1

print(end)
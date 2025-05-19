from math import *

x = copysign(1, eval(input()))
y = copysign(1, eval(input()))

quad = {
    (1, 1): 1,
    (-1, 1): 2,
    (-1, -1): 3,
    (1, -1): 4,
}

print(quad[(x, y)])

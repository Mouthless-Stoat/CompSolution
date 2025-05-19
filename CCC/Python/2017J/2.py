from math import *

n = eval(input())
k = eval(input())

print(int(sum(map(lambda x: n * (pow(10, x)), range(k + 1)))))

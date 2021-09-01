import random
import math

values = []
for i in range(1,1000):
    values.append(random.randint(1, 1000))
values.sort()
print ( values )

def BinarySearch(k,r):
    l = 0
    r = 1000

    while (l <= r):
        m = math.floor((1 + r) / 2)
        if (k == values[m]):
            return m
        elif (k < values[m]):
            r = m - 1
        else:
            l = m + 1
    return -1
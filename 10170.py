import math
from sys import stdin

for line in stdin:
    s,d = map(int, line.split(' ')) 
    print(math.ceil((-1 + (1 - (4 * 1 * (-(s ** 2) + s - 2 * d))) ** 0.5) / 2))
    
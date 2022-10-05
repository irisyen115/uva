import math
from sys import stdin

for line in stdin:
    if line.strip() == "0 0": 
        break
    a,b = map(int, line.split(' '))
    print(f"{(math.floor(b ** 0.5) - math.ceil(a ** 0.5)) + 1}")
     
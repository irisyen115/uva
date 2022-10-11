from collections import Counter
from sys import stdin

n = int(stdin.readline())
country = []
for x in range(n):
    input = stdin.readline().split()
    country.append(input[0]) 
c = Counter(country)
keys = sorted(c.keys())
for v in keys:
    print(f'{v} {c[v]}')
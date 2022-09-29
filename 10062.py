from sys import stdin
from collections import Counter

for line in stdin:
    if line.strip() == "": 
        break
    n = line.strip()
    c = Counter(n)
    names = []
    ascii = [] 
    for i,v in enumerate(n):
        if i == n.index(v):
            names.append(ord(v))
            ascii.append(c[v])
    for a,b in sorted(zip(names,ascii)):
        print(f'{a} {b}')
from sys import stdin
from collections import Counter

for i,line in enumerate(stdin):
    n = line.rstrip('\r\n')
    c = Counter(n)
    x = list(c.items())
    x.sort(key=lambda t:( t[1],-(ord(t[0]))))
    if i != 0:
        print('')
    for a,b in x:
        print(f'{ord(a)} {b}') 
    
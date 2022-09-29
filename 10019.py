from sys import stdin
from collections import Counter

n = int(stdin.readline())
for x in range(n):
    m = int(stdin.readline())    
    x = int(str(m),16)
    print(f'{bin(m)[2:].count("1")} {bin(x)[2:].count("1")}')
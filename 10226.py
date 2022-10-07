from collections import Counter
from sys import stdin

n = int(stdin.readline())
for x in range(n):
    a = []
    for i,line in enumerate(stdin):
        if line.strip() != '':
            a.append(line.strip())
        if i != 0 and line.strip() == '':
            break
    c = Counter(a)
    if x != 0:
        print('')
    keys = sorted(c.keys())
    for v in keys:
        value = '%.4f'%(c[v]/len(a)*100)
        print(f'{v} {value}') 
        
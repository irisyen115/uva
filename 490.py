import itertools
from sys import stdin

for line in stdin:    
    if line.strip() == "": 
        break
    a = (line + stdin.read()).split('\n')
    a = a[:-1]
    a.reverse()
    for col in itertools.zip_longest(*a,fillvalue=' '):        
        for v in col:
            ans = ""
            ans += v
            print(ans,end='')
        print('')
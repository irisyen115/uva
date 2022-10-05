from collections import Counter
from sys import stdin

for line in stdin:
    a = line
    b = stdin.readline()
    c = Counter(a.strip())
    d = Counter(b.strip())
    ans = ""
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        ans = ans + (ch * min(c[ch], d[ch]))
    print(ans)
    
    

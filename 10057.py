from sys import stdin

for line in stdin:
    if line.strip() == "": 
        break
    n, l = int(line), []
    for _ in range(n):
        l.append(int(stdin.readline()))
    l = sorted(l)
    s,t = l[(n-1)//2] , l[n//2]
    if s == t:
        print(f'{s} {l.count(s)} {1}')
    else:
        print(f'{s} {l.count(s)+l.count(t)} {t-s+1}')
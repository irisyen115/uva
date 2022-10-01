from sys import stdin

n = int(stdin.readline())
for x in range(n):
    d = [0] * (int(stdin.readline()))
    p = int(stdin.readline())
    for y in range(p):
        pi = int(stdin.readline())
        for i in range(pi-1 , len(d), pi):
            d[i] = 1
    ans = 0
    for i,v in enumerate(d):        
        if i % 7 != 5 and i % 7 != 6:
            ans += v
    print(ans)
from sys import stdin

n = int(stdin.readline())
for x in range(n):
    a,b = map(int, stdin.readline().split())
    c = (a + b) / 2
    d = a - c
    if (c >= 0 and d  >= 0) and (a+b) % 2 == 0:
        print(f'{int(c)} {int(d)}')
    else:
        print('impossible')

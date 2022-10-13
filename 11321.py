from sys import stdin

for line in stdin:
    if line.strip() == "0 0":
        break
    n,m = map(int,line.split())
    d = {}
    for i in range(n):
        input = stdin.readline().strip()
        d[input] = int(input) % m
    print(sorted(d.items(), key=lambda x:x[1]))
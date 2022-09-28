from sys import stdin

for line in stdin:
    if line.strip() == "": 
        break
    n, m = map(int, line.split(' '))
    print(n * m * 2)
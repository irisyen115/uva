from sys import stdin

for line in stdin:
    if line.strip() == "0":
        break
    n = int(line)
    a = 0
    while n > 0:
        a += n % 10
        n //= 10
        if a >= 10 and n == 0:
            n = a
            a = 0
    print(a)
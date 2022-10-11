from sys import stdin

def degree(n):
    a = 0
    if n < 10:
        return 1
    while n > 0:
        a += (n % 10)
        n //= 10    
    else:
        return (1 + degree(a))

for line in stdin:
    if line.strip() == "0":
        break
    n = int(line)
    if n % 9 == 0:
        if n >= 10:
            print(f'{n} is a multiple of 9 and has 9-degree {degree(n) -1}.')
        else:
            print(f'{n} is a multiple of 9 and has 9-degree 1.')
    else:
        print(f'{n} is not a multiple of 9.')
from sys import stdin

for line in stdin:
    if line.strip() == "0":
        break
    n = int(line)
    if n % 11 == 0:
        print(f'{line.strip()} is a multiple of 11.')
    else:
        print(f'{line.strip()} is not a multiple of 11.')
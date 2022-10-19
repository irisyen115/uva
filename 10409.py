from sys import stdin

for line in stdin:
    if line.strip() == "0":
        break
    n = int(line.strip())

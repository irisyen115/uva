from sys import stdin

for line in stdin:
    if line.strip() == "0": 
        break
    n = bin(int(line))[2:]
    x = str(n).count("1")
    print(f"The parity of {n} is {x} (mod 2).")
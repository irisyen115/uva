from sys import stdin

def process(line):
    n, m = map(int, line.split(' '))
    a = []    
    if m == 0  or m == 1 or n == 0 or n == 1:
        print("Boring!")
        return
    while n >= 1 :        
        a.append(str(n))        
        if n != 1 and n % m != 0:
            print("Boring!")
            return
        n = n // m
    print(' '.join(a))

for line in stdin:
    if line.strip() == '': # If empty string is read then stop the loop
        break
    process(line) # perform some operation(s) on given string

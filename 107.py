import math
from sys import stdin

def process(line):    
    h,c = map(int, line.split(' '))    
    n = 0
    if c == 1:
        n = 1
        k = int(math.log(h , n+1))
        num = k+1
    else:
        L, R = 0, c + 1
        while L + 1 < R:
            n = ( L + R ) // 2
            diff = math.log(h, n+1) - math.log(c, n)
            if abs(diff) < 1e-9 : break
            elif diff < 0: L = n
            else: R = n
        k = int(math.log(h , n+1))
        num = int((1 * ((n ** k) -1))/(n - 1))
    print(str(num)+" "+ str((h-c)*n+h))

for line in stdin:
    if line.strip() == "0" + " " + "0": # If empty string is read then stop the loop
        break
    process(line) # perform some operation(s) on given string
from sys import stdin

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
n = int(stdin.readline())
for x in range(n):
    s1 = int(stdin.readline(),2)
    s2 = int(stdin.readline(),2)
    l = gcd(s1,s2)
    if l != 0 and l != 1:
        print(f"Pair #{x+1}: All you need is love!")
    else:
        print(f"Pair #{x+1}: Love is not all you need!")        

from sys import stdin
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

d = {}
for line in stdin:
    if line.strip() == "0":
        break
    n = int(line)
    g = n-1
    for i in range(2,n):
        for j in range(i+1,n+1):             
            if (i,j) not in d:     
                d[(i,j)] = gcd(i,j)                            
            g += d[(i,j)]  
        if i > n:
            break
    print(g)
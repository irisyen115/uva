from sys import stdin

for line in stdin:
    if line.strip() == "": 
        break
    a,b = map(int, line.split(' '))    
    print(abs(a-b))
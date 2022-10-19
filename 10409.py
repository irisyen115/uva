from sys import stdin

for line in stdin:
    if line.strip() == "0":
        break
    n = int(line.strip())
    top, north, west = 1, 2, 3
    for _ in range(n):
        a = stdin.readline().strip()        
        if a == 'east':                        
            top, west = west, 7 - top             
        elif a == 'west':            
            top, west = 7 - west, top            
        elif a == 'north':            
            top, north = 7 - north, top            
        elif a == 'south':            
            top, north = north, 7 - top            
    print(top)
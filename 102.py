from sys import stdin

def process(line):    
    bottoms = list(map(int, line.split(' ')))
    First = [bottoms[i] for i in range(3)]
    Second = [bottoms[i] for i in range(3,6)]
    Third = [bottoms[i] for i in range(6,9)]        
    names = ["BGC","BCG","GBC","GCB","CBG","CGB"]
    count = [0] * 6
    count[0] = (First[1]+First[2])+(Second[0]+Second[2])+(Third[0]+Third[1])
    count[1] = (First[1]+First[2])+(Second[0]+Second[1])+(Third[0]+Third[2])
    count[2] = (First[0]+First[2])+(Second[1]+Second[2])+(Third[0]+Third[1])
    count[3] = (First[0]+First[2])+(Second[0]+Second[1])+(Third[1]+Third[2])
    count[4] = (First[0]+First[1])+(Second[1]+Second[2])+(Third[0]+Third[2])
    count[5] = (First[0]+First[1])+(Second[0]+Second[2])+(Third[1]+Third[2])
    c = sorted(zip(count, names))
    res, name = c[0]
    print(name + " " + str(res))
    
    



for line in stdin:
    if line.strip() == "": # If empty string is read then stop the loop
        break
    process(line) # perform some operation(s) on given string
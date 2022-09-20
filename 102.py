from sys import stdin

def process(line):    
    bottoms = list(map(int, line.split(' ')))
    first, second, third = bottoms[:3], bottoms[3:6], bottoms[6:]       
    names = ["BGC","BCG","GBC","GCB","CBG","CGB"]
    count = [0] * 6
    count[0] = (first[1]+first[2])+(second[0]+second[2])+(third[0]+third[1])
    count[1] = (first[1]+first[2])+(second[0]+second[1])+(third[0]+third[2])
    count[2] = (first[0]+first[2])+(second[1]+second[2])+(third[0]+third[1])
    count[3] = (first[0]+first[2])+(second[0]+second[1])+(third[1]+third[2])
    count[4] = (first[0]+first[1])+(second[1]+second[2])+(third[0]+third[2])
    count[5] = (first[0]+first[1])+(second[0]+second[2])+(third[1]+third[2])
    res, name = min(zip(count, names))
    print(f'{name} {res}')

for line in stdin:
    if line.strip() == "": # If empty string is read then stop the loop
        break
    process(line) # perform some operation(s) on given string
from sys import stdin

def process(line):    
    n = int(line)

    x = int((1+(1+ 8 * n) ** 0.5) / 2)
    s = int(((1+x)*x)/2)

    print(str(s-n) + " " + str(x))



for line in stdin:
    if line.strip() == "0": # If empty string is read then stop the loop
        break
    process(line) # perform some operation(s) on given string
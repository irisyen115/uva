from sys import stdin

def process(line):    
    SF = 1
    M = F = 0
    n = int(line)
    while n > 0:
        NM = SF + M +F
        NF = M
        M = NM
        F = NF
        n -= 1    
    print(str(M) + " " + str(SF + M + F))


for line in stdin:
    if line.strip() == "-1": # If empty string is read then stop the loop
        break
    process(line) # perform some operation(s) on given string



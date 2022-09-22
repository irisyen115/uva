from sys import stdin

def process(line):    
    a,b = map(int, line.split(' '))
    count = 0
    carry = 0
    while (a > 0 and b > 0) or carry > 0:
        if (a % 10) +  (b % 10) + carry >= 10:
            count+=1
            carry = 1
        else:
            carry = 0
        a//=10
        b//=10
    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print(f'{count} carry operations.')

for line in stdin:
    if line.strip() == "0" + " " + "0": # If empty string is read then stop the loop
        break
    process(line) # perform some operation(s) on given string
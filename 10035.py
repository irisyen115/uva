from sys import stdin

for line in stdin:
    if line.strip() == "0" + " " + "0": # If empty string is read then stop the loop
        break
    a,b = map(int, line.split(' '))
    count = 0   
    carry = 0 
    while (a > 0 and b > 0) or carry > 0:
        carry = ((a % 10) +  (b % 10) + carry >= 10)
        count += carry        
        a//=10
        b//=10
    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print(f'{count} carry operations.')
    
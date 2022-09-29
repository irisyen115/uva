from sys import stdin

def process(line):    
    nums = list(map(int, line.split(' ')))
    n = nums[0]
    diff = [abs(nums[i+1] - nums[i]) for i in range (1, n)]
    s = set(range(1, n))    
    for v in diff:
        if v not in s:            
            print("Not jolly")
            break
        s.remove(v)
    else:
        print("Jolly")
        
    

for line in stdin:
    if line.strip() == "": # If empty string is read then stop the loop
        break
    process(line) # perform some operation(s) on given string
from sys import stdin

def process(line):    
    nums = list(map(int, line.split(' ')))
    n = nums[0]
    diff = [abs(nums[i+1] - nums[i]) for i in range (1, n)]    
    diff = set(diff)    
    if (min(diff) == 1 and max(diff) == n-1) and len(diff) == n-1:
        print("Jolly")           
    else:
        print("Not jolly") 
        
    

for line in stdin:
    if line.strip() == "": # If empty string is read then stop the loop
        break
    process(line) # perform some operation(s) on given string
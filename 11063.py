from collections import Counter
from sys import stdin

def is_duplicated(nums):
    a = [] 
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if (nums[i] + nums[j]) in a:
                return True
            a.append(nums[i] + nums[j])
    return False

def sortt(nums):
    for i in range(len(nums)):
        if i > 0:
            if nums[i-1] >= nums[i]:
                return False
    return True

for x,line in enumerate(stdin):
    n = int(line.strip())
    nums = list(map(int, stdin.readline().split(' ')))
    try:
        _ = stdin.readline()
    except Exception as e:
        pass
    if x != 0:
        print('')
    if sortt(nums) == False:
        print(f'Case #{x+1}: It is not a B2-Sequence.')
    elif nums[0] < 1:
        print(f'Case #{x+1}: It is not a B2-Sequence.')
    else:
        if is_duplicated(nums):
            print(f'Case #{x+1}: It is not a B2-Sequence.')
        else:
            print(f'Case #{x+1}: It is a B2-Sequence.')
print('')
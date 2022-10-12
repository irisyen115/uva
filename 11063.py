from sys import stdin

def is_duplicated(nums):
    a = set()
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if (nums[i] + nums[j]) in a:
                return True
            a.add(nums[i] + nums[j])
    return False

for x,line in enumerate(stdin):
    n = int(line.strip())
    nums = list(map(int, stdin.readline().rstrip('\r\n').split(' ', n - 1)))
    _ = stdin.readline()
    if any(nums[i-1] >= nums[i] for i in range(1, n)):
        print(f'Case #{x+1}: It is not a B2-Sequence.')
    elif nums[0] < 1:
        print(f'Case #{x+1}: It is not a B2-Sequence.')
    else:
        if is_duplicated(nums):
            print(f'Case #{x+1}: It is not a B2-Sequence.')
        else:
            print(f'Case #{x+1}: It is a B2-Sequence.')
    print('')
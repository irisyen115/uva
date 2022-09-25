import statistics
from sys import stdin

n = int(stdin.readline())
for x in range(n):
    nums = stdin.readline().split()
    n = int(nums[0])
    homes = sorted([int(nums[i]) for i in range(1,len(nums))])
    s = 0
    if n % 2 == 1:
        s = homes[n//2]
    else:
        s = (homes[(n//2)-1] + homes[n//2])/2
    sum = 0
    for v in homes:
        sum += abs(v-s)
    print(int(sum))

from sys import stdin

n = int(stdin.readline())
for x in range(n):
    nums = stdin.readline().split()
    n = int(nums[0])
    homes = sorted([int(nums[i]) for i in range(1,len(nums))])
    s = (homes[(n-1)//2] + homes[n//2])/2
    ans = sum(abs(v-s)for v in homes)     
    print(int(ans))

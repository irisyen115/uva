from sys import stdin

data = stdin.readlines()
a, b = 0, 1
while a < len(data):
    x = int(data[a])
    nums = list(map(int, data[b].split()))[:-1]
    n = len(nums)
    s = 0
    for v in nums:
        s = s * x + v * n
        n = n - 1
    print(s)
    a, b = a + 2, b + 2
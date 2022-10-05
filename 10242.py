from sys import stdin
from collections import Counter

for line in stdin:
    nums = list(map(float, line.split()))
    try:
        sq = [(nums[0],nums[1]),(nums[2],nums[3]),(nums[4],nums[5]),(nums[6],nums[7])]
        c = Counter(sq)
        sum_x = 0
        sum_y = 0
        for v in sq:
            if c[v] == 1:
                sum_x += v[0]
                sum_y += v[1]
        for v in sq:
            if c[v] == 2:
                sum_x-=v[0]
                sum_y-=v[1]
                break
        x = '%.3f'%sum_x
        y = '%.3f'%sum_y
        print(f'{x} {y}')
    except Exception as e:
        break


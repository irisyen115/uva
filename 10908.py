from sys import stdin

def check(nums,x,y):
    edge = 1
    visited = set((x,y))
    level = [(x, y)] # 第一圈
    while True:
        next_level = []
        for (i,j) in level:            
            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    if (i+a) < 0 or (i+a) > len(nums)-1 or (j+b) < 0 or (j+b) > len(nums[0])-1 :
                        return edge
                    elif (i+a,j+b) in visited: 
                        continue
                    else:
                        visited.add((i+a,j+b))
                        next_level.append((i+a,j+b))
        if any(nums[i][j] != nums[x][y] for (i,j) in next_level):
            return edge            
        else:
            edge+=2
            level = next_level 
            
n = int(stdin.readline())
for _ in range(n):
    M,N,Q = map(int, stdin.readline().split())
    square = [list(stdin.readline().strip()) for _ in range(M)]
    print(f'{M} {N} {Q}')
    for _ in range(Q):
        x,y = map(int, stdin.readline().split())
        print(check(square,x,y))
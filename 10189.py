from sys import stdin

def check(board, x, y):
    if x < 0 or x > a-1 or y < 0 or y > b-1:
        return 0
    else:
        if board[x][y] == "*":
            return 1
        else:
            return 0

for x, line in enumerate(stdin):
    if line.strip() == "0 0":
        break
    a,b = map(int, line.split())
    mines = [list(stdin.readline().strip()) for _ in range(a)]
    if x != 0:
        print('')
    print(f'Field #{x+1}:')
    for i, row in enumerate(mines):
        arr = []
        for j, v in enumerate(row):
            s = 0
            if mines[i][j] == "*":
                arr.append("*")
            else:
                for c in [-1, 0, 1]:
                    for d in [-1, 0, 1]:
                        s = sum(check(mines, i + c, j + d) for c in [-1, 0, 1] for d in [-1, 0, 1])            
                arr.append(str(s))        
        print(''.join(arr).strip())
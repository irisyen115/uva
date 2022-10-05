from sys import stdin

n = int(stdin.readline())
for x in range(n):
    a, b = int(stdin.readline()) | 1, (int(stdin.readline()) - 1) | 1
    print(f'Case {x+1}: {(a + b) * (b - a + 2) // 4}')
    
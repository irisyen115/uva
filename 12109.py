from sys import stdin

n = int(stdin.readline())
for _ in range(n):    
    date = [31,28,31,30,31,30,31,31,30,31,30,31]
    cal = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    m, d = map(int,stdin.readline().strip().split())
    a = (sum(date[i] for i in range(m-1)) + d - 10) % 7 
    print(cal[a])
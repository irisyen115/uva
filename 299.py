from sys import stdin
from typing import Counter

n = int(stdin.readline())
for x in range(n):
    count = 0
    m = int(stdin.readline())
    input = stdin.readline()
    car = input.split()
    for i in range(m):
        car[i] = int(car[i])
    c = m
    while c > 1:
        for i in range(c-1):
            tmp = 0
            if car[i] > car[i+1]:
                tmp = car[i]
                car[i] = car[i+1]
                car[i+1] = tmp
                count+=1
        c-=1
    print("Optimal train swapping takes "+ str(count)+ " swaps.")
    
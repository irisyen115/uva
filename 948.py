from sys import stdin

n = int(stdin.readline())
fib = "1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155"
f_list = list(map(int, fib.split()))
for x in range(n):        
    input = stdin.readline()
    a = 0
    b = int(input)
    ans = ""
    for i in range(len(f_list)-1):
        if f_list[i] == b:
            a = i
            break
        if f_list[i] < b <= f_list[i+1]:
            a = i+1
            break
    while a >= 0:
        if f_list[a] <= b:
            b -= f_list[a]
            ans += "1"  
            if a > 0:
                ans += "0"
            a-=2                         
        else:
            ans += "0"
            a -= 1
    # print(input.strip() + " " + "=" + " " + ans[ans.index("1"):] + " " + "(fib)")
    print(f'{input.strip()} = {ans[ans.index("1"):]} (fib)')
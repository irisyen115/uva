from sys import stdin
from typing import Counter

n = int(stdin.readline())
ans = ""
for x in range(n):
    input = stdin.readline()
    input = input.upper()
    for ch in input:
        if 65 <= ord(ch) <= 90:
            ans += ch
        else:
            continue
c = Counter(ans).most_common()
c.sort(key=lambda x: (-x[1], x[0]))
for a, b in c:
    print(a + " " + str(b))

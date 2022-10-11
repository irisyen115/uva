from sys import stdin

for line in stdin:
    code = ['d','m','b','g','t','h','j','k','p','l',';','\'','.',',','[',']','e','y','f','u','o','n','r','v','i','c']
    ans = ""
    for v in line.strip():
        if v in code:
            ans += chr(97+code.index(v))
        else:
            ans += v
    print(ans)
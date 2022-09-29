from sys import stdin

count = 0
for ch in stdin.read():
    if ch == "\"":
        count+=1
        if count % 2 == 0: ch = "''"
        else: ch = "``"
    print(ch,end='')
     
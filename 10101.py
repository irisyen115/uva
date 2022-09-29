from sys import stdin
order = ['', 'shata' , 'hajar', 'lakh']
basis = [100, 10, 100, 100] 
def Bangla(n):
    global order,basis
    ans = []    
    idx = 0
    a = []
    if n > 10 ** 7:
        x = n % (10 ** 7)
        n = n // (10 ** 7)    
    else:
        x = n
        n = n // (10 ** 7)
    while x > 0:
        a.append(x % basis[idx])
        x //= basis[idx]
        idx += 1
    b = reversed(list(zip(a,order)))
    for num, unit in b:
        ans.append(f'{num} {unit}')
    if n == 0:         
        return ' '.join(ans)
    else:      
        return f'{Bangla(n)}' + 'kuti ' + ' '.join(ans)
    
for i,line in enumerate(stdin):
    if line.strip() == "": 
        break
    n = int(line)
    if n == 0:
        print(f"   {i+1}. "+str(0))
    if n == 10**7:
        print(f'{i + 1: >4}. 1kuti')
    else:
        print(f'{i + 1: >4}. {Bangla(n)}')

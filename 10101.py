from sys import stdin
basis = [('lakh', 10 ** 5), ('hajar', 10**3), ('shata', 100)]
def Bangla(n):
    global basis
    ans = []    
    if n >= 10 ** 7:
        x = n % (10 ** 7)
        n = n // (10 ** 7)    
    else:
        x = n
        n = n // (10 ** 7)
    for unit, base in basis:
        if x >= base: 
            ans.append(f'{x // base} {unit}')
        x %= base
    if 0 < x < 100:
        ans.append(str(x))        
    if n == 0:         
        return ' '.join(ans)
    else:      
        if ' '.join(ans) == '':
            return f'{Bangla(n)} ' + 'kuti'
        return f'{Bangla(n)} ' + 'kuti ' + ' '.join(ans)
    
for i,line in enumerate(stdin):
    if line.strip() == "": 
        break
    n = int(line)
    if n == 0:
        print(f"{i + 1: >4}. {str(0)}")
    else:
        print(f'{i + 1: >4}. {Bangla(n)}')

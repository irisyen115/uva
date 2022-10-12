from sys import stdin

for line in stdin:
    code = {'d':'a',
    'm':'b',
    'b':'c',
    'g':'d',
    't':'e',
    'h':'f',
    'j':'g',
    'k':'h',
    'p':'i',
    'l':'j',
    ';':'k',
    '\'':'l',
    '.':'m',
    ',':'n',
    '[':'o',
    ']':'p',
    'e':'q',
    'y':'r',
    'f':'s',
    'u':'t',
    'o':'u',
    'n':'v',
    'r':'w',
    'v':'x',
    'i':'y',
    'c':'z'}
    ans = ""
    for v in line.strip():
        ans += code.get(v,v)        
    print(ans)
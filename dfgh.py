a = ['nicola','balentin','sasha','stas','uri']
b = 0
ss = ''
for i in a:
    if list(i)[0] == 's':
        i = list(i)
        i[0] = 'S'
        for iii in i:
            ss += iii
        a[b] = ss
    b+=1
    ss = ''
print(a)
        
        
        
def fibonazi(num):
    a=1
    b=1
    c=2
    while c<num:
        c += 1
        a,b=b,a+b
        yield b

l=[1,1]
c=fibonazi(9999**99999)
for i in c:
    l.append(i)
print(l)
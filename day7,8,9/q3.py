from math import *

m=[]
c=''
while c!='STOP':
    a=input()
    c=a.upper()
    m.append(c)

b=len(m)
x=0
y=0
if m[0]=='START' and m[b-1]=='STOP':
    for i in m:
        if i=='UP':
            x=x+1
        elif i=='DOWN':
            x=x-1
        elif i=='RIGHT':
            y=y+1
        elif i=='LEFT':
            y=y-1

x=abs(x)
y=abs(y)
d=x+y
print(d)

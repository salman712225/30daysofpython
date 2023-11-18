a=input()
b=a.lower()
c=list(b)
c.sort()
d=''
for i in range(len(c)):
    d=d+c[i]
print(d)

a=int(input())
f=[]
c=[]
k=0
if a>1:
    for i in range(2,a+1):
        if a%i==0:
            f.append(i)
for j in f:
    e=0
    for k in range(2,j):
        if j%k==0:
            e=1
    c.append(e)

for s in c:
    if s==1:
        ind=c.index(s)
        c.pop(ind)
        f.pop(ind)
for x in f:
    print(x)

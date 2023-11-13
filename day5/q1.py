n=int(input())
l=[]
c=[]
for i in range(3):
    s=int(input())
    l.append(s)
for j in l:
    t=l.count(j)
    c.append(t)
if c.count(1)==3 and sum(l)==n:
    print('FAIR')
else:
    print('UNFAIR')

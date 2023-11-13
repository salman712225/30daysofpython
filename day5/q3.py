e=[]
r=[]
for i in range(5):
    a=int(input())
    e.append(a)
for i in range(5):
    n1=(i-1)%5
    n2=(i+1)%5
    if ((e[n1]+e[i])%2==0) and ((e[n2]+e[i])%2==0) and ((e[n1]+e[n2]+e[i])%2==0):
        r.append(1)
    else:
        r.append(0)


if r.count(1)==5:
    print('YES')
else:
    print('NO')

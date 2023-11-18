a=int(input())
b=(a*2)-1
k=0
for i in range(2):
    if k==0:
        for j in range(2,a+2):
            h=list(range(1,j))
            for v in h:
                print(v,sep=',',end=' ')
            print(' ')
            k=k+1
        
    elif k==a:
        for u in range(a,1,-1):
            s=list(range(1,u))
            for t in s:
                print(t,sep=',',end=' ')
            print(' ')

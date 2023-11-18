a=input()
b=len(a)
c=[]
d=[]
e=0
if b==10  and (a[0] in ['6','7','8','9']):
    for i in range(b):
        if a[i].isdigit():
            c.append(int(a[i]))
            d.append(a.count(a[i]))
    if max(d)<=7:
        for j in range(int(b/2)):
            if a[j]==a[j+1]==a[j+2]==a[j+3]==a[j+4]==a[j+5]:
                e=1
        if e==1:
            print('Invalid')
        else:
            print('Valid')
            

            
    

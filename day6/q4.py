a=int(input())
b=int(input())
for i in range(1000,2000):
    if i%a==0 and i%b==0:
        print(i)
    else:
        print(0)

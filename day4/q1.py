a=int(input())
b=int(input())
c=int(input())
if a==b and b==c:
    print('Its a Equilateral Triangle')
elif a==b or b==c or a==c:
    print('Its a Isosceles Triangle')
elif a!=b and b!=c and c!=a:
    print('Its a Scalene Triangle')

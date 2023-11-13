t=int(input())
if t<0 or t>=24:
    print('INVALID')
elif t>=0 and t<=5:
    print('NIGHT')
elif t>=6 and t<=11:
    print('MORNING')
elif t>=12 and t<=17:
    print('AFTERNOON')
elif t>=18 and t<=23:
    print('EVENING')

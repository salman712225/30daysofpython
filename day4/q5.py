t=int(input('Temperature:'))
o=int(input('Convert temperature from \n 1-Celsius to fahrenheit \n 2- Fahrenheit to Celsius\nEnter Your choice(1 or 2):'))
if o==1:
    res=(((t*9)/5)+32)
elif o==2:
    res=(((t-32)*5)/9)
print(res)

import math

a=float(input('Enter the value of A: '))
b=float(input('Enter the value of B: '))
c=float(input('Enter the value of C: '))

if((a+b+c) > c and (a+c)>b and (c+b)>a):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print('Area of the Triangel is: ', area)
else:
    print('The Triangel is not possible.')
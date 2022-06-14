import math

a= float(input("enter the value of A: "))
b= float(input("enter the value of B: "))
c= float(input("enter the value of C: "))


d=(b*b)-(4*a*c)
if(d==0):
    print('Roots are real & equal & are: ',  x )
elif(d>0):
    x1=(-b+math.sqrt(d))/(2*a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print("Roots are real & unequal & are: ", x1,x2)
else:
    print('The roots are imaginary.')


    # dighat shomikoron er mul nirnoy er program
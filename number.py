
number = int(input('enter a number : '))

if(number % 2 == 0):
    print('this is even number')
elif(number == 0):
    print('this is 0')
else:
    print('this is odd numnner')

# --------------------------------------------

if(number > 0 ):
    print('this is positive')
elif(number == 0):
    print('this is zero')
else:
    print('this is negative')

# -------------------------------------------

number1 = int(input('enter a number1 : '))
number2 = int(input('enter a number2 : '))


if(number1 < number2 ):
    print('Smallest numer is =', number1 )
elif(number1 > number2):
    print('Smallest numer is =', number2)
else:
    print('two number is equal')


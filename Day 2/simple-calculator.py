##Simple Calculator

operator =  input('Pls Choose the Operator(+, -, * or /): ')

var1 = int(input('Enter your first Number: '))

var2 = int(input('Enter your second Number: '))

if operator  == '+':
    result = var1 + var2
    print(result)

elif operator  == '-':
    result = var1 - var2
    print(result)

elif operator  == '*':
    result = var1 * var2
    print(result)
    
elif operator  == '/':
    result = var1 / var2
    print(result)

else:
    print('Error occured ;<')

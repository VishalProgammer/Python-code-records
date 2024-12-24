#Degree Celsius to Fahrenheit Convertor

C = int(input('Enter temperature in Degree Celcius: '))
F = 0

if C:
    F = C * 9/5 + 32
    print(f'Temprature in Fahrenheit is: {F}°F')
elif C == 0:
    print('Temprature in Fahrenheit is: 32°F')
else:
    print('Some Error Occurred ;<')


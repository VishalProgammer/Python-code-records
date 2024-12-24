#Pounds or Kg Convertor

var1 = input('You want to Convert your weight to Pounds(lbs) or KiloGrams(kg): ')

if var1 == 'P' or var1 == 'pounds'or var1 == 'Pounds'or var1 == 'p' or var1 == 'lbs':
    weight = float(input('Enter your weight in Kilograms:' ))
    converted  =  weight * 2.205
    print(f'Your Weight in Pounds: {round(converted, 3)} lbs')

elif var1 == 'kg' or var1 == 'kgs' or var1 == 'Kg' or var1 == 'Kgs' or var1 == 'Kilograms' or var1 == 'kilograms':
    weight = float(input('Enter your weight in Pounds:' ))
    converted  =  weight / 2.205
    print(f'Your Weight in Kilograms: {round(converted, 3)} kg')

else:
    print('Choose Pound(lbs) or Kilogram(kg) to Convert!!')
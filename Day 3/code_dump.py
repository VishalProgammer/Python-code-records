import time

dun = 'sfesd'
print(dun.isalpha())

while True:
    age = int(input('age of your dog:'))
    if age == 0:
        print('Your Dog is not even born yet?!')
        print('Enter a valid age!')
    elif age < 0:
        print('Enter a valid age!')
    else:
        break

print(f'Your Dog is {age} Years Old!!')

for i in reversed(range(1,11)):
    print(i)
    time.sleep(1)
print('FUCK YOU!!')

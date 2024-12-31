#INR to USD

while True:
    curr = input('Which currency(INR or USD) you have?? [q to Quit] :') 
    if curr == 'inr' or curr == 'INR'or curr == 'Rupee' or curr == 'Rupees' or curr == 'rupees' or curr == 'rupee' or curr == '₹':
        while True:
            amount = float(input('Enter the Amount:'))
            if amount >= 0:
                amount /= 85
                print(f'You have almost ${amount: .2f}')
                break
            elif amount == '' or amount < 0:
                print('Enter a Valid Amount!!')
            else:
                print('Enter a Valid Amount!!')
                continue

    elif curr == 'usd' or curr == 'USD'or curr == 'Dollar' or curr == 'Dollars' or curr == 'dollars' or curr == 'dollar' or curr == '$':
            while True:

                amount2 = float(input('Enter the Amount:'))
                if amount2 >= 0:
                    amount2 *= 85
                    print(f'You have almost ₹{amount2:.2f}')
                    break
                elif amount == '' or amount < 0:
                    print('Enter a Valid Amount!!')
                else:
                    print('Enter a Valid Amount!!')
                    continue

    elif curr == 'q' or curr == 'Q':
        break
    else:
        print('Enter a valid Response!!')
        continue 

#TIMER CLOCK

import time

while True:
    sec  = input('Enter the timer period(in Secs):')
    if sec.isalpha() or not sec.isdigit():
        print("Enter a Value in Seconds(Positive Numbers)!!")
        continue
    elif sec.isdigit() and int(sec) >= 0:
        sec = int(sec)
        if sec >= 0 :
            for s in range(sec, 0 ,-1):
                sec = s % 60
                min = int(s/60) % 60
                hour = int(s/3600)
                print(f'{hour}:{min}:{sec}')
                time.sleep(1)
        print("TIME's UP!!")
        break
    elif int(sec) < 0:
        print('Timer can not be Nagetive!!')
        continue
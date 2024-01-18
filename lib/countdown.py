import time

def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number, sleep_time=1):
    while number > 0:
        print(f'{number} SECOND(S)!')
        time.sleep(sleep_time)  
        number -= 1
    print("HAPPY NEW YEAR!")

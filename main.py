import random

number = random.randint(1, 100)
attempt = 1
guess = int(input("Enter your number: "))

while(True):
    if (guess>number):
        guess = int(input("Enter another number. This is too big: "))
        attempt += 1
    elif (guess<number):
        guess = int(input("Enter another number. This is too small: "))
        attempt += 1 

    else:
        print(f"Boyahh!! You have guess it right in {attempt} attempts")
        break


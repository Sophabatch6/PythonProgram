import random
count = 0
print("Hello, What is your name?")
name = input(">>>")
print(f"well {name}, Try to guess my number in mind.")
number = random.choice(range(1, 101))
while True:
    user_number = int(input(">>>"))
    count += 1
    if user_number < number:
        print("Too low, Try again.")
        continue
    elif user_number > number:
        print("Too high, Try again.")
        continue
    else:
        print(f"It took you {count} to guess my number which was {number}")
        while True:
            yes_no = input("Do you want to play again? [Y/N]")
            if yes_no=='Y':
                break
            elif yes_no=='N':
                exit()
            else:
                print("I don't understand it!!!!")
                continue

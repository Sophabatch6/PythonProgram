import random
print("Welcome to Dices Game")
while True:
    total = 0
    number = input("Enter the number of dices you want to play with: ")
    if number.isdigit():
        number = int(number)
        if 0 < number <9:
            for i in range(0, number):
                numbers = random.choice(range(1, 7))
                total += numbers
                print(f"Dice {i+1} : {numbers}")
            print(f"RESULT: {total}")
        else:
            print("USAGE: Your number must be between 1 to 8")
            continue
    else:
        print("USAGE: Your number must be between 1 to 8")
        continue


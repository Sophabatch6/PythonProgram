total = 0
while True:
    number = input("Enter Number: ")
    if number == "EXIT" or number == "Exit" or number == "exit":
        exit()
    else:
        total += int(number)
        print(f"{total}")

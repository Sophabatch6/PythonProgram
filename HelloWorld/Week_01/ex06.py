while True:
    print("Enter a number: ")
    x = input()
    if x.isdigit():
        if int(x) % 2 == 0:
            print(x, "is EVEN")
        else:
            print(x, "is ODD")
    else:
        if x == "exit" or x == "EXIT" or x == "Exit":
            exit()
        else:
            print(x, "is not a valid number.")

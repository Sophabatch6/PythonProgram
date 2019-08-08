number1 = int(input("Enter a number: "))
number2 = int(input("Enter second number: "))
if number1<number2:
    print(f"{number1}<{number2}")
elif number1>number2:
    print(f"{number1}>{number2}")
else:
    print(f"{number1}=={number2}")

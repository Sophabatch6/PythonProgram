import random
n = int(input("Enter number: "))
for i in range(n):
    result = random.choices(range(100))
    print(result)

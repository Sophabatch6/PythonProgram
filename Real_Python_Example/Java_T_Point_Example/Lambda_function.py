x = lambda a: a + 10
print("sum = ", x(20))

x = lambda a, b: a + b + 10
print("sum = ", x(12, 23))


# ____________________________

def table(n):
    return lambda a: a * n;


n = int(input("Enter the number: "))
b = table(n)

for i in range(1, 11):
    print(n, "X", i, " = ", b(i))

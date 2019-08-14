print("bin() function")
x = 10
print("10 = ", bin(x))  # change to binary

# __________________________
print("bool() function")  #
test = []
print(test, "Is", bool(test))
test = [0]
print(test, "is", bool(test))
test = 120
print(bool(test))

# ___________________________
print("callable() function")  # to check function is callable or not
x = 30
print(callable(x))


def y():
    x = 30


print(callable(y))

# ________________________
print("sun() function")
s = sum([1, 2, 3, 4])
print(s)

s = sum({1, 2, 3, 4, 5}, 45)
print(s)

# ________________________
print("any() function")  # return true if any item in an iterable is true.
i = [4, 5, 3, 5, 0]
print(any(i))

i = {0, False}
print(any(i))

i = [0, False, 5]
print(any(i))

# _______________________
print("float() function")
print(float(9))
print(float(-34.55))

# _______________________
print("format() function")
print(format(123, "d"))  # integer
print(format(123.23455, "f"))  # float
print(format(123, "b"))  # binary

# _____________________
# list of numbers
lists = [1, 2, 3, 4, 5]

listIter = iter(lists)

# prints '1'
print(next(listIter))

# prints '2'
print(next(listIter))

# prints '3'
print(next(listIter))

# prints '4'
print(next(listIter))

# prints '5'
print(next(listIter))





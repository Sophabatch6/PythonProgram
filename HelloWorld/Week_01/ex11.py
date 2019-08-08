string = input("Enter String: ")
if string == "":
    print("Empty String")
else:
    string_upper = string.upper()
    string_lower = string.lower()
    string_revers = string[::-1]
    print(string_upper)
    print(string_lower)
    print(string_revers)

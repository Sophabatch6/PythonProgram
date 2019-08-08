string = input("Enter Any String: ")
if string == "":
    print("Empty")
else:
    print(f"{string[0]}")
    print(f"{string[len(string)-1]}")
new = ""
string = input("Enter a String: ")
for i in string:
    if 64 < ord(i) < 91:
        new += i.lower()
    else:
        new += i.upper()
print(new)
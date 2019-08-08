string = input("Enter A Sentence: ")
encode = ''
for char in string:
    if 64 < ord(char) < 78 or 96 < ord(char) < 110:
        encode += chr(ord(char)+13)
    else:
        encode += chr(ord(char)-13)
print(encode)
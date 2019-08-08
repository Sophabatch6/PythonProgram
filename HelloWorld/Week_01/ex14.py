arr = []
while True:
    a = input("Enter string: ")
    if a == "Generate":
        break
    arr.append(a)
for j in arr:
    print(f"<p>{j}</p>")

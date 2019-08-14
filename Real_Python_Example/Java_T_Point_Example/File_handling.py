import os

with open("file.txt", "r") as file:
    # file.write(input("\n"))
    files = file.readline()
    print(files)
    file.close()

# os.remove("file.txt")  # to remove file
# os.mkdir("name")

with open("hello.txt", "w") as file:
    file.write("hello world")

print("Файл записан")

with open("hello.txt", "r") as file:
    for line in file:
        print(line)
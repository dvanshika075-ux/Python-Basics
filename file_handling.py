file = open("notes.txt")

print(file)
file = open("notes.txt")

print(file.read())

file.close()
file = open("notes.txt")

print(file.readline())

file.close()
file = open("notes.txt")

print(file.readline())
print(file.readline())

file.close()
file = open("notes.txt")

print(file.readline())
print(file.readline())
print(file.readline())

file.close()
file = open("notes.txt", "a")

file.write("\nI am learning Python with ChatGPT.")

file.close()
file = open("notes.txt")
print(file.read())
file.close()
file = open("notes.txt", "a")

file.write("\nMy dream is to become an AI Engineer.")

file.close()
file = open("notes.txt", "w")
file.write("Python")
file.close()
file = open("notes.txt", "a")
file.write(" AI")
file.close()
file = open("notes.txt", "w")
file.write("Python")
file.close()

file = open("notes.txt", "a")
file.write(" AI")
file.close()
file = open("notes.txt", "w")
file.write("Python")
file.close()

file = open("notes.txt", "a")
file.write(" AI")
file.close()

file = open("notes.txt", "r")
print(file.read())
file.close()
with open("notes.txt", "r") as file:
    print(file.read())
with open("notes.txt", "a") as file:
    file.write("\nI love programming.")
with open("notes.txt", "r") as file:
    print(file.read())

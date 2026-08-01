fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))
numbers = [10,20,30,40,50]

print(len(numbers))
numbers = [50,10,40,20,30]

numbers.sort()

print(numbers)
letters = ["d","b","a","c"]

letters.sort()

print(letters)
numbers = [10,20,30,40]

numbers.reverse()

print(numbers)
numbers = [10,20,10,30,10]

print(numbers.count(10))
fruits = ["Apple","Banana","Mango"]

print(fruits.index("Banana"))
students = ["Rahul","Priya","Vanshika","Ankit"]

print(len(students))

students.reverse()

print(students)

print(students.index("Vanshika"))
a = [10,20,30]

print(len(a))
a = [3,2,1]

a.sort()

print(a)
a = [5,5,5,2]

print(a.count(5))
a = ["A","B","C"]

a.reverse()

print(a)
numbers = [10,20,30]

numbers.append(40)

print(len(numbers))
numbers = [5,1,4]

numbers.sort()

numbers.reverse()

print(numbers)
fruits = ["Apple","Banana","Apple","Mango"]

print(fruits.count("Apple"))
colors = ["Red","Blue","Green"]

colors.pop()

colors.append("Black")

print(colors)
students = ["A","B","C","D"]

students.remove("B")

students.insert(1,"X")

students.append("Y")

print(students)
fruits = ["Apple", "Banana", "Mango"]

new_fruits = fruits.copy()

print(new_fruits)
numbers = [10, 20, 30]

new_numbers = numbers.copy()

new_numbers.append(40)

print(numbers)
print(new_numbers)
list1 = [1, 2, 3]

list2 = [4, 5, 6]

list1.extend(list2)

print(list1)
fruits = ["Apple", "Banana"]

more = ["Mango", "Orange"]

fruits.extend(more)

print(fruits)
numbers = [1, 2]

numbers.append([3, 4])

print(numbers)
numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)
a = [10, 20]

b = a.copy()

b.append(30)

print(a)
print(b)
a = ["Python", "Java"]

b = ["C", "C++"]

a.extend(b)

print(a)
numbers = [1, 2]

numbers.append([3, 4])

print(numbers)
numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)
list1 = [10, 20]

list2 = list1.copy()

list2.extend([30, 40])

list2.remove(20)

print(list1)
print(list2)
games = ["BGMI", "Valorant"]

games.extend(["Minecraft", "Free Fire"])

games.append("GTA 6")

print(games)
cities = ["Delhi", "Mumbai"]

new = cities.copy()

new.append("Jalandhar")

cities.append("Chandigarh")

print(cities)
print(new)
numbers = [5, 10]

copy_numbers = numbers.copy()

copy_numbers.extend([15, 20])

numbers.append(25)

print(numbers)
print(copy_numbers)
fruits = ["Apple", "Banana"]

fruits.append(["Mango", "Orange"])

print(fruits)
students = ["Rahul", "Priya"]

backup = students.copy()

students.append("Vanshika")

backup.extend(["Riya", "Ankit"])

backup.remove("Priya")

print(students)
print(backup)

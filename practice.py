fruits = ["Apple", "Banana", "Mango"]
print("Before:", fruits)
fruits.append("Orange")
print("After:", fruits)
colors = ["Red", "Green", "Blue"]
print("Before:", colors)
colors.extend(["Yellow", "Purple"])
print("After:", colors)
fruits = ["Apple", "Banana", "Mango"]
fruits.append("orange")
fruits.append("grapes")
print(fruits)
shopping = ["milk", "bread"]
shopping.append("eggs")
print(shopping)
fruits = ["Apple", "Banana", "Mango"]
print("Before:", fruits)
fruits.insert(2, "Orange")
print("After:", fruits)
colours = ["Red", "Blue"]
print("Before:", colours)
colours.insert(2, "Green")
print("After:", colours)
fruits = ["Apple", "Banana", "Mango", "Orange"]
fruits.remove("Banana")
print(fruits)
fruits.pop(1)
print(fruits)
animals = ["Dog", "Cat", "Elephant", "Lion"]
animals.remove("Cat")
print(animals)
animals.pop(2)
print(animals)
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(len(fruits)) 
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Before:", fruits)
fruits.clear()
print("After:", fruits)
colours = ["Red", "Green", "Blue" , "Yellow", "Purple"]
print(colours.count("Green"))
animals = ["Dog", "Cat", "Elephant", "Lion"]
print(animals.index("Elephant"))
numbers = [10, 20, 30, 20, 40, 50]
print(len(numbers))
print(numbers.count(20))
numbers.remove(20)
print(numbers)
print(len(numbers))
print(numbers.index(40))
numbers = [10, 20, 30, 40, 50]
print("Before:", numbers)
numbers.sort()
print("After:", numbers)
fruits = ["Banana", "Apple", "Mango", "Orange"]
fruits.sort()
print(fruits)
names = ["John", "Alice", "Bob", "David"]
names.sort()
print(names)
marks = [85, 92, 78, 90, 88]
marks.sort()
print(marks)
print(len(marks))
print(marks.count(90))
print(marks.index(78))
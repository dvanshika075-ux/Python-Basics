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
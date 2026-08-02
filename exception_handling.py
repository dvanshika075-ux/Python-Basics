num = int(input("Enter a number: "))

print(100 / num)
try:
    num = int(input("Enter a number: "))

    print(100 / num)

except:
    print("Something went wrong.")
try:
    num = int(input("Enter number:"))

    print(50 / num)

except:
    print("Invalid Input")
try:
    age = int(input("Enter Age:"))

    print(age)

except:
    print("Please enter numbers only.")
try:
    a = int(input("First Number:"))
    b = int(input("Second Number:"))

    print(a / b)

except:
    print("Cannot Divide.")
try:

    print("Hello")

except:

    print("Error")
try:
    print("Start")

    print(10/0)

    print("End")

except:
    print("Error")
try:
    print("A")

    print("B")

except:
    print("Error")
print("C")
try:
    print("Python")

except:
    print("Error")

print("AI")
try:
    age = int(input("Age:"))

except ValueError:
    print("Numbers only.")
try:
    print(10 / 2)

except:
    print("Error")
try:
    print(10 / 0)

except:
    print("Cannot Divide by Zero")
try:
    num = int(input("Enter Number : "))

    print(num)

except:
    print("Please Enter Numbers Only")
try:
    a = int(input("First Number : "))
    b = int(input("Second Number : "))

    print(a / b)

except:
    print("Something Went Wrong")
try:
    print("Python")

except:
    print("Error")

else:
    print("Program Executed Successfully")
try:
    print(20 / 0)

except:
    print("Division Error")

else:
    print("Success")
try:
    age = int(input("Enter Age : "))

except ValueError:
    print("Invalid Input")
try:
    num = int(input("Enter Number : "))

    print(100 / num)

except ZeroDivisionError:
    print("Number Cannot Be Zero")

except ValueError:
    print("Only Numbers Allowed")
try:
    print("Start")

    x = 10 / 2

    print("End")

except:
    print("Error")

else:
    print("Everything is Fine")
try:
    print("Start")

    x = 10 / 0

    print("End")

except:
    print("Exception Occurred")

print("Program Finished")
try:
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))

    result = a / b

except ZeroDivisionError:
    print("Cannot Divide By Zero")

except ValueError:
    print("Please Enter Valid Numbers")

else:
    print("Result =", result)

print("Thank You")

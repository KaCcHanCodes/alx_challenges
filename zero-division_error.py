#this program takes two numbers as input
#and divides the first number from the second number.
#While handling the ZeroDivisionError.

num1 = (input("Please enter a numerator: "))
num2 = (input("Please enter a denominator: "))

try:
    if (num1 == 0) or (num2 == 0):
        raise ZeroDivisionError("You cannot divide by zero!")
    else:
        div = num1 / num2
        print(f"{num1} divided by {num2} is {div}")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except Exception:
    print("Sorry. Please enter a valid whole number")
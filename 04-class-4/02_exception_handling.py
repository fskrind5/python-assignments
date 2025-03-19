# ======================
# 1. Exception Handling
# ======================
# Exceptions are errors that occur during program execution. Python provides a mechanism to handle them.

# 1. Common Exception Types
# ZeroDivisionError	Division by zero.
# TypeError	Invalid operation between incompatible types.
# ValueError	Function receives an argument of the wrong type.
# IndexError	Accessing an invalid index in a list.
# KeyError	Accessing a non-existing key in a dictionary.

# 🔹 Example of Try-Except Block
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Output: Cannot divide by zero!

# 🔹 Handling Multiple Exceptions
try:
    num = int("abc")  # Causes ValueError
except (ZeroDivisionError, ValueError) as e:
    print("Error:", e)

# 🔹 Finally Block (Always Executes)
try:
    f = open("test.txt", "r")
finally:
    f.close()  # Ensures file is closed

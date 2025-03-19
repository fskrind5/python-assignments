# Lesson 08: Control Modules & Functions
# Functions and modules in Python help organize and reuse code efficiently.

# =============
# 1. Functions
# =============

# A function is a block of reusable code that performs a specific task.

# A. Types of Functions
#1. Built-in Functions == Predefined functions like print(), len(), max().

#2. User-defined Functions == Created using def keyword.

#3. Lambda Functions ==	Anonymous one-liner functions using lambda.

#4. Recursive Functions == Functions that call themselves.

# 🔹 Example of a User-defined Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# 🔹 Example of a Lambda Function
square = lambda x: x * x
print(square(5))  # Output: 25

# 🔹 Example of a Recursive Function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# =============
# 2. Modules
# =============

# A module is a file containing Python code (functions, variables, classes) that can be imported into other programs.

# 🔹 Example of Importing a Module
import math
print(math.sqrt(25))  # Output: 5.0

# 🔹 Creating and Importing a Custom Module my_module.py
def add(a, b):
    return a + b

# main.py
import my_module
print(my_module.add(5, 3))  # Output: 8
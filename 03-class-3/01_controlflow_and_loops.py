# ========================
# 1. Control Flow & Loops
# ========================
# Control flow and loops help in decision-making and repeating tasks in Python.

#A. Conditional Statements (if-elif-else)
#Used for decision-making based on conditions.

x = 10

if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")

# B. Loops (for, while, break, continue)
# Loops are used to iterate over sequences or repeat code.

#🔹 For Loop Example (Iterating Over a List)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 🔹 While Loop Example (Repeating Until a Condition is False)
count = 5
while count > 0:
    print(count)
    count -= 1

# 🔹 Break Example (Stops Loop When a Condition is Met)
for num in range(1, 6):
    if num == 3:
        break
    print(num)  # Output: 1, 2

# 🔹 Continue Example (Skips a Specific Iteration)
for num in range(1, 6):
    if num == 3:
        continue
    print(num)  # Output: 1, 2, 4, 5 (skips 3)

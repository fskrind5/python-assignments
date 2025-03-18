# ========================
# 1. Arithmetic Operators
# ========================
# These operators are used to perform mathematical operations.
a, b = 10, 3

# Addition (+)
print("Addition:", a + b)  
print("Addition:", 15 + 5)

# Subtraction (-)
print("Subtraction:", a - b)
print("Subtraction:", 20 - 7)

# Multiplication (*)
print("Multiplication:", a * b)
print("Multiplication:", 6 * 4)

# Division (/)
print("Division:", a / b)  
print("Division:", 10 / 2)

# Floor Division (//)
print("Floor Division:", a // b)  
print("Floor Division:", 17 // 5)

# Modulus (%)
print("Modulus:", a % b)  
print("Modulus:", 29 % 6)

# Exponentiation (**)
print("Exponentiation:", a ** b)  
print("Exponentiation:", 2 ** 4)


# ========================
# 2. Assignment Operators
# ========================
# These operators are used to assign values to variables.
x = 5
y = 10

# Assign (=)
x = 10  
print("Assign:", x)

# Add and Assign (+=)
x += 5  
print("Add and Assign:", x)

# Subtract and Assign (-=)
y -= 3  
print("Subtract and Assign:", y)

# Multiply and Assign (*=)
x *= 2  
print("Multiply and Assign:", x)

# Divide and Assign (/=)
y /= 2  
print("Divide and Assign:", y)

# Floor Divide and Assign (//=)
x //= 3  
print("Floor Divide and Assign:", x)

# Modulus and Assign (%=)
y %= 4  
print("Modulus and Assign:", y)

# Exponentiate and Assign (**=)
x **= 2  
print("Exponentiate and Assign:", x)


# ========================
# 3. Comparison Operators
# ========================
# These operators compare values and return True or False.
a, b = 15, 10

# Equal to (==)
print("Equal to:", a == b)  
print("Equal to:", 5 == 5)

# Not Equal (!=)
print("Not Equal:", a != b)  
print("Not Equal:", 7 != 3)

# Greater than (>)
print("Greater than:", a > b)  
print("Greater than:", 12 > 8)

# Less than (<)
print("Less than:", a < b)  
print("Less than:", 5 < 9)

# Greater than or Equal to (>=)
print("Greater than or Equal to:", a >= b)  
print("Greater than or Equal to:", 10 >= 10)

# Less than or Equal to (<=)
print("Less than or Equal to:", a <= b)  
print("Less than or Equal to:", 6 <= 8)


# ========================
# 4. Logical Operators
# ========================
# Used to combine conditional statements.
p, q = True, False

# Logical AND (and)
print("Logical AND:", p and q)  
print("Logical AND:", True and True)

# Logical OR (or)
print("Logical OR:", p or q)  
print("Logical OR:", False or True)

# Logical NOT (not)
print("Logical NOT:", not p)  
print("Logical NOT:", not False)


# ========================
# 5. Identity Operators
# ========================
# These check if two objects refer to the same memory location.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Is (is)
print("Is list1 identical to list2?", list1 is list2)  
print("Is list1 identical to list3?", list1 is list3)

# Is Not (is not)
print("Is list1 not identical to list2?", list1 is not list2)  
print("Is list1 not identical to list3?", list1 is not list3)


# ========================
# 6. Membership Operators
# ========================
# These check if a value exists in a sequence (string, list, tuple, etc.).
text = "Hello World"
numbers = [1, 2, 3, 4, 5]

# In (in)
print("'H' in text:", 'H' in text)  
print("3 in numbers:", 3 in numbers)

# Not In (not in)
print("'Z' not in text:", 'Z' not in text)  
print("10 not in numbers:", 10 not in numbers)


# ========================
# 7. Bitwise Operators
# ========================
# These work on binary numbers (bitwise operations).
p, q = 5, 3  # 5 = 0101, 3 = 0011

# Bitwise AND (&)
print("Bitwise AND:", p & q)  
print("Bitwise AND:", 6 & 2)

# Bitwise OR (|)
print("Bitwise OR:", p | q)  
print("Bitwise OR:", 4 | 1)

# Bitwise XOR (^)
print("Bitwise XOR:", p ^ q)  
print("Bitwise XOR:", 7 ^ 2)

# Bitwise NOT (~)
print("Bitwise NOT:", ~p)  
print("Bitwise NOT:", ~q)

# Bitwise Left Shift (<<)
print("Bitwise Left Shift:", p << 2)  
print("Bitwise Left Shift:", q << 1)

# Bitwise Right Shift (>>)
print("Bitwise Right Shift:", p >> 1)  
print("Bitwise Right Shift:", q >> 2)

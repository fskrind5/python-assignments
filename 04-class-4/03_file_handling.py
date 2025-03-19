# ======================
# 1. File Handling
# ======================
# File handling allows reading from and writing to files in Python.

# 1. Opening and Closing a File

# "r"	Read mode (default).
# "w"	Write mode (creates file if not exists).
# "a"	Append mode (adds data to file).
# "x"	Exclusive mode (fails if file exists).

# 🔹 Example of Writing to a File
with open("example.txt", "w") as f:
    f.write("Hello, Python!")

# 🔹 Example of Reading from a File
with open("example.txt", "r") as f:
    content = f.read()
    print(content)  # Output: Hello, Python!

# 🔹 Appending to a File
with open("example.txt", "a") as f:
    f.write("\nAppending new text!")
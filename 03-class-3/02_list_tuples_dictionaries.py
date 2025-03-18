# ==============================
# 2. Lists, Tuples & Dictionary
# ==============================

#These are important data structures in Python.

#A. Lists (Mutable, Ordered Collection)
#Lists can store multiple values and can be modified.

# append()	Adds an element to the list.
# remove()	Removes a specific element.
# pop()	Removes the last element.
# sort()	Sorts the list.
# reverse()	Reverses the list.

# 🔹 List Example
numbers = [10, 20, 30]
numbers.append(40)
numbers.remove(20)
print(numbers)  # Output: [10, 30, 40]


#B. Tuples (Immutable, Ordered Collection)
# Tuples are like lists but cannot be changed after creation.

# count()	Counts occurrences of a value.
# index()	Returns the index of a value.

# 🔹 Tuples Example
fruits = ("apple", "banana", "cherry")
print(fruits[1])  # Output: banana


# C. Dictionary (Key-Value Pairs)
# Dictionaries store data in key-value pairs.

# Operation	Description
# keys()	Returns a list of keys.
# values()	Returns a list of values.
# items()	Returns key-value pairs.
# get()	Gets a value by key.
# update()	Updates dictionary with new key-value pairs.

# 🔹 Dictionary Example

person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice

person["age"] = 26  # Updating a value
person["city"] = "New York"  # Adding a new key-value pair

print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

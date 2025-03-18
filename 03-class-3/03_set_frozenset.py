# =======================
# 3. The Set & Frozenset
# =======================

# A set is an unordered collection of unique elements, while a frozenset is an immutable version of a set.

# A. Set (Mutable, Unordered Collection)
# Operation	Description
# add()	Adds an element.
# remove()	Removes an element.
# discard()	Removes an element without an error.
# union()	Combines sets.
# intersection()	Finds common elements.

# 🔹 Set Example

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.add(4)
print(set1)  # Output: {1, 2, 3, 4}

print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # Output: {3, 4}


# B. Frozenset (Immutable Version of a Set)
# A frozenset does not allow modifications.

# 🔹 Frozenset Example

frozen = frozenset([1, 2, 3, 4])
print(frozen)  # Output: frozenset({1, 2, 3, 4})

# A tuple is immutable, meaning its elements cannot be changed after creation.
my_tuple = (10, "Amit", 25.5, True, "Python", 10)

# 1. Display elements and data types
print("Elements and their data types:")

for item in my_tuple:
    print(item, type(item))

# 2. Indexing
print("\nElement at index 0:", my_tuple[0])
print("Element at index 1:", my_tuple[1])

# Slicing
print("Elements from index 1 to 3:", my_tuple[1:4])

# 3. Length
print("\nLength of tuple:", len(my_tuple))

# 4. Count occurrence
print("10 occurs:", my_tuple.count(10), "times")

# 5. Find index
print("Index of Python:", my_tuple.index("Python"))
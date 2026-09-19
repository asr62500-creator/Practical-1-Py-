my_list = [10, "Amit", 25.5, True, "Python"]

# 1. Display elements and their data types
print("Elements and their data types:")

for item in my_list:
    print(item, type(item))

# 2. Find length
print("\nLength of list:", len(my_list))

# 3. Indexing
print("\nElement at index 0:", my_list[0])
print("Element at index 1:", my_list[1])

# Slicing
print("Elements from index 1 to 3:", my_list[1:4])

# 4. Add an element
my_list.append("MCA")
print("\nAfter adding:", my_list)

# Update an element
my_list[0] = 100
print("After updating:", my_list)

# Remove an element
my_list.remove(25.5)
print("After removing:", my_list)
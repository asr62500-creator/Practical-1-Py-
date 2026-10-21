# Create and display a tuple
t = (10, 20, 30, 20, 40, 50)
print("Tuple:", t)

# Access elements using indexing
print("First element:", t[0])
print("Last element:", t[-1])

# Search for an element
x = int(input("Enter element to search: "))
if x in t:
    print(x, "is present in tuple")
else:
    print(x, "is not present in tuple")

# Slicing
print("Elements from index 1 to 3:", t[1:4])
print("First three elements:", t[:3])
print("Tuple in reverse:", t[::-1])

# Length and count
print("Length:", len(t))
print("Count of 20:", t.count(20))

# Find position using index()
x = int(input("Enter element to find its position: "))
if x in t:
    print("Index:", t.index(x))
else:
    print("Element not found")

# Maximum, minimum and sum
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Sum:", sum(t))

# Convert tuple to list and list to tuple
lst = list(t)
print("Tuple converted to list:", lst)

new_tuple = tuple(lst)
print("List converted to tuple:", new_tuple)
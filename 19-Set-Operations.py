# Create two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

# Basic operations
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A-B:", A - B)
print("Difference B-A:", B - A)
print("Symmetric Difference:", A ^ B)

# Subset, superset and membership
print("A is subset of B:", A.issubset(B))
print("A is superset of B:", A.issuperset(B))
print("3 belongs to A:", 3 in A)
print("10 belongs to A:", 10 in A)

# Add and remove elements
A.add(7)
print("After adding 7:", A)

A.discard(2)  # Does not raise an error if 2 is absent
print("After removing 2:", A)
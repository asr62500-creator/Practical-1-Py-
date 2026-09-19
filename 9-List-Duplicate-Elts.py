list1 = [10, 20, 30, 20, 40, 10]

# Create set
set1 = set(list1)

print("Set after removing duplicates:", set1)

# Add an element
set1.add(50)

print("After adding 50:", set1)

# Remove an element
set1.remove(20)

print("After removing 20:", set1)

# Another set
set2 = {30, 40, 50, 60, 70}

# Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference:", set1.difference(set2))
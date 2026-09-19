# A frozenset is an immutable version of a set.
# Once created, elements cannot be added or removed.
set1 = frozenset([10, 20, 30, 40])
set2 = {30, 40, 50, 60}

# Display sets
print("Frozen set:", set1)
print("Another set:", set2)

# Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference:", set1.difference(set2))
students = {
    "Amit": 95,
    "Suman": 80,
    "Neha": 82,
    "Priya": 88
}

# 1. Display all keys and values
print("Student names and marks:")

for name, marks in students.items():
    print(name, ":", marks)

# 2. Add a new key-value pair
students["Rohit"] = 80

print("\nAfter adding Rohit:")
print(students)

# 3. Update an existing value
students["Suman"] = 89

print("\nAfter updating Suman's marks:")
print(students)

# 4. Delete a key-value pair
del students["Rohit"]

print("\nAfter deleting Rohit:")
print(students)

# 5. Find student with highest marks
highest_name = ""
highest_marks = 0

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_name = name

print("\nStudent with highest marks:", highest_name)
print("Highest marks:", highest_marks)

# 6. Calculate average marks
total = 0

for marks in students.values():
    total = total + marks

average = total / len(students)

print("Average marks:", average)
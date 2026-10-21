# Dictionary containing student names and marks
students = {
    "Amit": 85,
    "Rahul": 72,
    "Priya": 92,
    "Neha": 68
}

# Display all students and their marks
print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

# Calculate average marks
average = sum(students.values()) / len(students)
print("Average Marks:", average)

# Find student with highest and lowest marks
highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print("Highest Marks:", highest, "-", students[highest])
print("Lowest Marks:", lowest, "-", students[lowest])
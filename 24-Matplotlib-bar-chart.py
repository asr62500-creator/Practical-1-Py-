import matplotlib.pyplot as plt

# Student names and their marks
names = ["Amit", "Rahul", "Priya", "Neha"]
marks = [85, 72, 92, 68]

# Create a bar chart
plt.bar(names, marks)

# Add title and axis labels
plt.title("Students' Marks")
plt.xlabel("Student Names")
plt.ylabel("Marks")

# Display the graph
plt.show()
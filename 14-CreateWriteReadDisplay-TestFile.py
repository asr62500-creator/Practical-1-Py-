# Create a file and write data into it
with open("student.txt", "w") as file:
    file.write("Name: Amit\n")
    file.write("Course: MCA\n")
    file.write("Semester: 3\n")

# Read and display the file contents
with open("student.txt", "r") as file:
    data = file.read()

print("File Contents:")
print(data)
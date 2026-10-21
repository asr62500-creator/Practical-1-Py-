import pandas as pd

# Create a dictionary of student data
data = {
    "Name": ["Amit", "Rahul", "Priya", "Neha"],
    "Age": [22, 23, 21, 22],
    "Marks": [85, 72, 92, 68]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display all data
print("Student Data:")
print(df)

# Select a single column
print("\nStudent Names:")
print(df["Name"])

# Select multiple columns
print("\nNames and Marks:")
print(df[["Name", "Marks"]])

# Calculate average marks
average = df["Marks"].mean()
print("\nAverage Marks:", average)

# Find the student with the highest marks
highest = df.loc[df["Marks"].idxmax()]
print("\nHighest Marks:")
print(highest)

# Find the student with the lowest marks
lowest = df.loc[df["Marks"].idxmin()]
print("\nLowest Marks:")
print(lowest)
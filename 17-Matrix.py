# Input matrix dimensions
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter elements of Matrix A:")
A = []
for i in range(r):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter elements of Matrix B:")
B = []
for i in range(r):
    row = list(map(int, input().split()))
    B.append(row)

# Matrix addition
addition = [[A[i][j] + B[i][j] for j in range(c)]
            for i in range(r)]

# Matrix subtraction
subtraction = [[A[i][j] - B[i][j] for j in range(c)]
               for i in range(r)]

print("Addition:")
for row in addition:
    print(row)

print("Subtraction:")
for row in subtraction:
    print(row)

# Matrix multiplication: A is r x c, B must be c x k
k = int(input("Enter number of columns for Matrix C (B's columns): "))

print("Enter elements of Matrix C (", c, "rows):")
C = []
for i in range(c):
    row = list(map(int, input().split()))
    C.append(row)

# Multiply A (r x c) by C (c x k)
multiplication = [[0 for j in range(k)] for i in range(r)]

for i in range(r):
    for j in range(k):
        for m in range(c):
            multiplication[i][j] += A[i][m] * C[m][j]

print("Multiplication:")
for row in multiplication:
    print(row)
n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Even Fibonacci terms:")

for i in range(n):
    if a % 2 == 0:
        print(a, end=" ")

    c = a + b
    a = b
    b = c
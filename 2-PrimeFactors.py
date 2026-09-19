n = int(input("Enter a number: "))

print("Prime factors:")

i = 2

while n > 1:
    if n % i == 0:
        print(i, end=" ")
        n = n // i
    else:
        i = i + 1
# Generate squares of numbers from 1 to 10
squares = [x ** 2 for x in range(1, 11)]
print("Squares:", squares)

# Generate even numbers from 1 to 20
even = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers:", even)

# Generate odd numbers from 1 to 20
odd = [x for x in range(1, 21) if x % 2 != 0]
print("Odd numbers:", odd)

# Generate numbers divisible by 3
numbers = [x for x in range(1, 31) if x % 3 == 0]
print("Numbers divisible by 3:", numbers)
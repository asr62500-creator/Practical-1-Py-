text = input("Enter a string: ")

# Reverse the string
reverse = text[::-1]

print("Reversed string:", reverse)

# Count vowels
count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Number of vowels:", count)

# Check palindrome
if text == reverse:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
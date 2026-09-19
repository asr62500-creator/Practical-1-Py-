text = input("Enter a string: ")

result = ""

for ch in text:
    if ch.isalnum() or ch == " ":   # if ch.isalnum() or ch == " ": isalnum() 
                                    # \\checks whether a character is:Alphabet or Number
        result = result + ch

print("String without punctuation:", result)
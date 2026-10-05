# Ask the user to enter a word.
word = input("Enter a word: ")

# Display the number of characters in the word.
print(f"Length: {len(word)}")

# Display the word using uppercase letters.
print(f"Uppercase: {word.upper()}")

# Repeat the word three times with spaces between each repetition.
repeated_word = (word + " ") * 3
print(f"Repeated three times: {repeated_word.strip()}")
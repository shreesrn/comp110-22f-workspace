"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730616899"

word: str = input("Enter a 5-character word. ")
if len(word) != 5: 
    exit("Error Word must contain 5 characters")

character: str = input("Enter a single character. ")
if len(character) != 1:
    exit("Error: Character must be a single character")

count: int = 0

print("Enter a 5-character word: " + word)
print("Enter a single character: " + character)
print("Searching for " + character + " in " + word)

if word[0] == character:
    print (character + " found at index 0.")
    count = count + 1
if word[1] == character:
    print (character + " found at index 1.")
    count = count + 1
if word[2] == character:
    print (character + " found at index 2.")
    count = count + 1
if word[3] == character:
    print (character + " found at index 3.")
    count = count + 1
if word[4] == character:
    print (character + " found at index 4.")
    count = count + 1

if count == 0: 
    print("No instances of " + character + " found in " + word)
elif count == 1:
    print("1 instance of " + character + " found in " + word)
else: 
    print(str(count) + " instances of " + character + " found in " + word)

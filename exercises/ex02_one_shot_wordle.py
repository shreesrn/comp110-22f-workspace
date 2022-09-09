"""One shot wordle assignment"""

__author__ = "730616899"

"""declaring some variables"""

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
box_color: str = ""

"""determining is input word is the correct number of characters"""

while len(guess) != len(secret):
    guess: str = input(f"That was not {len(secret)} letters! Try again: ")

"""Beginning to test for Green/Yellow/White boxes"""

while index < len(secret):
    if guess[index] == secret[index]:
        box_color = box_color + GREEN_BOX
    else:
        yellow_letter: bool = "False"
        yellow_tracker: int = 0
        while yellow_letter != "True" and yellow_tracker < len(secret):
            if guess[index] == secret[yellow_tracker]:
                yellow_letter = "True"
            else:
                yellow_tracker +=1
        if yellow_letter == "True":
            box_color = box_color + YELLOW_BOX
        else:
            box_color = box_color + WHITE_BOX
    index = index + 1
print(box_color)

"""Printing the congratulatory or "try again" messege"""

if guess == secret:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")

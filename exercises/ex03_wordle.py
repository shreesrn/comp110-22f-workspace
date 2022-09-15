"""Wordle assignment."""

__author__ = "730616899"

"""variables"""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

"""contains_char function"""

def contains_char(word: str, char: str) -> bool:
    assert len(char) ==1
    """check if a character is in a word."""
    yellow = False
    count: int = 0
    while count < len(word):
        if char == word[count]:
            yellow = True
            return yellow
        else:
            count += 1
    return yellow


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    """create boxes of green/yellow/white emojis to show how clase the guess is to the secret"""
    boxes: str = ""
    counter: int = 0
    while counter < len(secret):
        if guess[counter] == secret[counter]:
            boxes = boxes + GREEN_BOX
        elif contains_char(secret, guess[counter]) == True:
            boxes = boxes + YELLOW_BOX
        else: 
            boxes = boxes + WHITE_BOX
        counter +=1
    return boxes


def input_guess(expected: int) -> str:
    """makes sure guess is of correct characters"""
    guessed: str = input(f"what is your {expected}-letter guess? ")
    while len(guessed) != expected:
        guessed = input(f"That wasn't {expected} letters! Try again: ")
    return guessed

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    status: str = "loss"
    answer: str = "codes"
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(answer))
        print(emojified(guess, answer))
        if guess == answer:
            print(f"You won in {turn} turns!")
            return
        else:
            turn +=1
    print("X/6 - Sorry, try again tommorow!")
       
if __name__ == "__main__":
    main()
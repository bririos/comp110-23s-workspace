"""One shot at wordle."""

__author__ ="730576067"

SECRET: str = "python"
length_guess=(len(guess)-1)
length_secret=(len(SECRET)-1)
playing: bool = True 
i=0
j=0
empty_string=""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while length_guess!=length_secret:
    guess= input("That was not 6 letters! Try again: ")

while i < length_secret:


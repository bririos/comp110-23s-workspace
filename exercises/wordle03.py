"""One shot at wordle."""

__author__ ="730576067"

guess: str =str (input("What is your 6-letter guess? "))
SECRET: str = "python"
length_guess=(len(guess)-1)
length_secret=(len(SECRET)-1)
playing: bool = True 
guess_idx= guess[""]




while length_guess!=length_secret:
    guess= input("That was not 6 letters! Try again: ") 
    #nested while loop for nextr part
    while length_guess< length_secret:

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    
else:
    if length_guess<length_secret:
        input("That was not 6 letters! Try again: ") 
        print("Not quite. Play again soon! ")

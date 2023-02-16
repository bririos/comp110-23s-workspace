"""One shot at wordle."""

__author__ ="730576067"

SECRET: str = "python"
guess: str = ( input("What is your 6-letter guess? "))
length=(len(guess)-1)
playing: bool = True 
guess_idx: int=0
word = len(SECRET)
play: bool = True


while playing:
    if guess == SECRET:
        print("Woo! You got it")
        playing = False
    else:
        if length<4 or length>6:
            input("That was not 6 letters! Try again: ")
        else:
            if length ==5:
                print("Not quite. Play again soon! ")


                          
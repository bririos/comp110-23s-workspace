"""One shot at wordle."""

__author__ ="730576067"

guess: str = input("What is your 6-letter guess? ")
SECRET: str = "python"
length_guess: int = len(guess)
length_secret: int = len(SECRET) 
playing: bool = False 
i: int = 0
j: int = 0
empty_string: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
while length_guess != length_secret:
    guess = input("That was not 6 letters! Try again: ")

while i < length_secret:
    if guess[i]==SECRET[i]:
        empty_string += GREEN_BOX
    else:
        j = 0
        playing = False
        while playing is not True and j < length_secret:
            if SECRET[j]==guess[i]:
                playing= True 
            else:
                j+= 1
        if playing is True:
            empty_string += YELLOW_BOX
        else:
            empty_string+=WHITE_BOX
    i += 1
print("Not quite. Play again soon!")
print(empty_string)

if guess == SECRET:
    print("Woo! You got it!")

    


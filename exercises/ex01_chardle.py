"""EX01 - Chardle - A cute step toward Wardle."""

___author__ = "730576067"
wordle: str = input("Enter a 5-character word: ")
character: str = input("Enter a single character: ") 
search: str = input ("Searching for "+ character + " in "+ wordle )

if (wordle [0] == character):
    print(character + " found at index 0")
if (wordle [1] == character):
    print(character + " found at index 1")
if (wordle [2] == character):
    print(character + " found at index 2")
if (wordle [3] == character):
    print(character + " found at index 3")
if (wordle [4] == character):
    print(character + " found at index 4")
counter = 0
for c in wordle:
    if c== character:
        counter += 1
print(counter, "instances of " + character+ " found in " + wordle)

"""Demostrates how to count something."""

number_string: str = "321"
number_of_odds: int = 0

#if a number % 2 == 1, then it is odd
if (int(number_string[0]) % 2 == 1):
    number_of_odds = number_of_odds +1

if (int(number_string[1]) % 2 == 1):
    number_of_odds = number_of_odds +1

if (int(number_string[2]) % 2 == 1):
    number_of_odds = number_of_odds +1

print("You have  " + str(number_of_odds) + " odds in the string!")



print(wordle[1]) == 1

print(wordle[2]) == 2

print(wordle[3]) == 3

print(wordle[4]) == 4

print(wordle[5]) == 5
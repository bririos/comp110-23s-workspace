def mimic(my_words:str, letter_idx:int)-> str
    """Given the string my_words, outputs the same string."""


    if letter_idx>= len(my_words):
        print("Index too high")
    return my_words[letter_idx]

mimic("Hello!")

print(mimic("Hello!"))

my_words:str="Hello!"
response:str=mimic(my_words)
print(response)
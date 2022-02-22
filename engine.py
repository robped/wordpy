
def ask_next_word():
    next_word = ""
    while len(next_word) != 5:
        next_word = input("insert a new word: ")
        if len(next_word) != 5:
            print("Insert a word with 5 letters!")
 
    return next_word.upper()
 
def green(letter):
    return f'\033[92m{letter}\033[0m'
 
def yellow(letter):
    return f'\033[93m{letter}\033[0m'
 
def gray(letter):
     return f'\033[90m{letter}\033[0m'

 
def check_word(magic_word, new_word):
    checked_word = []
    for index, letter in enumerate(new_word):
        if letter in magic_word:
            if letter == magic_word[index]:
                checked_word.append(green(letter))
            else:
                 checked_word.append(yellow(letter))
        else:
            checked_word.append(gray(letter))
    return checked_word 
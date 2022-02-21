# TODO - at some point add funcionality to chose the length of the words
#       creating a new word db at runtime

import random
import table
import db_utility

def ask_next_word():
    next_word = ""
    while len(next_word) != 5:
        next_word = input("insert a new word: ")
        if len(next_word) != 5:
            print("Insert a word with 5 letters!")

    return next_word


if __name__ == '__main__':
    table = table.Table()
    current_row = 0
    magic_word = db_utility.get_random_word('all_the_words.txt')
    print(magic_word)
    while current_row < 5:
        table.show_table()
        next_word = ask_next_word()
        table.insert_word(next_word, current_row)
        current_row += 1
    print("\nWell Done!\n")

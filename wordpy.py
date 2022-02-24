# TODO - at some point add funcionality to chose the length of the words
#       creating a new word db at runtime

import random
import table
import db_utility
import engine

if __name__ == '__main__':
    table = table.Table()
    current_row = 0
    #magic_word = db_utility.get_random_word('all_the_words.txt').upper()
    words_list = db_utility.get_words_of_len('all_the_words.txt', 5)
    magic_word =  random.choice(words_list).upper()
    next_word = ""
    #print(magic_word)
    while current_row < 5:
        table.show_table()
        next_word = engine.ask_next_word(words_list)
        checked_word = engine.check_word(magic_word, next_word)
        table.insert_word(checked_word, current_row)
        current_row += 1
    table.show_table()
    if next_word == magic_word:
        print("\nWell Done!\n")
    else:
        print("\nGame Over!\nThe word was "+ magic_word +", Try Again!")


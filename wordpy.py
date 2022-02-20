import random
import utility
import table


if __name__ == '__main__':
    table = table.Table()
    table.show_table()
    table.insert_word("WORDE", 0)
    table.insert_word("WORDE", 1)
    table.insert_word("worde", 2)
    table.insert_word("worde", 3)
    table.show_table()

    next_word = input("inset a new word: ")
    table.insert_word(next_word, 2)
    
    table.make_letter_green(0, 0)
    table.make_letter_yellow(0, 1)
    table.make_letter_grey(0, 2)
    table.show_table()
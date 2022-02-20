import os
import random

def get_words(file_name):
    with open(file_name) as words_file:
        words = [w.lower() for w in words_file.read().split() if w.isalpha() and len(w)>1]
    
    return words

def get_words_of_len(file_name, length):
    with open(file_name) as words_file:
        words = [w.lower() for w in words_file.read().split() if w.isalpha() and len(w) == length]
    
    return words

def append_to_file(file_name, words):
    with open(file_name, 'a') as all_words:
        all_words.write(words)

def get_files(directory):
    file_list = []

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            file_list.append(f)
    
    return file_list

#main funcionality -> create text file with all the words
if __name__ == '__main__':
    
    file_list = get_files('db')
    for file_name in file_list:
        words_list = get_words_of_len(file_name, 5)
        for word in words_list:
            append_to_file('all_the_words.txt', word + "\n")

   
   
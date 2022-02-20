class Table():
    def __init__(self):
        self.table = [['-','-','-','-','-'] for i in range(5)]
        
    def show_table(self):
        print("_______________\n")
        for row in self.table:
            line = "   "
            for letter in row:
                line += f'{letter} '
            print(line)
        print("_______________")
    
    def insert_word(self, word, row):
        word = word.upper()
        for i in range(len(self.table[row])):
            self.table[row][i] = word[i]
    
    # green letter - right letter and right position
    def make_letter_green(self, row, column):
        self.table[row][column] = f'\033[92m{self.table[row][column]}\033[0m'

    # yellow letter - right letter but wrong position
    def make_letter_yellow(self, row, column):
        self.table[row][column] = f'\033[93m{self.table[row][column]}\033[0m'

    # gray letter - wrong letter
    def make_letter_grey(self, row, column):
        self.table[row][column] = f'\033[90m{self.table[row][column]}\033[0m'

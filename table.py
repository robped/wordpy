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
        self.table[row] = word

    # def insert_word(self, word, row):
    #     word = word.upper()
    #     for i in range(len(self.table[row])):
    #         self.table[row][i] = word[i]

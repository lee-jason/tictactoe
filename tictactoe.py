class Tic_Tac_Toe:
    def __init__ (self):
        self.board = ['1','2','3','4','5','6','7','8','9']
        self.options = ['1','2','3','4','5','6','7','8','9']
        self.num_of_turns = 0 


    def display_board(self):
        print(self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print("------------")
        print(self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print("------------")
        print(self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def play_game(self): #There must be two players
        self.display_board()
        while (self.winner() is not True):
            self.turns('X')
            if self.winner() is True:
                break
            self.turns('O')
            self.winner()
            
    def turns(self,player_symbol):
        print('\\n\\n\\n')
        print("It's " + player_symbol + "'s turn" )
        position = input('Pick a number displayed on the board ')

        if (position not in self.options):
            print('')
            print('Error, number not an option try again')
            self.display_board()
            self.turns(player_symbol)
        else:
            self.options.remove(position)
            self.board[int(position)-1] = player_symbol
            self.num_of_turns += 1
            self.display_board()
            if self.num_of_turns == 9:
                self.winner()
                print( 'TIE! Rematch?')
                return

    def winner(self):
        if self.col_win():
            return True
        if self.row_win():
            return True
        if self.diag_win():
            return True
    
    def col_win(self):
        for i in range(3):
            if (self.board[i] == self.board[i+3] and self.board[i] == self.board[i+6]):
                print(self.board[i] + " WINS!")
                return True
        return False
            
    def row_win(self):
        for i in range(0,7,3):
            if (self.board[i] == self.board[i+1] and self.board[i] == self.board[i+2]):
                print(self.board[i] + " WINS!")
                return True
        return False
    
    def diag_win(self):
        if (self.board[0] == self.board[4] and self.board[4] == self.board[8]):
            print (self.board[4] + " WINS!")
            return True
        if (self.board[2] == self.board[4] and self.board[4] == self.board[6]):
            print(self.board[4] + " WINS!")
            return True
        return False  "

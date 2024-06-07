import time

start_time = time.time()

import math 

class TicTacToe: 
    def _init_(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player1_char = 'O'
        self.player_char = 'X'
        self.current_player = self.player_char

    def play(self):
        while not self.is_game_over():
            self.print_board()
            if self.current_player == self.player_char:
                row, col = self.get_player_move()
            else:
                row, col = self.get_player_move()  # This should call AI move function
            self.make_move(row, col)
            self.current_player = self.get_next_player()
        
        self.print_board()
        winner = self.get_winner()
        if winner:
            print(f"Player {winner} wins!")
        else:
            print("It's a draw!")

    def get_player_move(self):
        valid_move = False
        while not valid_move:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if self.is_valid_move(row, col):
                    valid_move = True
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")
        return row, col

    def minimax(self, board, depth, is_maximizing):
        scores = {'X': -1, 'O': 1, 'draw': 0}
        if self.is_game_over():
            winner = self.get_winner()
            return scores[winner] if winner else scores['draw']

        if is_maximizing:
            best_score = -math.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = self.player1_char
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = ' '
                        best_score = max(score, best_score)
            return best_score 
        else:
            best_score = math.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = self.player_char
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = ' '
                        best_score = min(score, best_score)
            return best_score

    def is_valid_move(self, row, col):
        return self.board[row][col] == ' '

    def make_move(self, row, col):
        self.board[row][col] = self.current_player

    def is_game_over(self):
        return self.get_winner() is not None or self.is_board_full()

    def is_board_full(self):
        for row in range(3):            
            for col in range(3):
                if self.board[row][col] == ' ':
                    return False
        return True

    def get_winner(self):
        for char in [self.player_char, self.player1_char]:
            # Check rows and columns
            for i in range(3):
                if all([self.board[i][j] == char for j in range(3)]) or all([self.board[j][i] == char for j in range(3)]):
                    return char
            # Check diagonals
            if all([self.board[i][i] == char for i in range(3)]) or all([self.board[i][2-i] == char for i in range(3)]):
                return char
        return None

    def get_next_player(self):
        return self.player1_char if self.current_player == self.player_char else self.player_char

    def print_board(self):
        print("-------------")
        for row in self.board: 
            print("|", end=" ")
            for cell in row:
                print(cell, end=" ")
                print("|", end=" ")
            print("\n-------------")

# Main
game = TicTacToe()
game.play()

# Akhiri hitung waktu
end_time = time.time()

# Hitung waktu eksekusi
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

import tkinter as tk
from tkinter import ttk, messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"  # Human is X, computer is O
        self.board = [" " for _ in range(9)]
        self.game_over = False
        self.difficulty = "Easy"
        
        # Difficulty selection
        self.difficulty_frame = ttk.LabelFrame(root, text="Difficulty")
        self.difficulty_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="we")
        
        self.difficulty_var = tk.StringVar(value="Easy")
        ttk.Radiobutton(self.difficulty_frame, text="Easy", variable=self.difficulty_var, value="Easy").pack(side="left")
        ttk.Radiobutton(self.difficulty_frame, text="Medium", variable=self.difficulty_var, value="Medium").pack(side="left")
        ttk.Radiobutton(self.difficulty_frame, text="Hard", variable=self.difficulty_var, value="Hard").pack(side="left")
        
        # Create buttons for the board
        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text=" ", font=('Arial', 30), width=5, height=2,
                             command=lambda idx=i: self.on_click(idx))
            button.grid(row=i//3 + 1, column=i%3)
            self.buttons.append(button)
            
        # Add reset button
        reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        reset_button.grid(row=5, column=0, columnspan=3, sticky="we", padx=10, pady=10)
        
    def on_click(self, position):
        if self.game_over or self.board[position] != " ":
            return
            
        # Human player move
        self.make_move(position, self.current_player)
        
        if not self.check_winner() and " " in self.board:
            # Computer's turn
            self.computer_move()
            self.check_winner()
    
    def make_move(self, position, player):
        self.board[position] = player
        self.buttons[position].config(text=player, state=tk.DISABLED)
        
    def computer_move(self):
        self.difficulty = self.difficulty_var.get()
        
        if self.difficulty == "Easy":
            self.computer_move_random()
        elif self.difficulty == "Medium":
            self.computer_move_medium()
        else:  # Hard
            self.computer_move_hard()
    
    def computer_move_random(self):
        available_positions = [i for i, spot in enumerate(self.board) if spot == " "]
        if available_positions:
            computer_choice = random.choice(available_positions)
            self.make_move(computer_choice, "O")
    
    def computer_move_medium(self):
        # Check if computer can win
        move = self.find_winning_move("O")
        if move is not None:
            self.make_move(move, "O")
            return
            
        # Check if player can win and block
        move = self.find_winning_move("X")
        if move is not None:
            self.make_move(move, "O")
            return
            
        # Otherwise random
        self.computer_move_random()
    
    def computer_move_hard(self):
        best_score = -float('inf')
        best_move = None
        
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(self.board, False)
                self.board[i] = " "
                
                if score > best_score:
                    best_score = score
                    best_move = i
        
        if best_move is not None:
            self.make_move(best_move, "O")
    
    def minimax(self, board, is_maximizing):
        winner = self.check_winner_minimax(board)
        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        elif " " not in board:
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = self.minimax(board, False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score = self.minimax(board, True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score
    
    def find_winning_move(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        
        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == player and self.board[c] == " ":
                return c
            if self.board[a] == self.board[c] == player and self.board[b] == " ":
                return b
            if self.board[b] == self.board[c] == player and self.board[a] == " ":
                return a
        return None
    
    def check_winner(self):
        winner = self.check_winner_minimax(self.board)
        if winner:
            self.game_over = True
            for button in self.buttons:
                button.config(state=tk.DISABLED)
            if winner == "X":
                messagebox.showinfo("Game Over", "Winner: Player!")
            else:
                messagebox.showinfo("Game Over", "Defeat! Computer wins.")
            return True
        
        if " " not in self.board:
            self.game_over = True
            for button in self.buttons:
                button.config(state=tk.DISABLED)
            messagebox.showinfo("Game Over", "It's a tie!")
            return True
            
        return False
    
    def check_winner_minimax(self, board):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        
        for combo in winning_combinations:
            a, b, c = combo
            if board[a] == board[b] == board[c] != " ":
                return board[a]
        return None
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.game_over = False
        for button in self.buttons:
            button.config(text=" ", state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
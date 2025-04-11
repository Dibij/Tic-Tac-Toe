import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [' ' for _  in range (9)]
        self.game_over = False
        
        # Create buttons for the board
        self.buttons =[]
        for i in range(9):
            button = tk.Button(root, text=" ", font=('Arial', 30), width=2, height=2, command = lambda idx=i: self.on_click(idx))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
            
        # Add reset button
        reset_button = tk.Button(root, text='Reset', command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3, sticky='we')
    
    def on_click (self, position):
        if self.game_over or self.board[position] != " ":
            return
        
        self.make_move(position, self.current_player)
        
        if not self.check_winner() and " " in self.board:
            # Computer's turn (random move)
            self.current_player = "0" if self.current_player == "X" else "X"
            self.computer_move()
            self.check_winner()
    
    def make_move(self, position, player):
        self.board[position] = player
        self.buttons[position].config(text=player)
    
    def computer_move(self):
        available_positions = [i for i, spot in enumerate(self.board) if spot == " "]
        if available_positions:
            computer_choice = random.choice(available_positions)
            self.make_move(computer_choice, self.current_player)
            self.current_player = "0" if self.current_player == "X" else "X"
    
    def check_winner(self):
        # Check all possible wining conditions
        wining_combinations =[
            [0,1,2], [3,4,5],[6,7,8], # rows
            [0,3,6], [1,4,7], [2,5,8], # columns
            [0,4,8], [2,4,6] # diagonals
        ]
        
        for combo in wining_combinations:
            a, b ,c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                self.game_over = True
                winner = self.board[a]
                if winner == "X":
                    messagebox.showinfo("Game Over", "Winner: Player")
                else:
                    messagebox.showinfo("Game Over", "Defeat ! Computer wins.")
                return True
        
        if " " not in self.board:
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a Tie!")
            return True
        return False
    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.game_over = False
        for button in self.buttons:
            button.config(text=" ")
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
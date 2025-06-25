import tkinter as tk
from tkinter import messagebox

def is_winner(board, player):
    win_states = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for state in win_states:
        if all(board[i] == player for i in state):
            return True
    return False

def is_board_full(board):
    return all(spot != '' for spot in board)

def minimax(board, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = ''
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = ''
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    move = -1
    best_score = -float('inf')
    for i in range(9):
        if board[i] == '':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                move = i
    return move

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe with AI")
        self.board = [''] * 9
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            btn = tk.Button(self.root, text='', font=('Arial', 40), width=5, height=2,
                            command=lambda i=i: self.player_move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def player_move(self, index):
        if self.board[index] == '':
            self.board[index] = 'X'
            self.buttons[index].config(text='X', state='disabled')
            if self.check_winner('X'):
                messagebox.showinfo("Kết quả", "Bạn thắng! 🎉")
                self.disable_all()
            elif is_board_full(self.board):
                messagebox.showinfo("Kết quả", "Hòa rồi!")
                self.disable_all()
            else:
                self.root.after(500, self.ai_move)

    def ai_move(self):
        move = best_move(self.board)
        if move != -1:
            self.board[move] = 'O'
            self.buttons[move].config(text='O', state='disabled')
            if self.check_winner('O'):
                messagebox.showinfo("Kết quả", "AI thắng! 😢")
                self.disable_all()
            elif is_board_full(self.board):
                messagebox.showinfo("Kết quả", "Hòa rồi!")
                self.disable_all()

    def check_winner(self, player):
        return is_winner(self.board, player)

    def disable_all(self):
        for btn in self.buttons:
            btn.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

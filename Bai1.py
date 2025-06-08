import tkinter as tk
import tkinter.messagebox

root = tkinter.Tk()
root.title("Tic Tac Toe")
player = 'X'
interface = [[None for i in range(3)] for j in range(3)]
def click(i,j):
    global player
    btn = interface[i][j]
    if btn['text']== '':
        btn.config(text=player, fg='green' if player == 'X' else 'red')
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    winner = winner_check()
    if winner:
        if tkinter.messagebox.askyesno("Winner", f"Người chơi {winner} thắng\n Bạn có muốn chơi lại không ?"):
            reset_board()
        else:
            root.destroy()
       
        return  
    if draw():
        if tkinter.messagebox.askyesno("Hòa", "Hòa nhé !\nBạn có muốn chơi lại không ?"):
            reset_board()
        else:
            root.destroy()
        return

def reset_board():
    global player
    player = 'X'
    for i in range(3):
        for j in range(3):
            interface[i][j].config(text='')

for i in range(3):
    for j in range(3):
        interface[i][j] =tk.Button(root, text='', width= 50, height=5, font=('Arial', 12), activebackground= 'lightblue', background= 'beige', command=lambda i=i, j=j: click(i,j) )
        interface[i][j].grid(column=j, row=i)

def winner_check():
    lines = [];
    #kiem tra hang
    for i in range(3):
        lines.append([interface[i][j]['text'] for j in range(3)])
    #kiem tra cot    
    for j in range(3):
        lines.append([interface[i][j]['text'] for i in range(3)])
    #kiem tra 2 duong cheo
    lines.append([interface[i][i]['text'] for i in range(3)])  
    lines.append([interface[i][2-i]['text'] for i in range(3)])
    for line in lines:
        if line[0] != "" and all(cell == line[0] for cell in line):
            return line[0]
        
def draw():
    for i in range(3):
        for j in range(3):
            if interface[i][j]['text'] == '':
                return False
    return True

root.mainloop()



import tkinter as tk
import tkinter.messagebox

root = tkinter.Tk()
root.title("Tic Tac Toe")

nguoi_choi = 'X'
giaodien = [[None for i in range(3)] for j in range(3)]
def click(i,j):
    global nguoi_choi
    btn = giaodien[i][j]
    if btn['text']== '':
        btn.config(text=nguoi_choi)
        if nguoi_choi == 'X':
            nguoi_choi = 'O'
        else:
            nguoi_choi = 'X'

for i in range(3):
    for j in range(3):
        giaodien[i][j] =tk.Button(root, text=None, width= 50, height=5, command=lambda i=i, j=j: click(i,j) )
        giaodien[i][j].grid(column=i, row=j)






root.mainloop()


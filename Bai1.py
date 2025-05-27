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
    winner = winner_check()
    if winner:
        tkinter.messagebox.showinfo("Winner", f"Người chơi {winner} thắng")
    if draw():
        tkinter.messagebox.showinfo("Hòa", "Hòa nhé !")

for i in range(3):
    for j in range(3):
        giaodien[i][j] =tk.Button(root, text='', width= 50, height=5, command=lambda i=i, j=j: click(i,j) )
        giaodien[i][j].grid(column=j, row=i)

def winner_check():
    if giaodien[0][0]['text']==giaodien[0][1]['text']==giaodien[0][2]['text']!= '':
        return giaodien[0][0]['text']

    if giaodien[1][0]['text']==giaodien[1][1]['text']==giaodien[1][2]['text']!= '':
        return giaodien[1][0]['text']

    if giaodien[2][0]['text']==giaodien[2][1]['text']==giaodien[2][2]['text']!= '':
        return giaodien[2][0]['text']

    if giaodien[0][0]['text']==giaodien[1][0]['text']==giaodien[2][0]['text']!= '':
        return giaodien[0][0]['text']

    if giaodien[0][1]['text']==giaodien[1][1]['text']==giaodien[2][1]['text']!= '':
        return giaodien[0][1]['text']

    if giaodien[0][2]['text']==giaodien[1][2]['text']==giaodien[2][2]['text']!= '':
        return giaodien[0][2]['text']

    if giaodien[0][0]['text']==giaodien[1][1]['text']==giaodien[2][2]['text']!= '':
        return giaodien[0][0]['text']

    if giaodien[0][2]['text']==giaodien[1][1]['text']==giaodien[2][0]['text']!= '':
        return giaodien[0][2]['text']

def draw():
    for i in range(3):
        for j in range(3):
            if giaodien[i][j]['text'] == '':
                return False
    return True

root.mainloop()


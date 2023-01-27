import tkinter as tk
import random
import tkinter.messagebox as mb
window = tk.Tk()
window.geometry(f'+600+200')
window.title("Крестики-нолики")
move_game = [''] * 9

def first_check():
    my_list = [0, 2, 6, 8]
    my_list2 = [1, 3, 5, 7]
    global move_game
    if move_game[4] == 'X' or move_game[4] == 'O':
        try:
            a = random.choice(my_list)
            if move_game[a] == '':
                button[a].config(text='O', bg='white', state='disabled')
                move_game[a] = 'O'
            else:
                count = 0
                for i in range(len(my_list)):
                    if move_game[i] == '' and count == 0:
                        button[i].config(text='O', bg='white', state='disabled')
                        move_game[i] = 'O'
                        count += 1
        except:
            a = random.choice(my_list2)
            if move_game[a] == '':
                button[a].config(text='O', bg='white', state='disabled')
                move_game[a] = 'O'
            else:
                count = 0
                for i in range(len(my_list)):
                    if move_game[i] == ''and count == 0:
                        button[i].config(text='O', bg='white', state='disabled')
                        move_game[i] = 'O'
                        count += 1
    else:
        button[4].config(text='O', bg='white', state='disabled')
        move_game[4] = 'O'

def check_field_O(my_list):
    if ((my_list[0] == 'O' and my_list[1] == 'O') or (my_list[0] == 'X' and my_list[1] == 'X')) and my_list[2] == '':
        button[2].config(text='O', bg='white', state='disabled')
        my_list[2] = 'O'
    elif ((my_list[0] == 'O' and my_list[2] == 'O') or (my_list[0] == 'X' and my_list[2] == 'X')) and my_list[1] == '':
        button[1].config(text='O', bg='white', state='disabled') 
        my_list[1] = 'O'
    elif ((my_list[1] == 'O' and my_list[2] == 'O') or (my_list[1] == 'X' and my_list[2] == 'X')) and my_list[0] == '':
        button[0].config(text='O', bg='white', state='disabled') 
        my_list[0] = 'O'
    elif ((my_list[3] == 'O' and my_list[4] == 'O') or (my_list[3] == 'X' and my_list[4] == 'X')) and my_list[5] == '':
        button[5].config(text='O', bg='white', state='disabled') 
        my_list[5] = 'O'
    elif ((my_list[3] == 'O' and my_list[5] == 'O') or (my_list[3] == 'X' and my_list[5] == 'X')) and my_list[4] == '':
        button[4].config(text='O', bg='white', state='disabled') 
        my_list[4] = 'O'
    elif ((my_list[4] == 'O' and my_list[5] == 'O') or (my_list[4] == 'X' and my_list[5] == 'X')) and my_list[3] == '':
        button[3].config(text='O', bg='white', state='disabled') 
        my_list[3] = 'O'
    elif ((my_list[6] == 'O' and my_list[7] == 'O') or (my_list[6] == 'X' and my_list[7] == 'X')) and my_list[8] == '':
        button[8].config(text='O', bg='white', state='disabled') 
        my_list[8] = 'O'
    elif ((my_list[6] == 'O' and my_list[8] == 'O') or (my_list[6] == 'X' and my_list[8] == 'X')) and my_list[7] == '':
        button[7].config(text='O', bg='white', state='disabled') 
        my_list[7] = 'O'
    elif ((my_list[7] == 'O' and my_list[8] == 'O') or (my_list[7] == 'X' and my_list[8] == 'X')) and my_list[6] == '':
        button[6].config(text='O', bg='white', state='disabled') 
        my_list[6] = 'O'
    elif ((my_list[0] == 'O' and my_list[3] == 'O') or (my_list[0] == 'X' and my_list[3] == 'X')) and my_list[6] == '':
        button[6].config(text='O', bg='white', state='disabled') 
        my_list[6] = 'O'
    elif ((my_list[0] == 'O' and my_list[6] == 'O') or (my_list[0] == 'X' and my_list[6] == 'X')) and my_list[3] == '':
        button[3].config(text='O', bg='white', state='disabled') 
        my_list[3] = 'O'
    elif ((my_list[3] == 'O' and my_list[6] == 'O') or (my_list[3] == 'X' and my_list[6] == 'X')) and my_list[0] == '':
        button[0].config(text='O', bg='white', state='disabled') 
        my_list[0] = 'O'
    elif ((my_list[1] == 'O' and my_list[4] == 'O') or (my_list[1] == 'X' and my_list[4] == 'X')) and my_list[7] == '':
        button[7].config(text='O', bg='white', state='disabled') 
        my_list[7] = 'O'
    elif ((my_list[1] == 'O' and my_list[7] == 'O') or (my_list[1] == 'X' and my_list[7] == 'X')) and my_list[4] == '':
        button[4].config(text='O', bg='white', state='disabled') 
        my_list[4] = 'O'
    elif ((my_list[4] == 'O' and my_list[7] == 'O') or (my_list[4] == 'X' and my_list[7] == 'X')) and my_list[1] == '':
        button[1].config(text='O', bg='white', state='disabled') 
        my_list[1] = 'O'
    elif ((my_list[2] == 'O' and my_list[5] == 'O') or (my_list[2] == 'X' and my_list[5] == 'X')) and my_list[8] == '':
        button[8].config(text='O', bg='white', state='disabled') 
        my_list[8] = 'O'
    elif ((my_list[2] == 'O' and my_list[8] == 'O') or (my_list[2] == 'X' and my_list[8] == 'X')) and my_list[5] == '':
        button[5].config(text='O', bg='white', state='disabled') 
        my_list[5] = 'O'
    elif ((my_list[5] == 'O' and my_list[8] == 'O') or (my_list[5] == 'X' and my_list[8] == 'X')) and my_list[2] == '':
        button[2].config(text='O', bg='white', state='disabled') 
        my_list[2] = 'O'
    elif ((my_list[0] == 'O' and my_list[4] == 'O') or (my_list[0] == 'X' and my_list[4] == 'X')) and my_list[8] == '':
        button[8].config(text='O', bg='white', state='disabled') 
        my_list[8] = 'O'
    elif ((my_list[0] == 'O' and my_list[8] == 'O') or (my_list[0] == 'X' and my_list[8] == 'X')) and my_list[4] == '':
        button[4].config(text='O', bg='white', state='disabled') 
        my_list[4] = 'O'
    elif ((my_list[4] == 'O' and my_list[8] == 'O') or (my_list[4] == 'X' and my_list[8] == 'X')) and my_list[0] == '':
        button[0].config(text='O', bg='white', state='disabled') 
        my_list[0] = 'O'
    elif ((my_list[2] == 'O' and my_list[4] == 'O') or (my_list[2] == 'X' and my_list[4] == 'X')) and my_list[6] == '':
        button[6].config(text='O', bg='white', state='disabled') 
        my_list[6] = 'O'
    elif ((my_list[2] == 'O' and my_list[6] == 'O') or (my_list[2] == 'X' and my_list[6] == 'X')) and my_list[4] == '':
        button[4].config(text='O', bg='white', state='disabled') 
        my_list[4] = 'O'
    elif ((my_list[4] == 'O' and my_list[6] == 'O') or (my_list[4] == 'X' and my_list[6] == 'X')) and my_list[2] == '':
        button[2].config(text='O', bg='white', state='disabled') 
        my_list[2] = 'O'                                                   
    else:
        return False

def check_win(n):
    global move_game
    if(move_game[0] == n and move_game[1] == n and move_game[2] == n 
    or move_game[3] == n and move_game[4] == n and move_game[5] == n
    or move_game[6] == n and move_game[7] == n and move_game[8] == n
    or move_game[0] == n and move_game[3] == n and move_game[6] == n
    or move_game[1] == n and move_game[4] == n and move_game[7] == n
    or move_game[2] == n and move_game[5] == n and move_game[8] == n
    or move_game[0] == n and move_game[4] == n and move_game[8] == n
    or move_game[2] == n and move_game[4] == n and move_game[6] == n ):
        return True

def push(btn):
    global move_game
    button[btn].config(text='X', bg='white', state='disabled')
    move_game[btn] = 'X'
    if check_win('X') == True:
        mb.showinfo("Игра окончена", "Вы выиграли")
        window.destroy()     
    elif check_field_O(move_game) == False:
        first_check()
    if check_win('O') == True:
        mb.showinfo("Игра окончена", "Выиграл компьютер")
        window.destroy()
    elif move_game.count('') == 0:
        mb.showinfo("Игра окончена", "Ничья")
        window.destroy()


button = [tk.Button(width=3, height=1, font=('Arial', 40, 'bold'), bg='gray',
                    command=lambda x=i: push(x)) for i in range(9)]

button[0].grid(row=1, column=0)
button[1].grid(row=1, column=1)
button[2].grid(row=1, column=2)
button[3].grid(row=2, column=0)
button[4].grid(row=2, column=1)
button[5].grid(row=2, column=2)
button[6].grid(row=3, column=0)
button[7].grid(row=3, column=1)
button[8].grid(row=3, column=2)

window.mainloop()

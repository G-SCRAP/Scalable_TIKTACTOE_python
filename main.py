from tkinter import *
from random import *
from time import sleep
from PIL import ImageTk, Image
from threading import *
from tkinter import messagebox
import _thread
import math
'''
Gavin Ogren
Thursday, September 9th 2021
Tic Tac Toe GameTkinter Exercise

Creator Notes: Tic Tac Toe is scalable and may be adjusted to user input
Tic Tac Toe is multiplayer for 2 players and also has AI for single player mode. 

'''

"""
Dark Mode Color Scheme:
grey10
Navy Blue #1F2833
Light Grey #C5C6C7
Sky Blue #665CF1
Dark Sky Blue #45A29E
"""




ui = Tk()
ui.title("Alien Tic-Tac-Toe")
ui.geometry("600x600")
ui.minsize(600, 600)
ui.resizable(height=False, width=False)
ui.iconbitmap("Images/AlienLogo.png")

global board
global new_board
global player_turn
global lol
global start_clicked
global standard_start_button
player_turn = randint(0, 1)
new_board = []
board = []

#Clear screen widgets
def clear_screen():
    itemlist = ui.winfo_children()
    for l in itemlist:
        l.destroy()


#Ask user if they want to Quits the game
def quitgame(event):
    quitbox = messagebox.askquestion("Exit", "Are you sure you would like to exit?")
    if quitbox == "yes":
        ui.destroy()
        exit(0)
    else:
        return

#Starts the threading for the backdrop
class startloop(Thread):
    def __init__(self, ui, backdrop_label):
        self.ui = ui
        self.backdrop_label = backdrop_label
        backdrploop(backdrop_label)

#The loop of images for the backdrop
def backdrploop(backdrop_label):
    loop = True
    while loop:
        backdrop_label.config(image=backdrop)
        sleep(0.2)
        backdrop_label.config(image=backdrop2)
        sleep(0.2)
        backdrop_label.config(image=backdrop3)
        sleep(0.2)
        backdrop_label.config(image=backdrop4)
        sleep(0.2)
        backdrop_label.config(image=backdrop5)
        sleep(0.2)
        backdrop_label.config(image=backdrop4)
        sleep(0.2)
        backdrop_label.config(image=backdrop3)
        sleep(0.2)
        backdrop_label.config(image=backdrop2)
        sleep(0.2)

#This function was never used but still have future plans to have it work
def button_change():
    global standard_start_button
    standard_start_button.place_forget()
    global start_clicked
    start_button_clicked = Button(ui, image=start_clicked)
    start_button_clicked.place(x="210", y="320", width=126, height=63)
    sleep(0.5)
    singleplayer_multiplayer()

# singleplayer or mulitplayer
def singleplayer_multiplayer():
    def multiplayer():
        second_player = True
        start_game(second_player)

    def singleplayer():
        second_player = False
        start_game(second_player)
    clear_screen()

    global lol
    lol_label = Label(ui, image=lol)
    lol_label.place(x="-15", y="-15")
    singleplayer_multiplayer_heading_label = Label(ui, text="Single Player or Multiplayer", font=("helvetica", 25), bg="#78A53F", fg="red")
    singleplayer_multiplayer_heading_label.place(x="130", y="50")
    singleplayer_button = Button(ui, text="Single player Mode", command=singleplayer, width=15, height=5)
    multiplayer_button = Button(ui, text="Multiplayer Mode", command=multiplayer, width=15, height=5)
    singleplayer_button.place(x="120", y="100")
    multiplayer_button.place(x="300", y="100")

#Starts the game
def start_game(second_player):

    clear_screen()
    backdrop_label = Label(ui, image=backdrop)
    backdrop_label.place(x="-3", y="-3")
    _thread.start_new_thread(startloop, (ui, backdrop_label))

    quitbutton = Button(ui, text="QUIT", command=lambda: quitgame(0))
    quitbutton.place(x=1, y=550, width=50, height=50)

    #Clear Screen and reset variables
    def reset():
        clear_screen()
        global player_turn
        global new_board
        global board
        player_turn = randint(0, 1)
        new_board = []
        board = []
        singleplayer_multiplayer()
    # The player won
    def party(g):
        global z
        play_again = Button(ui, text="Play Again?", font=("Impact", 15), command=reset)
        if g == 1:
            for button in board:
                button["state"] = "disabled"
            player1_win_game = Label(ui, text="Player 1 Won the Game!", font=("Impact", 30))
            player1_win_game.place(x="140", y="100")
            play_again.place(x=230, y=550, width=100, height=50)
        elif g == 2:
            for button in board:
                button["state"] = "disabled"
            player2_win_game = Label(ui, text="Player 2 Won the Game!", font=("Impact", 30))
            player2_win_game .place(x="140", y="100")
            play_again.place(x=230, y=550, width=100, height=50)

        else:
            for button in board:
                button["state"] = "disabled"
            tie_game = Label(ui, text="Tie Game!", Font=("Impact", 30))
            tie_game.place(x="50", y="100")

    #Win game function checks win condition
    def wingame(z, i, a):
        v = len(board)
        e = math.sqrt(v)
        s = []
        board_value = []
        for x in range(0, v):
            print(board[x]["text"])
            s.append(board[x]["text"])
            print(s)
            if len(s) == e:
                board_value.append(s)
                s = []
        sign = ""
        win = False
        print(board_value)
        g = len(board_value)
        for x in range(0, len(board_value)):
            if board_value[x][0] == a:
                if all(sign == board_value[x][0] for sign in board_value[x]):
                    win = True
                    sign = board_value[x][0]
                    break
        for y in range(0, g):
            if board_value[0][y] == a:
                if all(sign[y] == board_value[0][y] for sign in board_value):
                    win = True
                    sign = board_value[0][y]
                    break

        if board_value[0][0] == a:
            diag = []
            number = 0
            for x in range(0, len(board_value)):
                if board_value[number][number] == a:
                    diag.append(board_value[number][number])
                number += 1
            if len(diag) == len(board_value):
                win = True
                sign = board_value[0][0]
        if board_value[0][-1] == a:
            diag = []
            number = 0
            num2 = -1
            for x in range(0, len(board_value)):
                if board_value[number][num2] == a:
                    diag.append(board_value[number][num2])
                number += 1
                num2 -= 1
            if len(diag) == len(board_value):
                win = True
                sign = board_value[0][-1]

        if win == True:
            if sign == "X":
                party(1)
            elif sign == "O":
                party(2)
        else:

            freetiles = []
            for x in board:
                if x["text"] != "X" and x["text"] != "O":
                    freetiles.append(x["text"])
            if len(freetiles) == 0:
                party(3)
            else:
                pass

    #When Player olays the game
    def play(second_player, board,z, i, y, messagelabel):
        global player_turn
        if player_turn == 0:
            messagelabel.config(text="Player 2's turn.")
            board[i - 1]["text"] = "X"
            board[i - 1]["state"] = "disabled"
            wingame(z, i, "X")
            player_turn = 1
            if second_player == False:
                player_turn = 0
                for button in board:
                    button["state"] = "disabled"
                messagelabel.config(text="CPU's turn.")

                freetiles = []
                for button in board:
                    if button["text"] != "X" and button["text"] != "O":
                        freetiles.append(button)
                Ai_move = choice(freetiles)
                Ai_move["text"] = "O"
                Ai_move["state"] = "disabled"
                for button in board:
                    if button["text"] != "X" and button["text"] != "O":
                        button["state"] = "normal"
                messagelabel.config(text="Your turn.")
                wingame(z, i, "O")

        else:
            messagelabel.config(text="Player 1's turn.")
            board[i - 1]["text"] = "O"
            board[i - 1]["state"] = "disabled"
            wingame(z, i, "O")
            player_turn = 0
    #Create the board
    def create_board(x):
        create_board_label.place_forget()
        board_size3.place_forget()
        board_size5.place_forget()
        board_size7.place_forget()
        board_size9.place_forget()
        global board
        global player_turn
        messagelabel = Label(ui)
        messagelabel.place(x="245", y="100")
        if second_player == False:
            player_turn = 0
            messagelabel.config(text="Your turn.")
        else:
            if player_turn == 0:
                messagelabel.config(text="Player 1's turn")
            else:
                messagelabel.config(text="Player 2's turn")

        width = ui.winfo_screenwidth()
        y_axis = width * 0.5 / 4.5
        y = x ** 2
        z = x ** 2 + 1

        if x == 3:
            x_axis = 190
        elif x == 5:
            x_axis = 175
        elif x == 7:
            x_axis = 150
        elif x == 9:
            x_axis = 125


        for i in range(1, z):
            x_axis = x_axis + 35
            board.append(Button(ui, text=i, width=3, command=lambda i=i: play(second_player, board,z, i, y, messagelabel)))
            board[(i-1)].place(x=x_axis, y=y_axis)
            print(x_axis)
            if len(board) % x == 0:
                if x == 3:
                    x_axis = 190
                elif x == 5:
                    x_axis = 175
                elif x == 7:
                    x_axis = 150
                elif x == 9:
                    x_axis = 125
                y_axis = y_axis + 15
                if i < y:
                    if x == 3:
                        x_axis = 190
                    elif x == 5:
                        x_axis = 175
                    elif x == 7:
                        x_axis = 150
                    elif x == 9:
                        x_axis = 125
                    y_axis = y_axis + 15

    create_board_label = Label(ui, text="Select Board Size")
    create_board_label.place(x="225", y="100")
    board_size3 = Button(ui, text="3x3", command=lambda: create_board(3))
    board_size5 = Button(ui, text="5x5", command=lambda: create_board(5))
    board_size7 = Button(ui, text="7x7", command=lambda: create_board(7))
    board_size9 = Button(ui, text="9x9", command=lambda: create_board(9))
    board_size3.place(x="200", y="150", width=70, height=70)
    board_size5.place(x="300", y="150", width=70, height=70)
    board_size7.place(x="200", y="250", width=70, height=70)
    board_size9.place(x="300", y="250", width=70, height=70)


# - This command sets button state to deactivated, making the text darker and unable to be clicked.
# button["state"] == "disabled"

# - This command re-enables button if it has been deactivated, allowing it to work as it normally does.
# button["state"] == "normal"

# - This command sets the button as activated, as if the button was being highlighted by the user.
# button["state"] == "active"

image1 = Image.open("Images/Intro.png")
lol = PhotoImage(file="Images/lol.png")

global backdrop
global backdrop2
global backdrop3
global backdrop4
global backdrop5


backdrop = PhotoImage(file="Images/Backdrop1.png")
backdrop2 = PhotoImage(file="Images/Backdrop2.png")
backdrop3 = PhotoImage(file="Images/Backdrop3.png")
backdrop4 = PhotoImage(file="Images/Backdrop4.png")
backdrop5 = PhotoImage(file="Images/Backdrop5.png")





#Photo Image
start_clicked = PhotoImage(file="Images/ButtonClick.png")
intro = ImageTk.PhotoImage(image1)
intro_label = Label(ui, image=intro)
intro_label.pack()
image2 = Image.open("Images/ButtonStandard.png")

start_button_clicked = Button(ui, image=start_clicked)
start_button_clicked.place(x="210", y="320", width=126, height=63)

standard_start = ImageTk.PhotoImage(image2)
standard_start_button = Button(ui, image=standard_start, command=button_change)
standard_start_button.place(x="210", y="320", width=126, height=63)


intro_header1 = Label(ui, text="ALIEN", fg="red", font=("Impact", 40))
intro_header2 = Label(ui, text="TIC - TAC - TOE", fg="red", font=("Impact", 40))
intro_header1.place(x="225", y="160")
intro_header2.place(x="160", y="220")
ui.bind("<Escape>", quitgame)

ui.mainloop()
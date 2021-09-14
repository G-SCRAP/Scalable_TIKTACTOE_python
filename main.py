from tkinter import *
from random import randint
import time
from PIL import ImageTk, Image
from tkinter import messagebox

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


def clear_screen():
    itemlist = ui.winfo_children()
    for l in itemlist:
        l.destroy()

ui = Tk()
ui.title("Alien Tic-Tac-Toe")
ui.geometry("600x600")
ui.minsize(600, 600)
ui.resizable(height=False, width=False)
ui.iconbitmap("Images/AlienLogo.png")




global board
global player_turn
player_turn = randint(0, 1)
print(player_turn)
board = []




def start_game():
    clear_screen()

    def create_board():
        def board_size(x):
            global board

            clear_screen()

            width = ui.winfo_screenwidth()
            height = ui.winfo_screenheight()

            def height_width():


            print(height)

            x_axis = height * 0.5 / 4.5

            if x < 5:
                x_axis += 50
                if x < 3:
                    x_axis += 50

            y_axis = width * 0.5 / 4.5

            print(y_axis)
            y = x ** 2
            z = x ** 2 + 1

            if x > 3:
                pass
            elif x > 5:
                pass
            elif x > 7:
                pass
            elif x > 9:
                pass
            for i in range(1, z):
                x_axis = x_axis + 35
                board.append(Button(ui, text=i, width=3))
                #for button in board:
                    #button["state"] == ""
                board[(i-1)].place(x=x_axis, y=y_axis)
                if len(board) % x == 0:
                    x_axis = 100
                    y_axis = y_axis + 15
                    if i < y:
                        x_axis = 100
                        y_axis = y_axis + 15

# - This command sets button state to deactivated, making the text darker and unable to be clicked.
# button["state"] == "disabled"

# - This command re-enables button if it has been deactivated, allowing it to work as it normally does.
# button["state"] == "normal"

# - This command sets the button as activated, as if the button was being highlighted by the user.
# button["state"] == "active"

        create_board_label = Label(ui, text="Select Board Size")
        create_board_label.place(x="250", y="100")

        board_size3 = Button(ui, text="3x3", command=lambda: board_size(3))
        board_size5 = Button(ui, text="5x5", command=lambda: board_size(5))
        board_size7 = Button(ui, text="7x7", command=lambda: board_size(7))
        board_size9 = Button(ui, text="9x9", command=lambda: board_size(9))

        board_size3.place(x="225", y="225")
        board_size5.place(x="325", y="325")
        board_size7.place(x="225", y="125")
        board_size9.place(x="325", y="125")

    def single_player():
        print("Hello World")

    def multiplayer():
        print("Hello world")

    create_board()


image1 = Image.open("Images/Intro.png")
intro = ImageTk.PhotoImage(image1)
intro_label = Label(ui, image=intro)
intro_label.pack()

image2 = Image.open("Images/ButtonStandard.png")
standard_start = ImageTk.PhotoImage(image2)
standard_start_button = Button(ui, image=standard_start, command= start_game)
standard_start_button.place(x="210", y="320", width=126, height=63)


intro_header1 = Label(ui, text="ALIEN", fg="red", font=("Impact", 40))
intro_header2 = Label(ui, text="TIC - TAC - TOE", fg="red", font=("Impact", 40))
intro_header1.place(x="225", y="160")
intro_header2.place(x="160", y="220")


ui.mainloop()

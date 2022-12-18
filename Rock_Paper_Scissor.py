from tkinter import *
# from PIL import Image, ImageTk                     #PIL for images
from random import randint

window = Tk()

window.title("Rock Paper Scissor")

window.configure(background="skyblue")  # or window.config(bg="black")

# This is for inserting image in code
rock1 = PhotoImage(file="rps/rock.png")
paper1 = PhotoImage(file="rps/paper.png")
scissor1 = PhotoImage(file="rps/scissor.png")

# This is for inserting image on left & right side
label_player = Label(window, image=paper1, width=255, height=200)
label_computer = Label(window, image=paper1, width=255, height=200)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

# This is for inserting score for player and computer
computer_score = Label(window, text=0, font=("arial", 60, "bold"), fg="red")
player_score = Label(window, text=0, font=("arial", 60, "bold"), fg="red")
computer_score.grid(row=1, column=1)
player_score.grid(row=1, column=3)

# This is for indicating player and computers tab

player_indicator = Label(window, font=("arial", 30, "bold"), text="PLAYER", bg="orange", fg="purple", height=1,
                         width=10)
computer_indicator = Label(window, font=("arial", 30, "bold"), text="COMPUTER", bg="orange", fg="purple", height=1,
                           width=10)
player_indicator.grid(row=0, column=3)
computer_indicator.grid(row=0, column=1)


def msg_updation(a):
    final_message['text'] = a


def Computer_Update():
    final = int(computer_score['text'])
    final += 1
    computer_score['text'] = str(final)


def Player_Update():
    final = int(player_score['text'])
    final += 1
    player_score['text'] = str(final)


# This is for checking the result
def winner_check(p, c):
    if p == c:
        msg_updation("It's a tie")
    elif p == "rock":
        if c == "paper":
            msg_updation("Computer Wins !!")
            Computer_Update()
        else:
            msg_updation("Player Wins :)")
            Player_Update()

    elif p == "paper":
        if c == "scissor":
            msg_updation("Computer Wins !!")
            Computer_Update()
        else:
            msg_updation("Player Wins :)")
            Player_Update()

    elif p == "scissor":
        if c == "rock":
            msg_updation("Computer Wins !!")
            Computer_Update()
        else:
            msg_updation("Player Wins :)")
            Player_Update()
    else:
        pass


to_select = ["rock", "paper", "scissors"]


# This is to change the picture with the choices
def choice_update(a):
    choice_computer = to_select[randint(0, 2)]
    if choice_computer == "rock":
        label_computer.configure(image=rock1)
    elif choice_computer == "paper":
        label_computer.configure(image=paper1)
    else:
        label_computer.configure(image=scissor1)

    if a == "rock":
        label_player.configure(image=rock1)
    elif a == "paper":
        label_player.configure(image=paper1)
    else:
        label_player.configure(image=scissor1)

    winner_check(a, choice_computer)


# This is for outputing the result / Final messange
final_message = Label(window, font=("arial", 20, "bold"), bg="skyblue", fg="black", width=15, height=1)
final_message.grid(row=3, column=2)

# This is for making button in window
button_rock = Button(window, width=16, height=3, text="ROCK", font=("arial", 20, "bold"), bg="aliceblue", fg="purple",
                     command=lambda: choice_update("rock")).grid(row=2, column=1)

button_paper = Button(window, width=16, height=3, text="PAPER", font=("arial", 20, "bold"), bg="aliceblue", fg="red",
                      command=lambda: choice_update("paper")).grid(row=2, column=2)

button_scissor = Button(window, width=16, height=3, text="SCISSOR", font=("arial", 20, "bold"), bg="aliceblue",
                        fg="darkgreen", command=lambda: choice_update("scissor")).grid(row=2, column=3)

window.mainloop()

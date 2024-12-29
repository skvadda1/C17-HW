import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.geometry("500x500")
window.title("v1.0.0   Rock, Paper, Scissors")
choices = ["Rock", "Paper", "Scissors"]
computerChoice = random.choice(choices)
def decision():
    user_choice = print("Rock, Paper, Or Scissors" + entry.get())
    computerResponse = tk.Label(window,text=computerChoice)
    computerResponse.pack()
    userResponse = tk.Label(window,text=user_choice)
    userResponse.pack()
    if(user_choice == "Rock" and computerChoice == "Paper"):
        l1 =tk.Label(window, text="Computer Wins!, Paper covers Rock.")
        l1.pack()
    elif(user_choice =="Paper" and computerChoice == "Rock"):
        l2 = tk.Label(window, text="You Win!, Paper covers Rock.")
        l2.pack()
    elif(user_choice == "Paper" and computerChoice == "Scissors"):
        l3 = tk.Label(window, text="Computer Wins!, Scissors cuts Paper!")
        l3.pack()
    elif(user_choice == "Scissors" and computerChoice == "Paper"):
        l4 = tk.Label(window, text="You Win!, Scissors cuts Paper!")
        l4.pack()
    elif(user_choice == "Rock" and computerChoice == "Scissors"):
        l5 = tk.Label(window, text="You Win!, Rock crushes Scissors")
        l5.pack()
    elif(user_choice == "Scissors" and computerChoice == "Rock"):
        l6 = tk.Label(window, text="Computer Wins!, Rock crushes Scissors")
        l6.pack()
    else:
        print("Response Invalid, please restart the game")
title = tk.Label(window, text ="Welcome to Rock,Paper,Scissors\n v1.0.0")
title.pack()
info = tk.Label(window, text="*Note that this is the first release of this software so there may be some bugs")
info.pack()
instructions = tk.Label(window,text="Please type Rock, Paper, or Scissors in the textbox below to begin the game")
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window,text='submit',command=decision)
button.pack()


window.mainloop()
import tkinter as tk
from tkinter import messagebox
import random

score=0
total_game=0

choose=["rock","paper","scissor"]
print("choose from: ",choose)
def play(your_choice):
    global score, total_game
    
    user_text.set(f"You chose: {your_choice}")
        
    computer_choice=random.choice(choose)
    comp_text.set(f"Computer chose: {computer_choice}")
    
    if(your_choice==computer_choice):
        result.set("It's a tie!!!")
    elif(your_choice=="rock" and computer_choice=="scissor")or(your_choice=="paper" and computer_choice=="rock")or(your_choice=="scissor" and computer_choice=="paper"):
        result.set("You win!!!")
        score+=1
    else:
        result.set("You Lose!!!")
        
    total_game+=1
    score_text.set(f"{score}/{total_game}")
    
    play_again=messagebox.askyesno("Do you want to play again?", f"You chose {your_choice}\nComputer chose {computer_choice}\n\nPlay again?")
    if not play_again:
        root.destroy()

root=tk.Tk()
root.geometry("300x300")
root.title("Rock Paper Scissor")

user_text=tk.StringVar()
result=tk.StringVar()
score_text=tk.StringVar(value="0/0")
comp_text=tk.StringVar()

tk.Label(root, text="Choose one: ",font=("Arial",12)).pack(pady=5)

tk.Button(root, text="Rock", width=12, command=lambda: play("rock")).pack(pady=4)
tk.Button(root, text="Paper", width=12, command=lambda: play("paper")).pack(pady=4)
tk.Button(root, text="Scisssor", width=12, command=lambda: play("scissor")).pack(pady=4)

tk.Label(root, textvariable=user_text).pack(pady=5)
tk.Label(root, textvariable=comp_text, font=("Arial", 10)).pack(pady=5)
tk.Label(root, textvariable=result, font=("Arial", 12, "bold")).pack(pady=5)
tk.Label(root, text="Score: ", font=("Arial", 10)).pack()
tk.Label(root,textvariable=score_text, font=("Arial", 11)).pack()

root.mainloop()
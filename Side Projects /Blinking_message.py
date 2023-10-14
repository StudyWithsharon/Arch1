import sys
from tkinter import *
import random

def color_change():
    list1 = ["red", "yellow", "blue", "orange"]
    virus.config(bg=random.choice(list1))  # Change 'backround' to 'bg'
    virus.after(200, color_change)

root = Tk()
root.geometry("700x250")
virus = Label(root, text="YOU ARE HACKED!", font=("times", 50, "bold"))
virus.grid(row=2, column=0, pady=20, padx=20)  # Add a missing comma in padx
color_change()

root.mainloop()

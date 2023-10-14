print("""

██████╗  ██████╗  ██████╗ ██╗  ██╗     ██████╗ ██╗   ██╗██╗███████╗██╗
██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔═══██╗██║   ██║██║╚══███╔╝██║
██████╔╝██║   ██║██║   ██║█████╔╝     ██║   ██║██║   ██║██║  ███╔╝ ██║
██╔══██╗██║   ██║██║   ██║██╔═██╗     ██║▄▄ ██║██║   ██║██║ ███╔╝  ╚═╝
██████╔╝╚██████╔╝╚██████╔╝██║  ██╗    ╚██████╔╝╚██████╔╝██║███████╗██╗
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚═╝
                                                                     
""")

import tkinter as tk

def check_answer():
    user_answer = entry.get().lower()
    if user_answer == current_answer.lower():
        result_label.config(text="CORRECT!")
    else:
        result_label.config(text="Try again")

def next_question():
    global current_question, current_answer
    if current_question == 1:
        current_question += 1
        question_label.config(text="You don’t know about me without you have read a book by the name of The Adventures of Tom Sawyer, but that ain’t no matter. Which Book?")
        current_answer = "the adventures of huckleberry finn"
    else:
        # Add more questions and answers as needed
        pass
    entry.delete(0, 'end')  # Clear the entry box

root = tk.Tk()
root.title("Book Quiz")

current_question = 1

question_label = tk.Label(root, text="And so we beat on, boats against the current, borne back ceaselessly into the past. Which Book?")
question_label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Check Answer", command=check_answer)
check_button.pack()

next_button = tk.Button(root, text="Next Question", command=next_question)
next_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Define the current question and answer
current_answer = "the great gatsby"

root.mainloop()


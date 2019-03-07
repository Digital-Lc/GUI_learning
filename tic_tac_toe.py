from tkinter import *

root = Tk()
root.title("Tic Tac Toe")
root.geometry("252x358")
root.option_add("*font", "Calibri", "30")

next = "X"

def place_point(button):
    global next
    print("A player has taken a turn")


title = Label(root, text="Tic Tac Toe", width=10, height=3).grid(row=0, column=0, columnspan=3, sticky=N+S+W+E)

button1 = Button(root, text="", width=10, height=5, command=lambda:place_point("")).grid(row=1, column=0, sticky=N+S+W+E)
button2 = Button(root, text="", width=10, height=5, command=lambda:place_point("")).grid(row=1, column=1, sticky=N+S+W+E)
button3 = Button(root, text="", width=10, height=5, command=lambda:place_point("")).grid(row=1, column=2, sticky=N+S+W+E)
button4 = Button(root, text="", width=10, height=5, command=lambda:place_point("")).grid(row=2, column=0, sticky=N+S+W+E)
button5 = Button(root, text="", width=10, height=5, command=lambda:place_point("")).grid(row=2, column=1, sticky=N+S+W+E)
button6 = Button(root, text="", width=10, height=5, command=lambda:place_point("")).grid(row=2, column=2, sticky=N+S+W+E)
button7 = Button(root, text="", width=10, height=5, command=lambda:place_point("")).grid(row=3, column=0, sticky=N+S+W+E)
button8 = Button(root, text="", width=10, height=5, command=lambda:place_point("")).grid(row=3, column=1, sticky=N+S+W+E)
button9 = Button(root, text="", width=10, height=5, command=lambda:("")).grid(row=3, column=2, sticky=N+S+W+E)
reset_button = Button(root, text="Reset", width=30, height=3, command=lambda:reset_game("")).grid(row=4, column=0, columnspan=3, sticky=N+S+W+E)

root.mainloop()
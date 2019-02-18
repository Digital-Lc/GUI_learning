import tkinter
root = tkinter.Tk()

def print_1():
    print("What the hell man?")

def print_2():
    print("uwu")

button1 = tkinter.Button(root)
button1.config(text="Kill me",
               bg="Black",
               fg="Red",
               font=("Comic San MS", "50"), command=print_1)
button1.grid()

button2 = tkinter.Button(root)
button2.config(text="Save me",
               bg="Black",
               fg="Red",
               font=("Comic San MS", "50"), command=print_2)
button2.grid()

root.mainloop()

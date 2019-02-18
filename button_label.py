import tkinter

count = 0

def count_up():
    global count
    count += 1
    count_text.set(count)

def count_down():
    global count
    count -= 1
    count_text.set(count)

root = tkinter.Tk()

count_text = tkinter.StringVar()
count_text.set("0")

up_btn = tkinter.Button(root)
up_btn.config(text="Count up", command=count_up, bg="#32CD32", fg="#F0FDEE", font=("Copperplate", 50))
up_btn.grid()

down_btn = tkinter.Button(root)
down_btn.config(text="Count down", command=count_down, bg="#FF4500", fg="#FFFAFA", font=("Copperplate", 50))
down_btn.grid()

count_label = tkinter.Label(root)
count_label.config(textvariable=count_text)
count_label.grid()

root.mainloop()
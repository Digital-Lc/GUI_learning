import tkinter

count = 0

def count_up():
    global count
    if count:
        print(count)
    count += 1
    print(count)

def count_down():
    global count
    count -= 1
    print(count)

root = tkinter.Tk()

up_btn = tkinter.Button(root)
up_btn.config(text="Count up", command=count_up, bg="#32CD32", fg="#F0FDEE", font=("Copperplate", 50))
up_btn.grid()

down_btn = tkinter.Button(root)
down_btn.config(text="Count down", command=count_down, bg="#FF4500", fg="#FFFAFA", font=("Copperplate", 50))
down_btn.grid()

root.mainloop()
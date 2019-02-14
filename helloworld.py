import tkinter
root = tkinter.Tk()

root.title("Hello World!")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text="WE ARE ALL GOING TO DIE", font=("Comic Sans MS", "50"), fg="white", bg="light pink")
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="Have a good day", fg="white", bg="light pink")
my_label.grid()

root.mainloop()
from tkinter import *

root = Tk()
root.title("Calculator")
root.option_add("*font", " Georgia 20")

input_text = StringVar()
input_text.set("")

answer_value = StringVar()
answer_value.set("")

button1 = Button(root, text="7", width=3, command=lambda:add_to_input_text("7")).grid(row=0, column=0, sticky=N+S+W+E)
button2 = Button(root, text="8", width=3, command=lambda:add_to_input_text("8")).grid(row=0, column=1, sticky=N+S+W+E)
button3 = Button(root, text="9", width=3, command=lambda:add_to_input_text("9")).grid(row=0, column=2, sticky=N+S+W+E)
button4 = Button(root, text="4", width=3, command=lambda:add_to_input_text("4")).grid(row=1, column=0, sticky=N+S+W+E)
button5 = Button(root, text="5", width=3, command=lambda:add_to_input_text("5")).grid(row=1, column=1, sticky=N+S+W+E)
button6 = Button(root, text="6", width=3, command=lambda:add_to_input_text("6")).grid(row=1, column=2, sticky=N+S+W+E)
button7 = Button(root, text="1", width=3, command=lambda:add_to_input_text("1")).grid(row=2, column=0, sticky=N+S+W+E)
button8 = Button(root, text="2", width=3, command=lambda:add_to_input_text("2")).grid(row=2, column=1, sticky=N+S+W+E)
button9 = Button(root, text="3", width=3, command=lambda:add_to_input_text("3")).grid(row=2, column=2, sticky=N+S+W+E)
button0 = Button(root, text="0", width=3, command=lambda:add_to_input_text("0")).grid(row=3, column=0, sticky=N+S+W+E)

button_add      = Button(root, text="+", width=3, command=lambda:add_to_input_text("+")).grid(row=0, column=3, sticky=N+S+W+E)
button_subtract = Button(root, text="-", width=3, command=lambda:add_to_input_text("-")).grid(row=1, column=3, sticky=N+S+W+E)
button_multiply = Button(root, text="*", width=3, command=lambda:add_to_input_text("*")).grid(row=2, column=3, sticky=N+S+W+E)
button_equals   = Button(root, text="=", width=3, command=lambda:answer()).grid(row=3, column=1, columnspan=2, sticky=N+S+W+E)
button_divide   = Button(root, text="/", width=3, command=lambda:add_to_input_text("/")).grid(row=3, column=3, sticky=N+S+W+E)

input_area = Label(root, textvariable=input_text, bg="tomato", fg="white").grid(row=4, column=0,columnspan=4, sticky=N+S+W+E)
answer_area = Label(root, textvariable=answer_value, bg="pale green", fg="white").grid(row=5, column=0,columnspan=4, sticky=N+S+W+E)

button_clear = Button(root, text="Clear", command=lambda:clear()).grid(row=6, column=0,columnspan=4, sticky=N+S+W+E)


def add_to_input_text(next_val):
    current_text = input_text.get()
    input_text.set(current_text+next_val)

def answer():
    ans = eval(input_text.get())
    answer_value.set(ans)

def clear():
    input_text.set("")
    answer_value.set("")

root.mainloop()
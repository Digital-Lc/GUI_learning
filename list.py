class Note:
    def __init__(self, title, text, category):
        self.__title = title
        self.__text = text
        self.__category = category

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def get_category(self):
        return self.__category

from tkinter import *

root = Tk()
root.title("Notes")
root.geometry("400x600")
root.option_add("*font", "Calibri", "30")

notes = []

def save_note(window,title, body, category="To do"):
    new_note = Note(title.title().strip(), body.title().strip(), category.title().strip())
    notes.append(new_note)
    print("Category: {}".format(new_note.get_category()))
    print("Title: {}".format(new_note.get_title()))
    print("Body: {}".format(new_note.get_text()))
    window.destroy()

def open_new_note():
    print("Open new note window")
    title_value = StringVar()
    text_value = StringVar()

    new_note_window = Toplevel(root)

    new_note_title = Label(new_note_window, text="New Note")
    new_note_title.grid()

    title_label = Label(new_note_window, text="Title:")
    title_label.grid(sticky=W)

    title_entry = Entry(new_note_window, textvariable=title_value)
    title_entry.grid()

    note_label = Label(new_note_window, text="Note text:")
    note_label.grid(sticky=W)

    note_text = Text(new_note_window)
    note_text.config(height=10, width=20)
    note_text.grid()

    button_frame = Frame(new_note_window)
    button_frame.grid()

    cancel_button = Button(button_frame, text="Cancel", command=new_note_window.destroy)
    cancel_button.grid(row=0, column=1, sticky=E)

    save_button = Button(button_frame, text="Save", command=lambda: save_note(new_note_window, title_value.get(), note_text.get(1.0, END)))
    save_button.grid(row=0, column=2, sticky=E)


def open_list(list_name):
    print("Open a list")



title = Label(root, text="Notes", bg="light grey", fg="Black")
title.config(font=("Calibri", "30"), width=24)
title.grid(row=0, sticky=N+S+W+E)

new_note = Button(root, text="+ New note", bg="light grey", fg="black", command=lambda:open_new_note())
new_note.config(font=("Calibri", "30"))
new_note.grid(row=1, sticky=W)

new_todo = Button(root, text="To do",bg="light grey", fg="black", command=lambda:open_list("To do"))
new_todo.config(font=("Calibri", "30"))
new_todo.grid(row=2, sticky=N+S+W+E)

new_homework = Button(root, text="Homework", bg="light grey", fg="black", command=lambda:open_list("Homework"))
new_homework.config(font=("Calibri", "30"))
new_homework.grid(row=3, sticky=N+S+W+E)

new_date = Button(root, text="Dates", bg="light grey", fg="black", command=lambda:open_list("Dates"))
new_date.config(font=("Calibri", "30"))
new_date.grid(row=4, sticky=N+S+W+E)

root.mainloop()
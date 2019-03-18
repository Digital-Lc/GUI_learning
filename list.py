class Note:
    """
    """

    def __init__(self, title, text, category):
        self.__title = title
        self.__text = text
        self.__category = category

    def get_title(self):
        """Getter function: gets the note title
        Returns: the title of the note
        """
        return self.__title

    def get_text(self):
        """Getter function: gets the note body text
        Returns: the body text of the note
        """
        return self.__text

    def get_category(self):
        """Getter function: gets the note category
        Returns: the category of the note
        """
        return self.__category


from tkinter import *

# creates and sets up the window
root = Tk()
root.title("Notes")
root.option_add("*font", "Consolas 20")
root.geometry("397x600")

# this list is where all note objects will be stored
notes = []


def save_note(window, title, body, category="Shopping"):
    """Saves a note to the note list then closes the parent window.
    Args:
        window: the window this function was called from
        title: the title of the note to be saved
        body: the body text of the note to be saved
        category: the category of the note to be saved
    """

    # creates the note object, after cleaning up the input values
    new_note = Note(title.capitalize().strip(),
                    body.capitalize().strip(),
                    category.capitalize().strip())

    # add the note to the note list
    notes.append(new_note)
    print("Title: {}".format(new_note.get_title()))
    print("Body: {}".format(new_note.get_text()))
    print("Category: {}".format(new_note.get_category()))

    # close the window this function was called from
    window.destroy()


def open_new_note(category):
    """Creates a window for the user to enter their note in."""
    print("Open new note window")
    title_value = StringVar()

    # creates the window
    new_note_window = Toplevel(root)

    # creates and adds labels and text entry areas
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

    # a frame allows us to group GUI elements together
    # this one will hold the buttons
    button_frame = Frame(new_note_window)
    button_frame.grid()

    cancel_button = Button(button_frame, text="Cancel", command=new_note_window.destroy)
    cancel_button.grid(row=0, column=1, sticky=E)

    save_button = Button(button_frame,
                         text="Save",
                         command=lambda: save_note(new_note_window,
                                                   title_value.get(),
                                                   note_text.get(1.0, END),
                                                   category))

    save_button.grid(row=0, column=2, sticky=E)


def open_list(list_category):
    """Opens a window with all of the notes of the given category.
    Args:
        list_category: the category this window should display
    """
    print("Open {}".format(list_category))

    # creates and formats the window
    list_window = Toplevel(root)
    list_window.title(list_category)
    list_window.geometry("600x400")

    # takes each note from the list, formats it and adds it to the window
    for note in notes:
        title = note.get_title()
        body = note.get_text()
        category = note.get_category()

        note_text = "***{}***\n{}\n".format(title, body)

        # only add notes with the relevant category
        if category == list_category:
            Label(list_window, text=note_text).grid(sticky=W)


"""
    The main (root) window is configured from here down.
    It is not in a function so all widgets etc are globally accessible.
"""

title = Label(root, text="Notes", bg="light grey", fg="Black")
title.config(font=("Calibri", "30"), width=23)
title.grid(row=0, column=0, columnspan=2, sticky=N+S+W+E)

new_todo = Button(root, text="To do",bg="light grey", fg="black", command=lambda:open_list("To do"))
new_todo.config(font=("Calibri", "30"), width=15)
new_todo.grid(row=1, column=0, sticky=N+S+W+E)

new_todo_note = Button(root, text="+", bg="light grey", fg="black", command=lambda:open_new_note("To do"))
new_todo_note.config(font=("Calibri", "30"), width=4)
new_todo_note.grid(row=1, column=1, sticky=W+E)

new_homework = Button(root, text="Homework", bg="light grey", fg="black", command=lambda:open_list("Homework"))
new_homework.config(font=("Calibri", "30"), width=15)
new_homework.grid(row=2, column=0, sticky=N+S+W+E)
""
new_todo_note = Button(root, text="+", bg="light grey", fg="black", command=lambda:open_new_note("Homework"))
new_todo_note.config(font=("Calibri", "30"), width=4)
new_todo_note.grid(row=2, column=1, sticky=W+E)

new_date = Button(root, text="Dates", bg="light grey", fg="black", command=lambda:open_list("Dates"))
new_date.config(font=("Calibri", "30"), width=15)
new_date.grid(row=3, column=0, sticky=N+S+W+E)

new_todo_note = Button(root, text="+", bg="light grey", fg="black", command=lambda:open_new_note("Dates"))
new_todo_note.config(font=("Calibri", "30"), width=4)
new_todo_note.grid(row=3, column=1, sticky=W+E)

root.mainloop()
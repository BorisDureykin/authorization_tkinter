import tkinter as tk
from tkinter import Button, Label, Tk
from database.sqliteUser import clearDatabase, deleteUser

def confirmationWindow(textLbl, textBtn, comm, arg, window):
    confirmationWindow = tk.Toplevel()
    confirmationWindow.title('Confirmation Window!')
    confirmationWindow.geometry('400x250')
    command=''
    if comm=='clear':
        command=lambda: [clearDatabase(), window.destroy(), confirmationWindow.destroy()]
    if comm=='delete':
        command=lambda: [deleteUser(arg), window.destroy(), confirmationWindow.destroy()]

    lbl = Label(confirmationWindow, text=textLbl,
                   font=("Arial Bold", 14))
    lbl.pack()

    btn = Button(confirmationWindow, text=textBtn, width=20,
                    height=1, command=command)
    btn.pack()

    btn1 = Button(confirmationWindow, text='Отмена', width=20,
                  height=1, command=lambda: confirmationWindow.destroy())
    btn1.pack()

    confirmationWindow.transient()
    confirmationWindow.grab_set()
    confirmationWindow.focus_set()
    confirmationWindow.wait_window()
    confirmationWindow.mainloop()

def errorWindow(text):
    error = Tk()
    error.title('Ошибка!')
    error.geometry('350x100')
    error.attributes("-topmost", True)

    lbl = Label(error, text=f'{text}', font=("Arial Bold", 10))
    lbl.pack()

    btn = Button(error, text='Ок', width=10,
                           height=1, command=error.destroy)
    btn.pack()

    error.mainloop()

def successfulRegistration(title, text, window):
    if window != None:
        window.destroy()
    successfulRegistration = tk.Toplevel()
    successfulRegistration.title(title)
    successfulRegistration.geometry('600x100')

    lbl = Label(successfulRegistration, text=f'{text}', font=("Arial Bold", 10))
    lbl.pack()

    btn = Button(successfulRegistration, text='Ок', width=10,
                           height=1, command=successfulRegistration.destroy)
    btn.pack()

    successfulRegistration.transient()
    successfulRegistration.grab_set()
    successfulRegistration.focus_set()
    successfulRegistration.wait_window()
    successfulRegistration.mainloop()
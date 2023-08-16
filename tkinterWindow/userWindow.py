import tkinter as tk
from tkinter import Label, Button
from tkinterWindow.notificationWindow import confirmationWindow
from tkinterWindow.updateWindow import updateWindow

def userWindow(login, user_id):
    userWindow = tk.Toplevel()
    userWindow.title('User!')
    userWindow.geometry('400x250')

    lbl = Label(userWindow, text=f'Добро пожаловать {login}!', font=("Arial Bold", 14))
    lbl.pack()

    btn = Button(userWindow, text='Update user', width=30,
                           height=1,  command=lambda :[updateWindow(user_id,login, userWindow)])
    btn.pack()

    btn = Button(userWindow, text='Delete User', width=30,
                           height=1, command=lambda: [confirmationWindow("Подтвердите удаление\nданных пользователя!",
                                                                "Удалить!", 'delete', user_id, userWindow)])
    btn.pack()

    btn = Button(userWindow, text='Выход', width=30,
                           height=1, command=userWindow.destroy)
    btn.pack()

    userWindow.transient()
    userWindow.grab_set()
    userWindow.focus_set()
    userWindow.wait_window()
    userWindow.mainloop()

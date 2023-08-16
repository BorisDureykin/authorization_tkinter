import ast
import tkinter as tk
from tkinter import Label, Button, Listbox, END
from database.sqliteUser import getUserAll
from tkinterWindow.notificationWindow import confirmationWindow, errorWindow
from tkinterWindow.updateWindow import updateWindow

def adminWindow(login, role_admin):
    adminWindow = tk.Toplevel()
    adminWindow.title('Admin!')
    adminWindow.geometry('400x250')

    lbl = Label(adminWindow, text=f'Добро пожаловать {login}!', font=("Arial Bold", 14))
    lbl.pack()

    btn = Button(adminWindow, text='Clear the database!', width=20, height=1,)
    btn.config(command=lambda: confirmationWindow('Подтвердите очистку Базы данных!\nДанные востановить не возможно!',
                                                    'Clear the database!', 'clear', 0, adminWindow))
    btn.pack()

    btn = Button(adminWindow, text='Viewing User', width=20,
                 height=1, command=lambda: viewingWindow(adminWindow, role_admin))
    btn.pack()

    btn = Button(adminWindow, text='Выход', width=20,
                 height=1, command=adminWindow.destroy)
    btn.pack()

    adminWindow.transient()
    adminWindow.grab_set()
    adminWindow.focus_set()
    adminWindow.wait_window()
    adminWindow.mainloop()

def viewingWindow(window, role_admin):
    window.destroy()
    records = getUserAll()
    viewingWindow = tk.Toplevel()
    viewingWindow.title('Viewing User!')
    viewingWindow.geometry('700x300')

    lbl = Label(viewingWindow, text='Просмотр и редактирование пользователей!', font=("Arial Bold", 14))
    lbl.pack()
    listbox = Listbox(viewingWindow, height=10, width=100)
    for row in records:
        user = {'user_id': row[0],
                'login': row[1],
                'password': row[2],
                'eMail': row[3],
                'role': row[4]
                }
        listbox.insert(END, f'{user}')
    listbox.yview_scroll(number=1, what="units")

    listbox.pack()

    btn = Button(viewingWindow, text='Delete User!', width=20,
                 height=1, command=lambda: confirmationWindow('Подтвердите удаление\nданных пользователя!',
                                                              'Удалить!', 'delete', user_id(), viewingWindow))
    btn.pack()

    btn = Button(viewingWindow, text='Update User!', width=20,
                 height=1, command=lambda: [(updateWindow(user_id(), role_admin, viewingWindow))])
    btn.pack()

    btn = Button(viewingWindow, text='Выход!', width=20, height=1, command=viewingWindow.destroy)
    btn.pack()

    def user_id():
        try:
            user_id = ast.literal_eval(listbox.get(listbox.curselection()))['user_id']
        except:
            errorWindow('Не выбран пользователь!')
        else:
            return user_id

    viewingWindow.transient()
    viewingWindow.grab_set()
    viewingWindow.focus_set()
    viewingWindow.wait_window()
    viewingWindow.mainloop()

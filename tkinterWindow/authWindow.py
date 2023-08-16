from tkinter import Tk, Label, Entry, Button
from action.checks import isUserInDb
from tkinterWindow.adminWindow import adminWindow
from tkinterWindow.notificationWindow import errorWindow
from tkinterWindow.regWindow import reg
from tkinterWindow.userWindow import userWindow


def authWindow():

    authWindow = Tk()
    authWindow.title('Авторизация!')
    authWindow.geometry('400x250')


    lbl = Label(authWindow, text='Авторизация', font=("Arial Bold", 14))
    lbl.pack()

    login = Entry(authWindow, width=30)
    login.pack()

    password = Entry(authWindow, width=30)
    password.pack()

    btn = Button(authWindow, text='Вход', width=20,
                           height=1, command=lambda: authorizationVerification(login.get(), password.get()))
    btn.pack()

    btn1 = Button(authWindow, text='Зарегистрироваться', width=20,
                           height=1, command=reg)
    btn1.pack()

    btn2 = Button(authWindow, text='Выход', width=20,
                           height=1, command=lambda: exit())
    btn2.pack()

    authWindow.mainloop()

def authorizationVerification(login, password):
    records = isUserInDb('login', login)

    if records is None:
        errorWindow('Логин или пароль\nвведены не верно!')

    for row in records:
        if row[2] != password:
            errorWindow('Логин или пароль\nвведены не верно!')
    user_id = row[0]
    login = row[1]
    role = row[4]

    if role == 'admin':
        adminWindow(login, role)

    if role == 'customer' or role == 'manager':
        userWindow(login,user_id)
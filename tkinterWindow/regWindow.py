import tkinter as tk
from tkinter import *
from action.checks import loginVerification, passwordVerification, emailVerification
from database.sqliteUser import putUser
from tkinterWindow.notificationWindow import successfulRegistration


def reg():
    regWindow('login')

def regWindow(text):
    def loginget(entry):
        loginVerification(entry)
        regWindow.destroy()
        returnlogin(entry)

    def passwordget(entry):
        passwordVerification(entry)
        regWindow.destroy()
        returnPassword(entry)

    def emailget(entry):
        emailVerification(entry)
        regWindow.destroy()
        returnEmail(entry)

    command = ''

    if text == 'login':
        command = lambda: [loginget(entry.get())]

    if text == 'password':
        command = lambda: [passwordget(entry.get())]

    if text == 'email':
        command = lambda: [emailget(entry.get())]

    regWindow = tk.Toplevel()
    regWindow.title('Ввод данных пльзователя!')
    regWindow.geometry('400x250')

    lbl = Label(regWindow, text=(f'Введите {text}:'), font=("Arial Bold", 14))
    lbl.pack()

    entry = Entry(regWindow, width=30)
    entry.pack()

    btn = Button(regWindow, text='Ok!', width=10,
                           height=1, command=command)
    btn.pack()

    regWindow.transient()
    regWindow.grab_set()
    regWindow.focus_set()
    regWindow.wait_window()
    regWindow.mainloop()

def returnlogin(login):
    global loging
    loging = login
    regWindow('password')

def returnPassword(password):
    global passwordg
    passwordg = password
    regWindow('email')

def returnEmail(email):
    global emailg
    emailg = email
    registration(loging, passwordg, emailg)
# Регистрация user и вывод на экран сообщения об успешной регистрации и данных
def registration(login, password, email):
    userData = {'login': login, 'password': password, 'eMail': email}
    putUser(userData)
    text = (f' {login}, успешная регистрация,\nдетали регистрации: \nlogin: {login}, password: {password}, eMail: {email}')
    successfulRegistration('Успешная регистрация!',text, None)

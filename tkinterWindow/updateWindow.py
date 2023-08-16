import tkinter as tk
from tkinter import Label, Entry, Button, IntVar, Radiobutton
from action.checks import emailVerification, passwordVerification, loginVerification
from database.sqliteUser import getUser, getRole, updateUser
from tkinterWindow.notificationWindow import successfulRegistration


def updateWindow(user_id, role_admin, window):

    def loginUpdate(login):
        lbl = Label(updateWindow, text=f'Текущий login: {login}\nВведите новый login: ', font=("Arial Bold", 10))
        lbl.pack()

        entry = Entry(updateWindow, width=30)
        entry.pack()
        login = entry.get()

        btn = Button(updateWindow, text='Проверить!', width=10,
                     height=1,
                     command=lambda: [loginVerification(entry.get()), returnLogin(login, entry.get()),
                                      change(btn, entry.get())])
        btn.pack()

    def returnLogin(login, entry):
        global loging
        if entry is None:
            loging = login
        loging = entry

    def passwordUpdate(password):
        lbl = Label(updateWindow, text=f'Текущий password: {password}\n Введите новый password: ',
                    font=("Arial Bold", 10))
        lbl.pack()

        entry = Entry(updateWindow, width=30)
        entry.pack()

        btn = Button(updateWindow, text='Проверить!', width=10, height=1,
                     command=lambda: [passwordVerification(entry.get()), returnPassword(password, entry.get()),
                                      change(btn, entry.get())])
        btn.pack()

    def returnPassword(password, entry):
        global passwordg
        if entry is None:
            passwordg = password
        passwordg = entry

    def emailUpdate(email):

        lbl = Label(updateWindow, text=f'Текущий eMail: {email}\nВведите новый eMail:', font=("Arial Bold", 10))
        lbl.pack()

        entry = Entry(updateWindow, width=30)
        entry.pack()

        btn = Button(updateWindow, text='Проверить!', width=10,
                     height=1,
                     command=lambda: [emailVerification(entry.get()), returnEmail(email, entry.get()),
                                      change(btn, entry.get())])
        btn.pack()

    def returnEmail(email, entery):
        global emailg
        if entery is None:
            emailg = email
        emailg = entery

    def roleUpdate(role):
        lbl = Label(updateWindow, text=f'Текущая роль: {role}\nВыберите новую роль: ', font=("Arial Bold", 10))
        lbl.pack()

        def returnRole(entry):
            global roleg, roleW
            roleg = entry
            if entry == 1:
                roleW = "Admin"
            if entry == 2:
                roleW = "Customer"
            if entry == 3:
                roleW = "Manager"

        def rolechange(role_id, rolevar):
            if rolevar.get() == 0:
                entry = role_id
            elif rolevar.get() == 1:
                entry = 1
            elif rolevar.get() == 2:
                entry = 2
            elif rolevar.get() == 3:
                entry = 3
            returnRole(entry)

        rolevar = IntVar()
        rolevar.set(0)
        roleA = Radiobutton(updateWindow, text='Admin',
                            variable=rolevar, value=1)
        rileC = Radiobutton(updateWindow, text='Customer',
                            variable=rolevar, value=2)
        roleM = Radiobutton(updateWindow, text='Manager',
                            variable=rolevar, value=3)

        btn = Button(updateWindow, text='Подтвердить новую роль!', width=20,
                     height=1,
                     command=lambda: [rolechange(role_id, rolevar), change(btn, roleW)])
        roleA.pack()
        rileC.pack()
        roleM.pack()
        btn.pack()

    def change(btn, text):
        btn['text'] = f"{text}"
        # btn['bg'] = '#000000'
        # btn['activebackground'] = '#000000'
        # btn['fg'] = '#ffffff'
        # btn['activeforeground'] = '#ffffff'
        btn['state'] = tk.DISABLED

    window.destroy()
    records = getUser('user_id', user_id)

    for row in records:
        user_id = row[0]
        login = row[1]
        password = row[2]
        email = row[3]
        role = row[4]

    recordRole = getRole()
    for row in recordRole:
        if role == row[1]:
            role_id = row[0]

    global loging, passwordg, emailg, roleg, roleW
    loging = login
    passwordg = password
    emailg = email
    roleg = role_id
    roleW = role

    updateWindow = tk.Toplevel()
    updateWindow.title('Update User!')
    # updateWindow.geometry('700x500')

    lbl = Label(updateWindow, text=f'      Изменение данных пользователя {login}      ',
                font=("Arial Bold", 14))
    lbl.pack()

    loginUpdate(login)
    passwordUpdate(password)
    emailUpdate(email)
    if role_admin == 'admin':
        roleUpdate(role)

    lbl = Label(updateWindow)
    lbl.pack()

    btn = Button(updateWindow, text='Сохранить изменения', width=20, height=1,
                 command=lambda: [updateUser(user_id, loging, passwordg, emailg, roleg),
                                  successfulRegistration('Изменение данных',(f'Профиль успешно изменен,'
                                                        f'\nновые данные:\nlogin: {loging}, '
                                                        f'password: {passwordg}, eMail: {emailg}, role: {roleW}'),
                                                         updateWindow)])

    btn.pack()

    lbl = Label(updateWindow)
    lbl.pack()

    btn = Button(updateWindow, text='Выход!', width=20, height=1, command=updateWindow.destroy)
    btn.pack()

    lbl = Label(updateWindow)
    lbl.pack()

    updateWindow.transient()
    updateWindow.grab_set()
    updateWindow.focus_set()
    updateWindow.wait_window()
    updateWindow.mainloop()

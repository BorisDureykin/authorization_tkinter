import re
from database.sqliteUser import *
from tkinterWindow.notificationWindow import errorWindow

# проверка наличия введенного значения в БД
def isUserInDb(variable, inputString):
    records = getUser(variable, inputString)
    for row in records:
        if row[1] == inputString or row[3] == inputString:
            return records
        return False

def loginVerification(entry):

        if re.match("[a-zA-Z0-9а-яА-Я]+", entry) is None:
            errorWindow('Login is not valid')

        if isUserInDb('login', entry):
            errorWindow(f'User {entry} already is is exists. Try again.')

def passwordVerification(entry):

        if re.match("[a-zA-Z0-9а-яА-Я]{6}", entry) is None:
            errorWindow('Password is not valid')

def emailVerification(entry):

        if re.fullmatch("[a-zA-Z0-9]+[-]?[a-zA-Z0-9]+[.]?[a-zA-Z0-9]+[@]{1}[a-zA-Z0-9]+[-]?["
                        "a-zA-Z0-9]+[.]{1}[a-zA-Z]{2,4}", entry) is None:
            errorWindow('E-Mail is not valid')

        if isUserInDb('eMail', entry):
            errorWindow(f'E-Mail {entry} already is is exists. Try again.')



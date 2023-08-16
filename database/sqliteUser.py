import sqlite3

def openConnect():
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    return conn, cur

def closeConnect(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

def clearDatabase():
    conn, cur = openConnect()
    cur.execute('DROP TABLE users_role')
    cur.execute('DROP TABLE role')
    cur.execute('DROP TABLE users')
    cur.execute('CREATE TABLE IF NOT EXISTS users  ('
                'user_id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'login text NOT NUlL UNIQUE, '
                'password text NOT NULL, '
                'eMail text NOT NULL UNIQUE'
                ')')
    cur.execute(f'INSERT INTO users '
                f'(login, password, eMail) '
                f'VALUES '
                f'(?, ?, ?)',
                ('admin',
                 'admin1234',
                 'admin@email.ru')
                )

    cur.execute('CREATE TABLE IF NOT EXISTS role ('
                'role_id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'name_role text NOT NULL UNIQUE'
                ')')
    cur.execute('INSERT INTO role '
                '(name_role) '
                'VALUES ("admin"), ("customer"), ("manager");')

    cur.execute('CREATE TABLE IF NOT EXISTS users_role('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'role_id INTEGER REFERENCES role(role_id) DEFAULT 2, '
                'user_id INTEGER, '
                'FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE) '
                )
    cur.execute('INSERT INTO users_role('
                'user_id, role_id) '
                'VALUES (?, ?)',
                (1, 1))

    closeConnect(conn, cur)

def putUser(user):
    conn, cur = openConnect()
    cur.execute(f'INSERT INTO users '
                f'(login, password, eMail) '
                f'VALUES '
                f'(?, ?, ?)',
                (user['login'],
                 user['password'],
                 user['eMail'])
                )
    conn.commit()

    cur.execute('SELECT user_id '
                'FROM users '
                'WHERE login=? ',[user['login']]
                )
    user_id = cur.fetchone()

    cur.execute('INSERT INTO users_role '
                '(user_id) '
                'VALUES (?)',
                (user_id)
                )
    closeConnect(conn, cur)

def getUserAll():
    conn, cur = openConnect()
    cur.execute("SELECT users.user_id, users.login, users.password, users.email, role.name_role "
                "FROM users "
                "JOIN users_role "
                "ON users.user_id = users_role.user_id "
                "JOIN role "
                "ON users_role.role_id = role.role_id")
    users = cur.fetchall()
    closeConnect(conn, cur)
    return users

def getUser(column, inputString):
    conn, cur = openConnect()

    cur.execute(f"SELECT users.user_id, users.login, users.password, users.email, role.name_role "
                f"FROM users "
                f"JOIN users_role "
                f"ON users.user_id = users_role.user_id "
                f"JOIN role "
                f"ON users_role.role_id = role.role_id "
                f"WHERE users.{column}=? ",[inputString])

    user = cur.fetchall()
    closeConnect(conn, cur)
    return user

def getRole():
    conn, cur = openConnect()

    cur.execute(f"SELECT * "
                f"FROM role ")


    role = cur.fetchall()
    closeConnect(conn, cur)
    return role

def updateUser(user_id, login, password, email, role_id):
    conn, cur = openConnect()
    cur.execute(f"UPDATE users SET login = ?, "
                                 f"password = ?, "
                                 f"eMail = ?  "
                f"WHERE user_id= ? ", ((login), (password), (email), (user_id)))
    cur.execute(f"UPDATE users_role SET role_id = ? "
                f"WHERE user_id=?  AND user_id != '1'", ((role_id), (user_id)))
    closeConnect(conn, cur)

def deleteUser(inputString):
    conn, cur = openConnect()
    cur.execute(f"DELETE "
                f"FROM users "
                f"WHERE user_id = ? "
                f"AND user_id != '1'", [inputString])
    conn.commit()
    cur.execute(f"DELETE "
                f"FROM users_role "
                f"WHERE user_id = ? "
                f"AND user_id != '1'", [inputString])

    closeConnect(conn, cur)

import sqlite3
import getpass

def verifica_credenciales(username, password) -> bool:
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}' "

    rows = cursor.execute(query)
    data = rows.fetchone()
    cursor.close()
    conn.close()

    if data == None:
        return False
    else:
        return True

def crear_usuario(id, username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = '''INSERT INTO users(id, username, password) VALUES (?,?,?)'''

    rows = cursor.execute(query, (id,username,password))
    print(type(rows))

    conn.commit()
    cursor.close()
    conn.close()

def main():
    crear_usuario(3, 'pepe', 'abc')

def main2():

    username = input('Nombre de usuario: ')
    password = getpass.getpass('Contraseña: ')

    if verifica_credenciales(username, password):
        print('Login correcto')
    else:
        print('Login incorrecto')



if __name__ == '__main__':
    main()

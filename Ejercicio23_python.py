import sqlite3




def crear_alumno(id, nombre, apellido):
    conn = sqlite3.connect('escuela.db')
    cursor = conn.cursor()

    query = '''INSERT INTO alumnos(id, nombre, apellido) VALUES (?,?,?)'''

    rows = cursor.execute(query, (id,nombre,apellido))

    conn.commit()
    cursor.close()
    conn.close()

def  crear_tabla():
    conn = sqlite3.connect('escuela.db')
    cursor = conn.cursor()

    query = '''CREATE TABLE alumnos(id PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL);'''

    rows = cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()

def buscar_alumno(nombre, apellido):
    conn = sqlite3.connect('escuela.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM alumnos WHERE nombre = '{nombre}' AND apellido = '{apellido}' "

    rows = cursor.execute(query)
    data = rows.fetchone()
    print(data, '\n')
    cursor.close()
    conn.close()

def mostrar_todos():
    conn = sqlite3.connect('escuela.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM alumnos "

    rows = cursor.execute(query)
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

def main():
    crear_tabla()
    crear_alumno(1, 'Juan', 'Ramón')
    crear_alumno(2, 'Pablo', 'Ruiz')
    crear_alumno(3, 'Marta', 'Jimenez')
    crear_alumno(4, 'Sandra', 'Nuñez')
    crear_alumno(5, 'Manuel', 'Sanchez')
    crear_alumno(6, 'M.', 'Joy')
    crear_alumno(7, 'José', 'Larraz')
    crear_alumno(8, 'Francisco', 'Muñez')

    print('Busqueda individual: ')
    buscar_alumno('Juan', 'Ramón')

    print('Mostrar todos los registros: ')
    mostrar_todos()

if __name__ == '__main__':
    main()

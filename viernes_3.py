import sqlite3

db = sqlite3.connect('invernadero.db')
c = db.cursor()

def insertar(lista):
    c.execute("INSERT INTO usuario(nombre, \
    apellido1, apellido2, correo, password, \
    tipo) VALUES(?,?,?,?,?,?)", (lista[0], \
    lista[1], lista[2], lista[3], lista[4],
    lista[5]))

    db.commit()

def mostar():
    c.execute("SELECT * FROM usuario")
    for e in c:
        print(e)

insertar( ['michel2', 'd2', 'b2', 'a@yahoo.com', '1234', 0] )
mostar()
db.close()

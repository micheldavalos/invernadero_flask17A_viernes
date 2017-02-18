import sqlite3

class administrador():
    db = sqlite3.connect('invernadero.db')
    c = db.cursor()

    def insertar(self, lista):
        self.c.execute("INSERT INTO usuario(nombre, \
        apellido1, apellido2, correo, password, \
        tipo) VALUES(?,?,?,?,?,?)", (lista[0], \
        lista[1], lista[2], lista[3], lista[4],
        lista[5]))

        self.db.commit()

    def mostrar(self):
        self.c.execute("SELECT * FROM usuario")
        lista = []
        for e in self.c:
            usuario = {'id': e[0],
                       'nombre': e[1],
                       'apellido1': e[2],
                       'apellido2': e[3],
                       'correo': e[4],
                       'password': e[5],
                       'tipo': e[6]
                       }
            lista.append(usuario)

        return lista


# insertar( ['michel2', 'd2', 'b2', 'a@yahoo.com', '1234', 0] )
# mostar()
# db.close()

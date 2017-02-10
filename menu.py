from viernes_3 import administrador

class menu():
    def __init__(self):
        admin = administrador()

        while True:
            print("1) Inserta Usuario")
            print("2) Mostrar")
            print("0) Salir")
            op = input()

            if op == '1':
                lista = self.menu_usuario()
                admin.insertar(lista)

            elif op == '2':
                admin.mostrar()
            elif op == '0':
                break
    def menu_usuario(self):
        nombre = input("Nombre: ")
        apellido1 = input("Apellido: ")
        apellido2 = input("Apellido 2: ")
        correo = input("Correo: ")
        password = input("Password: ")
        tipo = input("Tipo: ")
        tipo = int(tipo)
        return [nombre, apellido1, apellido2, correo, password, tipo]

m = menu()
print(m.menu_usuario())

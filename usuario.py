#!python3
# Proyecto final del recorrido del programador

from db import Database

class Usuario():
    """ Modulo para la creacion de los usuarios del E-Commerce"""

    def __init__(self, email, nombre, apellido, clave):
        self.email = email
        self.nombre = nombre
        self.apellido = apellido
        self.clave = clave

    # Getters y setter para los atributos del usuario
    def get_email(self):
        query = Database.consultar_usuario()
        return self.email

    def set_email(self, email):
        self.email = email

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_clave(self, clave):
        pass

    def login(self, email, clave):
        """ Metodo para registrarse en el sistema. """
        usuario = Database.validar_usuario(email, clave)
        if usuario:
            return True
        else:
            return False
    
    def get_user(self):
        result = Database.consultar_usuario_id()
        print(result)
        return result
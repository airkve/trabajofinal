#!python3
# Proyecto final del recorrido del programador

class Usuario():
    """ Modulo para la creacion de los usuarios del E-Commerce"""

    def __init__(self, documento, nombre, apellido, clave):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.clave = clave

    # Getters y setter para los atributos del usuario
    def get_documento(self):
        return self.documento

    def set_documento(self, dni):
        self.documento = documento

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
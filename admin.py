#!python3
# Proyecto final del recorrido del programador

from usuario import Usuario
from db import Database

class Administrador(Usuario, Database):
    """ Modulo que define los atributos y metodos del administrador. """

    def __init__(self, email, nombre, apellido, clave, rights):
        super().__init__(email, nombre, apellido, clave)
        self.rights = rights
        self.usuario_id = Database.consultar_usuario()
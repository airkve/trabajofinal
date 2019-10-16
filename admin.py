#!python3
# Proyecto final del recorrido del programador

from usuario import Usuario
from db import Database

class Administrador(Usuario, Database):
    """ Modulo que define los atributos y metodos del administrador. """

    def __init__(self, documento, nombre, apellido, clave):
        super().__init__(documento, nombre, apellido, clave)
        self.usuario_id = Database.consultar_usuario(documento)

        def adm_login(self, pswd):
            if pswd = Database.consultar_usuario()
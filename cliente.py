#!python3
# Modulo de cliente

from usuario import Usuario
from db import Database
from venta import Venta

class Cliente(Usuario, Database, Venta):
    """ Modulo que define los atributos y metodos del cliente. """

    def __init__(self, email, nombre, apellido, clave, dni, telefono, direccion, altura, cod_postal, ciudad, prov, pais):
        super().__init__(email, nombre, apellido, clave)
        self.dni = dni
        self.telefono = telefono
        self.direccion = direccion
        self.altura = altura
        self.cod_postal = cod_postal
        self.ciudad = ciudad
        self.provincia = prov
        self.pais = pais
        self.historico_compras = []

    def set_dni(self, dni):
        self.dni = dni
    
    def get_dni(self):
        return self.dni

    def set_telefono(self, tlf):
        self.telefono = tlf

    def get_telefono(self):
        return self.telefono

    def set_direccion(self, direccion):
        self.direccion = direccion
    
    def get_direccion(self):
        return self.direccion

    def set_altura(self, altura):
        self.altura = altura
    
    def get_altura(self):
        return self.altura

    def set_codpostal(self, cod):
        self.cod_postal = cod
    
    def get_codpostal(self):
        return self.cod_postal

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad
    
    def get_ciudad(self):
        return self.ciudad

    def set_provincia(self, prov):
        self.provincia = prov
    
    def get_provincia(self):
        return self.provincia

    def set_pais(self, pais):
        self.pais = pais
    
    def get_pais(self):
        return self.pais

    def login(self, user_data):
        account = Database.validar_usuario(user_data)

    def comprar(self, buy_info):

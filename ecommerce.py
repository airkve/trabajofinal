#!pyhton3
# Modulo principal del E-Commerce

from cliente import Cliente
from db import Database
from producto import Producto

class Ecommerce(Producto, Cliente):
    """ Modulo que controla las funciones de la tienda. """

    def __init__(self, nombre, descripcion, marca, categoria, precio):
        Producto.__init__(self, nombre, descripcion, marca, categoria, precio)
        Cliente.__init__(self, )

    def get_nombre(self):
        return self.nombre
        
    def set_nombre(self, nombre):
        self.nombre = nombre

    def venta(self):

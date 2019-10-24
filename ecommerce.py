# Modulo principal del E-Commerce

from db import *
import datetime as dt

class Ecommerce():
    """ Modulo que controla las funciones de la tienda. """

    def __init__(self, nombre):
        self.nombre = nombre
        self.db = Database()
        self.fecha_hoy = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.lista_clientes = []
        self.lista_productos = []

    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre

    def venta(self, cliente, producto, cantidad):
        # envia la factura de compra al cliente y resta la cantidad de la base de datos
        fecha_compra = self.fecha_hoy
        comprador = (cliente.get_nombre(), cliente.get_apellido(), cliente.get_telefono(), cliente.get_email())
        item = producto.get_nombre()
        cant = producto.get_cantidad()
        precio_final = producto.get_precio() * cant
        direccion = cliente.direccion()
        print(fecha_compra, comprador, item, cant, precio_final, direccion)

def menu(self, nombre):
    print()

if __name__ == "__main__":
    db = Database()
    mi_tienda = Ecommerce()
    

#!pyhton3
# Modulo principal del E-Commerce

from cliente import Cliente
from producto import Producto
import datetime as dt

class Ecommerce():
    """ Modulo que controla las funciones de la tienda. """

    def __init__(self):
        self.fecha_hoy = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_nombre(self):
        return self.nombre
        
    def set_nombre(self, nombre):
        self.nombre = nombre

    def venta(self, cliente_id, producto_id, cantidad):
        # envia la factura de compra al cliente y resta la cantidad de la base de datos
        fecha_compra = self.fecha_hoy
        comprador = Cliente.get_data_comprador(cliente_id)
        item = Producto.get_producto(producto_id)
        cant = cantidad
        precio_final = item[3] * cant
        direccion = comprador[4]
        print(fecha_compra, comprador, item, cant, precio_final, direccion)


prueba = Ecommerce()
#ric = Cliente('Richard', 'Jimenez', '95806829', 'ricjim@gmail.com', 'Jeronimo Salguero 1964')
prueba.venta(1, 5, 2)
        

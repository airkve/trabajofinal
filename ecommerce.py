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
        self.lista_productos = self.db.consultar_lista_productos()

    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre

    def set_lst_clientes(self, clientes):
        for cliente in clientes:
            self.lista_clientes.append(list(Cliente(*cliente)))

    def set_lst_productos(self, productos):
        for producto in productos:
            self.lista_productos.append(list(Producto(*producto)))

    def carrito_de_compras(self):
        productos_carrito = []

    def venta(self, cliente, producto, cantidad):
        # envia la factura de compra al cliente y resta la cantidad de la base de datos
        fecha_compra = self.fecha_hoy
        comprador = (cliente.get_nombre(), cliente.get_apellido(), cliente.get_telefono(), cliente.get_email())
        item = producto.get_nombre()
        cant = producto.get_cantidad()
        precio_final = producto.get_precio() * cant
        direccion = cliente.direccion()
        print(fecha_compra, comprador, item, cant, precio_final, direccion)

    def listar_clientes(self, lst):
        for producto in lst:
            pass


def print_menu(nombre):       # Your menu design here
        print('{:-^60}'.format('Menú principal - ' + nombre))
        print("1. Tienda ")
        print("2. Historial de compras ")
        print("3. Salir ")
        print(60 * "-")

def print_menu_tienda(nombre, items):       # Your menu design here
        print('{:-^60}'.format('Tienda - ' + nombre))
        print('{:>3} {:<33} {:<40.40} {:^9} {:>20} {:>10} {:>4}'.format('ID', 'Producto', 'Descripcion', 'Precio', 'Categoria', 'Marca', 'Cant'))
        for item in items:
            temp = [
                item.get_id(),
                item.get_nombre(),
                item.get_descripcion(),
                item.get_precio(),
                item.get_categoria(),
                item.get_marca(),
                item.get_cantidad(),
            ]
            print('{:>3} {:<33} {:<40.40} {:>09,.2f} {:>20} {:>10} {:>4d}'.format(item.get_id(), item.get_nombre(), item.get_descripcion(), item.get_precio(), item.get_categoria(), item.get_marca(), item.get_cantidad()))
        print(60 * "-")
        print("1. Buscar por nombre")
        print("2. Buscar por categoria ")
        print("3. Carrito de compras ")
        print("4. Regresar ")
        print(60 * "-")

def print_menu_carrito(nombre):       # Your menu design here
        print('{:-^60}'.format('Carrito de compras - ' + nombre))
        print("1. Buscar por nombre")
        print("2. Buscar por categoria ")
        print("3. Carrito de compras ")
        print("4. Regresar ")
        print(60 * "-")



if __name__ == "__main__":
    db = Database()
    mi_tienda = Ecommerce("Mercado Caro")
    print_menu(mi_tienda.get_nombre())
    #i = db.consultar_lista_productos()
    #mi_tienda.set_lst_productos(i)
    print_menu_tienda(mi_tienda.get_nombre(), mi_tienda.lista_productos)
    # while True:
    #     respuesta = input('Ingresa tu opción: ')
    #     if respuesta == '1':
    #         print_menu_tienda()
    

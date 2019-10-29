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
        """ Ejecuta el proceso de compra de un cliente. """



    def listar_clientes(self, lst):
        for producto in lst:
            pass


def login(nombre):
    print('{:-^60}'.format('Menú de ingreso. - ' + nombre))
    email = input('Ingresa tu E-Mail: ')
    psw = input('Ingresa tu clave: ')
    return email, psw

def print_menu(nombre):       # Your menu design here
    print('{:-^60}'.format('Menú principal. - ' + nombre))
    print("A. Tienda ")
    print("B. Historial de compras ")
    print("C. Salir ")
    print(60 * "-")

def print_menu_tienda(nombre, items):       # Your menu design here
    print('{:-^60}'.format('Catálogo. - ' + nombre))
    print('{:>3} {:<33} {:<40.40} {:^9} {:>20} {:>10} {:>4}'.format('ID', 'Producto', 'Descripcion', 'Precio', 'Categoria', 'Marca', 'Cant'))
    for item in items:
        print('{:>3} {:<33} {:<40.40} {:>09,.2f} {:>20} {:>10} {:>4d}'.format(*item))
    print(60 * "-")
    print('Selecciona el numero del producto y despues la opcion.')
    print("A. Comprar.")
    print("B. Cancelar la selección ")
    print("C. Regresar ")
    print(60 * "-")

def print_menu_carrito(nombre):       # Your menu design here
    print('{:-^60}'.format('Carrito de compras - ' + nombre))
    print("1. Buscar por nombre")
    print("2. Buscar por categoria ")
    print("3. Carrito de compras ")
    print("4. Regresar ")
    print(60 * "-")



if __name__ == "__main__":
    datab = Database()
    mi_tienda = Ecommerce("Mercado Caro")
    credenciales = login(mi_tienda.get_nombre())
    if datab.validar_usuario(credenciales):
        while True:
            print_menu(mi_tienda.get_nombre())
            opcion = input('')
            
            print_menu_tienda(mi_tienda.get_nombre(), datab.consultar_lista_productos())
            # while True:
            #     respuesta = input('Ingresa tu opción: ')
            #     if respuesta == '1':
            #         print_menu_tienda()
    else:
        print("Usuario o clave incorrectos.")
    

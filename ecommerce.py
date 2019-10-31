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

    def get_cliente(self, credenciales):
        cliente = self.db.consultar_usuario_por_email(credenciales)
        return Cliente(*cliente)

    def buscar_producto(self, producto_id):
        for producto in self.lista_productos:
            if producto_id == str(producto[0]):
                return Producto(*producto)

    def buscar_compras_cliente(self, comprador):
        compras = self.db.consultar_compras(comprador)
        return compras

    def carrito_de_compras(self, producto):
        carrito = []
        carrito.append(producto)
        return carrito

    def venta(self, cliente, producto, cantidad):
        """ Ejecuta el proceso de compra de un cliente. """

        nueva_cant = producto.get_cantidad() - cantidad
        precio_total = producto.get_precio() * cantidad
        data_de_compra = (cliente.get_user_id(), str(self.fecha_hoy), int(producto.get_id()), int(cantidad), float(precio_total))
        data_de_cantidad = (nueva_cant, producto.get_id())
        try:
            self.db.crear_compra(data_de_compra)
            self.db.modificar_producto_cantidad(data_de_cantidad)
        except Error as e:
            print('Ocurrió un error tratando de registrar la compra.', e)
        else:
            print('Operación exitosa.')
        

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

def print_catalogo(nombre, items):       # Your menu design here
    print('{:-^60}'.format('Catálogo. - ' + nombre))
    print('{:>3} {:<33} {:<40.40} {:^9} {:>20} {:>10} {:>4}'.format('ID', 'Producto', 'Descripcion', 'Precio', 'Categoria', 'Marca', 'Cant'))
    for item in items:
        print('{:>3} {:<33} {:<40.40} {:>09,.2f} {:>20} {:>10} {:>4d}'.format(*item))
    print(60 * "-")
    print("A. Comprar.")
    print("B. Regresar ")
    print(60 * "-")

def print_menu_carrito(nombre):       # Your menu design here
    print('{:-^60}'.format('Carrito de compras - ' + nombre))
    print("1. Buscar por nombre")
    print("2. Buscar por categoria ")
    print("3. Carrito de compras ")
    print("4. Regresar ")
    print(60 * "-")



if __name__ == "__main__":
    mi_tienda = Ecommerce("Mercado Caro") # se instancia la tienda
    mc = mi_tienda.get_nombre() # se guarda el nombre de la tienda
    catalogo = mi_tienda.lista_productos # se crea una lista con los productos de la tienda
    credenciales = login(mc) # se ejecuta la funcion para registrarse en el sistema
    if mi_tienda.db.validar_usuario(credenciales): # se valida el usario con email y clave
        cliente = mi_tienda.get_cliente(credenciales[0]) # guarda el cliente en una variable
        while True:
            print_menu(mc)
            opcion = input('>')
            if opcion.lower() == 'a':
                print_catalogo(mc, catalogo)
                compra = input('>')
                if compra.lower() == 'a':
                    item = input('Ingresa el ID del producto: ')
                    cant = int(input('Cantidad: '))
                    confirmacion = input('Deseas realizar la compra? S/N: ')
                    if confirmacion.lower() == 's':
                        producto_seleccionado = mi_tienda.buscar_producto(item)
                        mi_tienda.venta(cliente, producto_seleccionado, cant)
                    else:
                        print_catalogo(mc, catalogo)
                elif compra.lower() == 'b':
                    print('Hasta luego.')
                    break
            elif opcion.lower() == 'b':
                print(mi_tienda.buscar_compras_cliente(cliente))
            elif opcion.lower() == 'c':
                break
            
            #print_menu_tienda(mi_tienda.get_nombre(), db.consultar_lista_productos())
            # while True:
            #     respuesta = input('Ingresa tu opción: ')
            #     if respuesta == '1':
            #         print_menu_tienda()
    else:
        print("Usuario o clave incorrectos.")
    

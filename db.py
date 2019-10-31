import mysql.connector
from dbdata import dbconf, queries
from mysql.connector import Error
from mysql.connector import errorcode
from cliente import Cliente
from producto import Producto
from venta import Venta
from factura import Factura

class Database():
    """ Clase para consultar, modificar y conectarse a la base de datos. """
  
    def __init__(self):
        self.conexion = mysql.connector.connect(**dbconf)
        self.cursor = self.conexion.cursor()
        
    def crear_usuario(self, cliente):
        """ Crea un usuario en la DB usando:
        dni, nombre, apellido, email, telefono,
        clave, direccion y ciudad_id. """

        self.cursor.execute(queries['get_user_dni'], (cliente.get_dni(),))
        consulta = self.cursor.fetchone()
        if consulta:
            print('El usuario ya existe.')
        else:
            user = [
                cliente.get_dni(),
                cliente.get_nombre(),
                cliente.get_apellido(),
                cliente.get_email(),
                cliente.get_telefono(),
                cliente.get_clave(),
                cliente.get_direccion(),
                cliente.get_ciudad()
            ]
            print(user)
            try:
                self.cursor.execute(queries['add_user'], (*user,))
            except Error as e:
                print('Hubo un problema al registrar los datos en la DB.', e)
            else:
                # registra los cambios a la base de datos
                self.conexion.commit()
                print('Se registraron los datos con exito.')

    def eliminar_usuario(self, usuario_dni):
        """ Elimina a un usuario en la db usando su dni. """

        # archiva el DNI del usuario para multiple usos
        dni = usuario_dni.get_dni()
        # valida si existe el usuario en la db
        self.cursor.execute(queries['get_user_dni'], (dni,))
        consulta = self.cursor.fetchone()
        if consulta:
            try:
                self.cursor.execute(queries['del_user_by_dni'], (dni,))
            except Error as e:
                print('No existe alguien con ese codigo de usuario.', e)
            else:
                # registra los cambios a la base de datos
                self.conexion.commit()
                print('Usuario eliminado.')
        else:
            print('No existe un usuario con ese DNI.')
        
    def consultar_usuario_por_email(self, usuario):
        """ Busca a un usuario en la db por su email. """

        try:
            self.cursor.execute(queries['get_user_by_email'], (usuario,))
        except Error as e:
            print('No existe alguien con ese E-Mail.', e)
        else:
            consulta = self.cursor.fetchone()
        # envia el reporte en caso de que exista el email
        return consulta
    
    def consultar_usuario_por_dni(self, usuario):
        """ Busca un usuario en la DB utilizando su DNI. """

        try:
            self.cursor.execute(queries['get_user_by_dni'], (usuario.get_dni(),))
        except Error as e:
            print('No se encontró el usuario con ese DNI.', e)
        else:
            # archiva en una variable los resultados del query
            consulta = self.cursor.fetchone()
            # retorna la data del query
            return consulta

    def consultar_usuario_clave(self, usuario):
        """ Busca la clave de un usuario en la DB. """

        self.cursor.execute(queries['get_user_by_pswd'], (usuario.get_clave(),))
        consulta = self.cursor.fetchone()
        return consulta

    def consultar_clientes(self):
        """ Busca la lista de clientes en la DB. """

        self.cursor.execute(queries['get_clients'])
        consulta = self.cursor.fetchall()
        return consulta


    def validar_usuario(self, data):
        """ Busca el email y la clave de un usuario en la DB para validar login. """

        try:
            self.cursor.execute(queries['validate_user'], data)
        except Error as e:
            print('El usuario o la contraseña no coinciden.', e)
        else:
            # guarda la consulta en una variable
            result = self.cursor.fetchone()
            return result

    # Metodos para los poductos
    def eliminar_producto(self, producto):
        """ Elimina un producto en la DB por su ID. """

        # elimina un producto de la base de datos
        try:
            self.cursor.execute(queries['del_producto'], (producto.get_id(),))
        except Error as e:
            print('No existe un producto con ese ID.')
        else:
            # registra los cambios a la base de datos
            self.conexion.commit()

    def cargar_producto(self, producto):
        """ Crea un producto nuevo en la DB. """

        item = [
            self.producto.get_id(),
            self.producto.get_nombre(),
            self.producto.get_descriptcion(),
            self.producto.get_marca(),
            self.producto.get_categoria(),
            self.producto.get_precio(),
            self.producto.get_cantidad()
        ]
        # inserta un producto en la base de datos
        try:
            self.cursor.execute(queries['add_product'], producto)
        except Error as e:
            print('No existe producto con ese ID.')
        else:
            # registra los cambios a la base de datos
            self.conexion.commit()
    
    def modificar_producto_cantidad(self, data):
        """ Modifica la cantidad de un producto en la DB. """

        try:
            self.cursor.execute(queries['mod_product_cant'], data)
        except Error as e:
            print('Ocurrió un problema al tratar de ejecutar la operación.', e)
        else:
            # registra los cambios a la base de datos
            self.conexion.commit()
            #print('Cambio exitoso {}.'.format(producto))

    def consultar_producto_id(self, producto):
        try:
            self.cursor.execute(queries['get_product_by_id'], (producto,))
        except Error as e:
            print('No se encontró el producto.', e)
        else:
            consulta = self.cursor.fetchone()
            # retorna el resultado de la busqued
            return consulta

    def consultar_lista_productos(self):
        """ Busca toda la lista de productos en la DB. """
        
        try:
            self.cursor.execute(queries['get_products'])
        except Error as e:
            print('Ocurrió un error al hacer la consulta.', e)
        else:
            # guarda la consulta en una variable
            consulta = self.cursor.fetchall()
            return consulta

    def crear_compra(self, shop_data):
        """ Registra las compras del cliente en la DB. """

        try:
            self.cursor.execute(queries['new_shopping'], shop_data)
        except Error as e:
            print("Error al guardar los datos de la compra.", e)
        else:
            #guarda la consulta en una variable
            self.conexion.commit()

    def consultar_compras(self, cliente):
        """ Busca el historial de compras del usuario en ls DB. """

        try:
            self.cursor.execute(queries['get_user_shop_history'], (cliente.get_email(),))
        except Error as e:
            print("Error al consultar el historico", e)
        else:
            #guarda la consulta en una variable
            consulta = self.cursor.fetchall()
            return consulta
        


# prueba = Database()
# data = (5, 18)
# item = (12, '2019-10-29 22:54:17', 13, 1, 25000)
# prueba.crear_compra(item)
# martina = prueba.consultar_usuario_por_email('martg@gmail.com')
# cliente1 = Cliente(*martina)
# result = prueba.consultar_compras(cliente1)
# print(result)
# ric = Cliente(
#     12,
#     95806829,
#     'Richard',
#     'Jimenez',
#     'ricjim@gmail.com',
#     1131592009,
#     'asfñkj',
#     'Jeronimo Salguero 1964 cp1425', 
#     1)
# print(prueba.consultar_compras(ric))
# item = prueba.consultar_producto_id(13)
# print(item)
# tele = Producto(*item)
# print(tele.get_nombre())
# print('El precio del televisor es de {:7,.2f}'.format(tele.get_precio()))
# tele.set_cantidad(tele.get_cantidad() - 1)
# datos = (tele.get_id(), tele.get_cantidad())
# prueba.modificar_producto_cantidad(datos)
# prueba.modificar_producto_cantidad(data)
#prueba.crear_usuario(ric)
#query_table = ('usuarios',)
#prueba.eliminar_usuario(ric)
#print(prueba.validar_usuario(('martg@gmail.com', 'gatonegro')))
#print(prueba.get_clave(4))
#print(prueba.consultar_clientes())
#comprador = prueba.consultar_cliente(5)
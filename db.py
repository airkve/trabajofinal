import mysql.connector
from dbdata import dbconf, queries
from mysql.connector import Error
from mysql.connector import errorcode
from cliente import Cliente
from producto import Producto
from venta import Venta

class Database():
    """ Clase para consultar, modificar y conectarse a la base de datos. """
  
    def __init__(self):
        self.conexion = mysql.connector.connect(**dbconf)
        self.cursor = self.conexion.cursor()
        
    def crear_usuario(self, data_usuario):
        """ Crea un usuario en la DB usando:
        dni, nombre, apellido, email, telefono, clave, direccion y ciudad_id. """

        self.cursor.execute(queries['get_user_dni'], (data_usuario.get_dni(),))
        consulta = self.cursor.fetchone()
        if consulta:
            print('El usuario ya existe.')
        else:
            user = [
                data_usuario.get_dni(),
                data_usuario.get_nombre(),
                data_usuario.get_apellido(),
                data_usuario.get_email(),
                data_usuario.get_telefono(),
                data_usuario.get_clave(),
                data_usuario.get_direccion(),
                data_usuario.get_ciudad()
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
        """ Metodo para eliminar un usuario en la db usando su dni. """

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
        
    # Metodos para los usuarios
    def consultar_usuario_por_email(self, email):
        """ Metodo para buscar un usuario en la db por su email. """

        try:
            self.cursor.execute(queries['get_user_by_email'], (email.get_email(),))
        except Error as e:
            print('No existe alguien con ese E-Mail.', e)
        else:
            consulta = self.cursor.fetchone()
        # envia el reporte en caso de que exista el email
        return consulta
    
    def consultar_usuario_id(self, usuario_id):
        """ Busca el ID de un usuario en la DB. """

        try:
            self.cursor.execute(queries['list_user_id'], (usuario_id,))
        except Error as e:
            print('No se encontró el usuario por el ID.', e)
        else:
            # archiva en una variable los resultados del query
            consulta = self.cursor.fetchone()
            # imprime el reporte
        # retorna la data del query
        return consulta

    def consultar_usuario_clave(self, clave):
        """ Busca la clave de un usuario en la DB. """

        self.cursor.execute(queries['get_user_by_pswd'], (clave,))
        consulta = self.cursor.fetchone()
        return consulta

    def consultar_clientes(self):
        """ Busca la lista de clientes en la DB y la archiva en una lista. """

        clientes = []
        self.cursor.execute(queries['get_clients'])
        consulta = self.cursor.fetchall()
        for line in consulta:
            print(line)
            clientes.append(Cliente(*line))

        return clientes

    def consultar_cliente(self, cliente):
        """ Busca un usuario en la DB utilizando el DNI. """

        try:
            self.cursor.execute(queries['get_client'], (cliente.get_dni(),))
        except Error as e:
            print('Se produjo un error buscando al usuario por su DNI', e)
        else:
            # guarda la consulta en una variable
            consulta = self.cursor.fetchone()
            return Cliente(*consulta)



    def validar_usuario(self, user_data):
        """ Busca el email y la clave de un usuario en la DB para validar login. """

        try:
            self.cursor.execute(queries['validate_user'], user_data)
        except Error as e:
            print('El usuario o la contraseña no coinciden.', e)
        else:
            # guarda la consulta en una variable
            result = self.cursor.fetchone()
            return result

    # Metodos para los poductos
    def eliminar_producto(self, producto_id):
        """ Elimina un producto en la DB por su ID. """

        # elimina un producto de la base de datos
        try:
            self.cursor.execute(queries['del_producto'], (producto_id,))
        except Error as e:
            print('No existe producto con ese ID.')
        else:
            # registra los cambios a la base de datos
            self.conexion.commit()

    def cargar_producto(self, data_producto):
        """ Crea un producto nuevo en la DB. """

        # inserta un producto en la base de datos
        try:
            self.cursor.execute(queries['add_product'], data_producto)
        except Error as e:
            print('No existe producto con ese ID.')
        else:
            # registra los cambios a la base de datos
            self.conexion.commit()
    
    def modificar_producto_cantidad(self, producto):
        """ Modifica la cantidad de un producto en la DB. """

        try:
            self.cursor.execute(queries['mod_product_cant'], (producto))
        except Error as e:
            print('Hay un problema con la cantidad del producto.', e)
        else:
            # registra los cambios a la base de datos
            self.conexion.commit()
            print('Se cambió la cantidad a {}.'.format(producto[1]))

    def consultar_producto_id(self, producto_id):
        try:
            self.cursor.execute(queries['get_product_by_id'], (producto_id,))
        except Error as e:
            print('No se encontró el producto.', e)
        else:
            consulta = self.cursor.fetchone()
            # retorna el resultado de la busqued
            return consulta

    def consultar_lista_productos(self):
        lista_productos = []
        try:
            self.cursor.execute(queries['get_products'])
        except Error as e:
            print('Ocurrió un error al hacer la consulta.', e)
        else:
            # guarda la consulta en una variable
            consulta = self.cursor.fetchall()

        for producto in consulta:
            lista_productos.append(Producto(*producto))
        return lista_productos

    def crear_compras(self, cliente, producto):
        """ Registra en la DB las compras del cliente. """

        try:
            self.cursor.execute(queries['get_user_shop_history'], (cliente.get_dni(),))
        except Error as e:
            print("Error al consultar el historico", e)
        else:
            #guarda la consulta en una variable
            consulta = self.cursor.fetchall()
        # aplica el modelo de Factura a cada linea de la consulta
        for linea in consulta:
            historico.append(Factura(*linea))
        # returna la lista de facturas
        return historico

    def consultar_compras(self, cliente):
        """ Busca el historial de compras del usuario en ls DB. """

        historico = []
        try:
            self.cursor.execute(queries['get_user_shop_history'], (cliente.get_dni(),))
        except Error as e:
            print("Error al consultar el historico", e)
        else:
            #guarda la consulta en una variable
            consulta = self.cursor.fetchall()
        # aplica el modelo de Factura a cada linea de la consulta
        for linea in consulta:
            historico.append(Factura(*linea))
        # returna la lista de facturas
        return historico


# prueba = Database()
# print(prueba.consultar_lista_productos())
# ric = Cliente(
#     95806829,
#     'Richard',
#     'Jimenez',
#     'ricjim@gmail.com',
#     1131592009,
#     'asfñkj',
#     'Jeronimo Salguero',
#     1964,
#     1425, 
#     1, 
#     1, 
#     11)
# item = prueba.consultar_producto_id(13)
# print(item)
# tele = Producto(*item)
# print(tele.get_nombre())
# print('El precio del televisor es de {:7,.2f}'.format(tele.get_precio()))
# tele.set_cantidad(tele.get_cantidad() - 1)
# datos = (tele.get_id(), tele.get_cantidad())
# prueba.modificar_producto_cantidad(datos)
#prueba.modificar_producto_cantidad()
#prueba.crear_usuario(ric)
#query_table = ('usuarios',)
#prueba.eliminar_usuario(ric)
#print(prueba.validar_usuario(('martg@gmail.com', 'gatonegro')))
#print(prueba.get_clave(4))
#print(prueba.consultar_clientes())
#comprador = prueba.consultar_cliente(5)
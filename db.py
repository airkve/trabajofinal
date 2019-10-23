import mysql.connector
from dbdata import dbconf, queries
from mysql.connector import Error
from mysql.connector import errorcode
from cliente import Cliente
from producto import Producto

class Database():
    """ Modulo para consultar, modificar y conectarse a la base de datos. """
  
    def __init__(self):
        self.conexion = mysql.connector.connect(**dbconf)
        self.cursor = self.conexion.cursor()
        
    def crear_usuario(self, data_usuario):
        """ Metodo para crear un usuario en la db, utiliza dni, nombre, apellido, email, telefono y clave. """
        user = Cliente(data_usuario).get_nombre
        try:
            self.cursor.execute(queries['add_user'], data_usuario)
            self.cursor.execute(queries['add_address'], (Cliente.direccion,))
            self.cursor.execute(queries['add_city'], (Cliente.ciudad,))
            self.cursor.execute(queries['add_province'], (Cliente.provincia,))
            self.cursor.execute(queries['add_pais'], (Cliente.pais,))
        except Error as e:
            print('El registro ya existe.')
        else:
            # registra los cambios a la base de datos
            self.conexion.commit()

    def eliminar_usuario(self, usuario):
        """ Metodo para eliminar un usuario en la db usando el id del usuario o su dni. """
        # detecta si el argumento corresponde a un ID o a un DNI
        direccionID = self.cursor.execute(queries['get_address_id'], (Cliente.dni))
        if usuario[0] <= 999:
            try:
                self.cursor.execute(queries['get_address_by_user_id'], (direccionID,))
                self.cursor.execute(queries['del_user_id'], (usuario,))
            except Error as e:
                print('No existe alguien con ese codigo de usuario.')
            else:
                # registra los cambios a la base de datos
                self.conexion.commit()
        else:
            self.cursor.execute(queries['del_user_dni'], (usuario,))
        # registra los cambios a la base de datos
        self.conexion.commit()
        print('Usuario eliminado.')

    def consultar_usuario_por_email(self, email):
        """ Metodo para buscar un usuario en la db por su email. """
        try:
            self.cursor.execute(queries['get_user_by_email'], (email,))
        except Error as e:
            print('No existe alguien con ese E-Mail.', e)
        else:
            consulta = self.cursor.fetchone()
        # envia el reporte en caso de que exista el email
        return consulta
    
    def consultar_usuario_id(self, usuario_id):
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
        self.cursor.execute(queries['get_user_by_pswd'], (clave,))
        consulta = self.cursor.fetchone()
        return consulta

    def consultar_clientes(self):
        clientes = []
        self.cursor.execute(queries['get_clients'])
        consulta = self.cursor.fetchall()
        for line in consulta:
            print(line)
            clientes.append(Cliente(*line))

        return clientes

    def consultar_cliente(self, cliente_id):
        self.cursor.execute(queries['get_client'], (cliente_id,))
        consulta = list(self.cursor.fetchone())
        return Cliente(*consulta)

    def validar_usuario(self, user_data):
        self.cursor.execute(queries['validate_user'], user_data)
        result = self.cursor.fetchone()
        return result

    def eliminar_producto(self, producto_id):
        # elimina un producto de la base de datos
        try:
            self.cursor.execute(queries['del_producto'], (producto_id,))
        except Error as e:
            print('No existe producto con ese ID.')
        else:
            # registra los cambios a la base de datos
            self.conexion.commit()

    def cargar_producto(self, data_producto):
        # inserta un producto en la base de datos
        try:
            self.cursor.execute(queries['add_product'], data_producto)
        except Error as e:
            print('No existe producto con ese ID.')
        else:
            # registra los cambios a la base de datos
            self.conexion.commit()
    
    def modificar_producto_cantidad(self, cantidad):
        # modifica la cantidad de un producto en la base de datos
        try:
            self.cursor.execute(queries['mod_product_cant'], (cantidad,))
        except Error as e:
            print('Hay un problema con la cantidad del producto.')
        else:
            # registra los cambios a la base de datos
            self.conexion.commit()

    def consultar_producto_id(self, producto_id):
        try:
            self.cursor.execute(queries['list_product_id'], (producto_id,))
        except:
            print('No se encontró el producto.')
        else:
            result = self.cursor.fetchone()
        # retorna el resultado de la busqued
        return result


prueba = Database()
#nuevo_usuario = (55555555, 'Jose', 'Reyes', 'jr2000@gmail.com', '1131592009', '123456')
#prueba.crear_usuario(nuevo_usuario)
#query_table = ('usuarios',)
#prueba.eliminar_usuario((95806829,))
#print(prueba.consultar_usuario_id(5))
#print(prueba.validar_usuario(('martg@gmail.com', 'gatonegro')))
#print(prueba.get_clave(4))
#print(prueba.consultar_clientes())
comprador = prueba.consultar_cliente(5)
print
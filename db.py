import mysql.connector
from dbdata import dbconf, queries
from mysql.connector import Error
from mysql.connector import errorcode

class Database():
    """ Modulo para consultar, modificar y conectarse a la base de datos. """
  
    def __init__(self):
        self.conexion = mysql.connector.connect(**dbconf)
        self.cursor = self.conexion.cursor()
        
    def crear_usuario(self, data_usuario):
        """ Metodo para crear un usuario en la db, utiliza dni, nombre, apellido, email, telefono y clave. """
        try:
            self.cursor.execute(queries['add_user'], data_usuario)
        except Error as e:
            print('El registro ya existe.')
        else:
            # registra los cambios a la base de datos
            self.conexion.commit()

    def eliminar_usuario(self, usuario):
        """ Metodo para eliminar un usuario en la db. """
        # detecta si el argumento corresponde a un ID o a un DNI
        if usuario[0] <= 999:
            try:
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
            print('No existe alguien con ese E-Mail.')
        else:
            reporte = self.cursor.fetchone()
        # envia el reporte en caso de que exista el email
        return reporte
    
    def consultar_usuario_por_id_dni(self, usuario):
        # detecta si el argumento corresponde a un ID o a un DNI
        if usuario[0] <= 999:
            try:
                self.cursor.execute(queries['list_user_id'], (usuario,))
            except Error as e:
                print('No se encontró el usuario por el ID.', e)
            else:
                # archiva en una variable los resultados del query
                reporte = self.cursor.fetchall()
                # imprime el reporte
                print(reporte)
        else:
            try:
                self.cursor.execute(queries['list_user_dni'], (usuario,))
            except Error as e:
                print('No se encontró el usuario por su DNI.', e)
            else:
                # archiva en una variable los resultados del query
                reporte = self.cursor.fetchall()
            # imprime el reporte
            print(reporte)

    def consultar_usuario_clave(self, clave):
        self.cursor.execute(queries['get_user_by_pswd'], (clave,))
        usuario = self.cursor.fetchone()
        return clave

    def consulta_compras(self, usuario):
        self.cursor.execute()

    def validar_usuario(self, user_data):
        self.cursor.execute(queries['validate_user'], user_data)
        result = self.cursor.fetchone()
        return result

    def salida_producto(self, producto_id):
        # elimina un producto de la base de datos
        try:
            self.cursor.execute(queries['del_producto'], (producto_id,))
        except Error as e:
            print('No existe producto con ese ID.')
        else:
            # registra los cambios a la base de datos
            self.conexion.commit()

    def entrada_producto(self, data_producto):
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


prueba = Database()
#nuevo_usuario = (55555555, 'Jose', 'Reyes', 'jr2000@gmail.com', '1131592009', '123456')
#prueba.crear_usuario(nuevo_usuario)
#query_table = ('usuarios',)
#prueba.eliminar_usuario((95806829,))
#prueba.consultar_usuario((95806829,))
print(prueba.validar_usuario(('martg@gmail.com', 'gatonegro')))
#print(prueba.get_clave(4))
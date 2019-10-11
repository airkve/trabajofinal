import mysql.connector
from dbdata import dbconf, queries
from mysql.connector import Error
from mysql.connector import errorcode

class Database():
    """ Modulo para consultar, modificar y conectarse a la base de datos. """
  
    def __init__(self):
        self.conexion = mysql.connector.connect(**dbconf)
        self.cursor = self.conexion.cursor()
        self.agregar_usuario = """ 
            INSERT INTO usuarios
                (dni, nombre, apellido, email, telefono, clave)
            VALUES
                (%s, %s, %s, %s, %s, %s)
        """
        self.eliminar_usuario = """ 
            DELETE FROM usuarios
            WHERE usuario_id = %s
        """
        self.agregar_producto = """ 
            INSERT INTO productos
                (nombre, descripcion, marca, categoria, precio)
            VALUES
                (%s, %s, %s, %s, %s)
        """
        self.eliminar_producto = """ 
            DELETE FROM productos
            WHERE producto_id = %s
        """
        
    def crear_usuario(self, data_usuario):
        self.modificar_db(queries['add_user'], data_usuario)
    
    def consultar_usuario(self):
        self.cursor.execute('SELECT * FROM usuarios')
        for i in self.cursor:
            print(i)

    def consulta_db(self, query, consulta):
        self.cursor.execute(query, consulta)
        
    def modificar_db(self, statement, data):
        self.cursor.execute(statement, data)


prueba = Database()
nuevo_usuario = (55555555, 'Jose', 'Reyes', 'jr2000@gmail.com', '1131592009', '123456')
prueba.crear_usuario(nuevo_usuario)
query = prueba.consultar_usuario()
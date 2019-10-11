import mysql.connector
from dbdata import dbconf
from mysql.connector import Error
from mysql.connector import errorcode

class Database():
    """ Modulo para consultar, modificar y conectarse a la base de datos. """
  
    def __init__(self):
        self.conexion = mysql.connector.connect(**dbconf)
        self.cursor = self.conexion.cursor(prepared=True)
        self.agregar_usuario = """ 
            INSERT INTO usuarios
                (documento, nombre, apellido, direccion, email, telefono, clave)
            VALUES
                (%, %, %, %, %, %, %)
        """
        self.eliminar_usuario = """ 
            DELETE FROM usuarios
            WHERE usuario_id = %
        """
        self.agregar_producto = """ 
            INSERT INTO productos
                (nombre, descripcion, marca, categoria, precio)
            VALUES
                (%, %, %, %, %)
        """
        self.eliminar_producto = """ 
            DELETE FROM productos
            WHERE producto_id = %
        """
        
    def crear_usuario(self, data_usuario):
        self.modificar_db(self.agregar_usuario, data_usuario)
    
    def consultar_usuario(self, userid):
        self.cursor.execute('SELECT * FROM usuarios')

    def consulta_db(self, query, consulta):
        self.cursor.execute(query, consulta)
        
    def modificar_db(self, statement, data):
        self.cursor.execute(statement, data)


prueba = Database()
prueba.consultar_usuario()
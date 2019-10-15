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
        self.cursor.execute(queries['add_user'], data_usuario)
        self.conexion.commit()

    def eliminar_usuario(self, usuario):
        # detecta si la data de usuario corresponde a un ID o a un DNI
        if usuario[0] <= 999:
            self.cursor.execute(queries['del_user_id'], usuario)
        else:
            self.cursor.execute(queries['del_user_dni'], usuario)
        
        self.conexion.commit()
    
    def consultar_tabla(self, tabla):
        #self.consulta_db(queries['list_table'], (tabla,))
        self.cursor.execute(queries['list_table'], (tabla,))
        reporte = self.cursor.fetchall()
        print(reporte)

    def consulta_compras(self, usuario):
        self.cursor.execute()


prueba = Database()
nuevo_usuario = (55555555, 'Jose', 'Reyes', 'jr2000@gmail.com', '1131592009', '123456')
#prueba.crear_usuario(nuevo_usuario)
query_table = ('usuarios')
#prueba.eliminar_usuario((55555555,))
prueba.consultar_tabla(query_table)
import mysql.connector
from dbconf import dbconf
from mysql.connector import Error
from mysql.connector import errorcode

class Database():
  """ Modulo para consultar, modificar y conectarse a la base de datos. """
  
  def __init__(self):
      self.conexion = mysql.connector.connect(**dbconf)
      self.cursor = self.conexion.cursor()
    
  def consulta_db(self, consulta):
      pass
    
  def modificar_db(self, data):
      pass

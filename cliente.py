# Modulo de cliente

from usuario import Usuario
#from db import Database
#from venta import Venta

class Cliente(Usuario):
    """ Modulo que define los atributos y metodos del cliente. """

    def __init__(self, user_id, dni, nombre, apellido, email, telefono, clave, direccion, ciudad):
        Usuario.__init__(self, email, nombre, apellido, clave)
        self.user_id = user_id
        self.dni = dni
        self.telefono = telefono
        self.direccion = direccion
        #self.altura = altura
        #self.cod_postal = cod_postal
        self.ciudad = ciudad
        #self.provincia = prov
        #self.pais = pais
        self.historial_compras = []

    def set_user_id(self, userid):
        self.user_id = userid
    
    def get_user_id(self):
        return self.user_id
    
    def set_dni(self, dni):
        self.dni = dni
    
    def get_dni(self):
        return self.dni

    def set_telefono(self, tlf):
        self.telefono = tlf

    def get_telefono(self):
        return self.telefono

    def set_clave(self, pwd):
        self.clave = pwd

    def get_clave(self):
        return self.clave

    def set_direccion(self, direccion):
        self.direccion = direccion
    
    def get_direccion(self):
        return self.direccion

    def set_altura(self, altura):
        self.altura = altura
    
    def get_altura(self):
        return self.altura

    def set_codpostal(self, cod):
        self.cod_postal = cod
    
    def get_codpostal(self):
        return self.cod_postal

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad
    
    def get_ciudad(self):
        return self.ciudad

    def set_provincia(self, prov):
        self.provincia = prov
    
    def get_provincia(self):
        return self.provincia

    def set_pais(self, pais):
        self.pais = pais
    
    def get_pais(self):
        return self.pais

    def get_client(self):
        """ dni, nombre, apellido, email, telefono, clave """
        client = [
            self.dni, self.nombre, self.apellido,
            self.email, self.telefono, self.clave
        ]
        # 
        direction = []

    def set_clients_list(self, lst_clientes):
        """ Metodo que transforma la data de la base de datos a objetos Cliente. """
        # variable que guarda los ususarios en una lista
        clientes = []
        # ciclo que recorre los tuples de usuarios y los agrega a la lista clientes
        for cliente in lst_clientes:
            clientes.append(list(cliente))

        # retorna la lista de clientes
        return clientes

    
#richard = list(Database().consultar_cliente(1))
#ric = Cliente(*richard)
#ric.get_user(5)
#print(ric.get_apellido())
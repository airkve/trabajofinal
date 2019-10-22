# Modulo de cliente

from usuario import Usuario
#from db import Database
#from venta import Venta

class Cliente(Usuario):
    """ Modulo que define los atributos y metodos del cliente. """

    def __init__(self, email, nombre, apellido, clave, dni, telefono, direccion, altura, cod_postal, ciudad, prov, pais):
        Usuario.__init__(self, email, nombre, apellido, clave)
        self.dni = dni
        self.telefono = telefono
        self.direccion = direccion
        self.altura = altura
        self.cod_postal = cod_postal
        self.ciudad = ciudad
        self.provincia = prov
        self.pais = pais
        self.historico_compras = []

    def set_dni(self, dni):
        self.dni = dni
    
    def get_dni(self):
        return self.dni

    def set_telefono(self, tlf):
        self.telefono = tlf

    def get_telefono(self):
        return self.telefono

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
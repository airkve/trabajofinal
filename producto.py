#!python3
# Proyecto final del recorrido del programador

class Producto():
    """ Modulo que parametriza la creaccion de un nuevo producto. """

    def __init__(self, nombre, descripcion, marca, categoria, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.marca = marca
        self.categoria = categoria
        self.precio = precio

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, desc):
        self.descripcion = desc
    
    def get_marca(self):
        return self.marca
    
    def set_marca(self, marca):
        self.marca = marca

    def get_categoria(sefl):
        return self.categoria

    def set_categoria(self, cat):
        self.categoria = cat

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio
    
    
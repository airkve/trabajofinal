# Proyecto final del recorrido del programador

class Producto():
    """ Modulo que parametriza la creaccion de un nuevo producto. """

    def __init__(self, id_product, nombre, descripcion, precio, categoria, marca, cantidad):
        self.id = id_product
        self.nombre = nombre
        self.descripcion = descripcion
        self.marca = marca
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    # Getters y setter para los atributos de producto
    def get_id(self):
        return self.id
    
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

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, cat):
        self.categoria = cat

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cant):
        self.cantidad = cant
    


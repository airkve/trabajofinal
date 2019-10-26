# Modulo para generar una factura con el historico de compras del cliente

class Factura:
    """ Clase que toma nombre, fecha, producto, cantidad, precio y crea una factura. """

    def __init__(self, nombre, fecha, producto, cantidad, precio):
        self.nombre = nombre
        self.fecha = fecha
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre

    def set_fecha(self, fecha):
        self.fecha = fecha

    def get_fecha(self):
        return self.fecha

    def set_producto(self, producto):
        self.producto = producto

    def get_producto(self):
        return self.producto

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    
    def get_cantidad(self):
        return self.cantidad

    def set_precio(self, precio):
        self.precio = precio
    
    def get_precio(self):
        return self.precio
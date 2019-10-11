#!python3
# Proyecto final del recorrido del programador

class Venta():
    """ Modulo para controlar los productos que se venden, las cantidades y los usuarios que los adquieren. """

    def __init__(self, comprador, producto, cantidad, precio_total, dir_envio):
        self.comprador = comprador
        self.producto = producto
        self.cantidad = cantidad
        self.precio_total = precio_total
        self.dir_envio = dir_envio

    def get_comprador(self):
        return self.comprador

    def set_comprador(self, usuario):
        self.comprador = usuario

    def get_producto(self):
        return self.producto

    def set_producto(self, articulo):
        self.producto = articulo

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cant):
        self.cantidad = cant

    def get_precio_total(self):
        return self.precio_total

    def set_precio_total(self, monto):
        self.precio_total = monto

    def get_dir_envio(self):
        return self.dir_envio

    def set_dir_envio(self, direccion):
        self.dir_envio = direccion

    
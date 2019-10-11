# Diccionario con la configuracion de la base de datos

dbconf = {
    'host':'localhost',
    'database':'ecommerce',
    'user':'root',
    'password':''
}

queries = {
    'add_user':'INSERT INTO usuarios (dni, nombre, apellido, email, telefono, clave) VALUES (%s, %s, %s, %s, %s, %s)',
    'del_user_id':'DELETE FROM usuarios WHERE usuario_id = %s',
    'del_user_dni':'DELETE FROM usuarios WHERE dni = %s',
    'add_product':'INSERT INTO productos (nombre, descripcion, marca, categoria, precio) VALUES (%s, %s, %s, %s, %s)',
    'mod_product_cant':'UPDATE '
    'del_product':'DELETE FROM productos WHERE producto_id = %s',
    'add_compra':'INSERT INTO compras () '
}
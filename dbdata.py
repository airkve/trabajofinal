# Diccionario con la configuracion de la base de datos

dbconf = {
    'host':'localhost',
    'database':'ecommerce',
    'user':'root',
    'password':''
}

queries = {
    'get_user_by_pswd':'SELECT * FROM usuarios WHERE clave = %s',
    'get_user_by_email':'SELECT * FROM usuarios WHERE email = %s',
    'list_user_id':'SELECT * FROM usuarios WHERE usuario_id = %s',
    'list_user_dni':'SELECT * FROM usuarios WHERE dni = %s',
    'list_product_id':'SELECT * FROM productos WHERE usuario_id = %s',
    'add_user':'INSERT INTO usuarios (dni, nombre, apellido, email, telefono, clave) VALUES (%s, %s, %s, %s, %s, %s)',
    'del_user_id':'DELETE FROM usuarios WHERE usuario_id = %s',
    'del_user_dni':'DELETE FROM usuarios WHERE dni = %s',
    'add_product':'INSERT INTO productos (nombre, descripcion, marca, categoria, precio) VALUES (%s, %s, %s, %s, %s)',
    'mod_product_cant':'UPDATE productos set cantidad = %s where id = %s',
    'del_product':'DELETE FROM productos WHERE producto_id = %s',
    'new_shopping':'INSERT INTO compras (usuario_id, fecha_compra, producto_id, cantidad, precio_total, direccion_id) VALUES (%s, %s, %s, %s, %s, %s)',
    'user_shop_history':'SELECT usuarios.nombre, productos.nombre, compras.cantidad, compras.precio_total FROM usuarios INNER JOIN compras ON compras.usuario_id = usuarios.usuario_id INNER JOIN productos ON productos.producto_id = compras.producto_id',
    'validate_user':'SELECT * FROM usuarios WHERE email = %s AND clave = %s'
}
import sqlite3
import mostrar

DB_NAME = "inventario.db"

def actualizar_producto():
    print("Actualizar Producto")
    #Muestro los productos disponibles
    mostrar.mostrar_productos()
    while True:
        try:
            producto = int(input("Ingrese el ID del producto que desea actualizar (o '0' para cancelar): "))
            if producto == 0:
                print("Actualización de producto cancelada.")
                return
            elif producto < 0:
                print("¡Error! El ID no puede ser un número negativo. Intente de nuevo.")
            else:
                break
        except ValueError:
            print("¡Error! Debe ingresar un número entero. Intente de nuevo.")
            continue

    #Conexion DB
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE id = ?;", (producto,))

        producto_existente = cursor.fetchone()

        if not producto_existente:
            print(f"No se encontró un producto con ID {producto}. No se actualizó nada.")
            return

        #Muestro los datos actuales del producto
        print(f"Datos actuales del producto con ID {producto}:")
        print(f"Nombre actual: {producto_existente[1]}")
        print(f"Descripción actual: {producto_existente[2]}")
        print(f"Cantidad actual: {producto_existente[3]}")
        print(f"Precio actual: {producto_existente[4]}")
        print(f"Categoría actual: {producto_existente[5]}")
        print("(Deje vacío un campo si no desea actualizarlo)")

        #Inicio nuevas variables
        nuevo_nombre = producto_existente[1]
        nueva_descripcion = producto_existente[2]
        nueva_cantidad = producto_existente[3]
        nuevo_precio = producto_existente[4]
        nueva_categoria = producto_existente[5]

        #Solicito nuevos datos
        #Nombre
        nombre = input(f"Ingrese el nuevo nombre del producto, actual {nuevo_nombre}: ")
        if nombre: #Si se ingresa un nombre, se cambia
            nuevo_nombre = nombre
        elif nombre == "":
            print("No se actualizó el nombre del producto.")

        #Descripción
        descripcion = input(f"Ingrese la nueva descripción del producto, actual {nueva_descripcion}: ")
        if descripcion: #Si se ingresa una descripcion, se cambia
            nueva_descripcion = descripcion
        elif descripcion == "":
            print("No se actualizó la descripción del producto.")

        #Cantidad
        while True:
            cantidad = int(input(f"Ingrese la nueva cantidad del producto, actual {nueva_cantidad}: "))
            if not cantidad:
                print("No se actualizó la cantidad del producto.")
                break

            try:
                if cantidad < 0:
                    print("¡Error! La cantidad no puede ser un número negativo. Intente de nuevo.")
                else:
                    nueva_cantidad = cantidad
                    break
            except ValueError:
                print("¡Error! Debe ingresar un número entero. Intente de nuevo.")

        #Precio
        while True:
            precio = int(input(f"Ingrese el nuevo precio del producto, actual {nuevo_precio}: "))
            if not precio:
                print("No se actualizó el precio del producto.")
                break
            try:
                if precio < 0:
                    print("¡Error! El precio no puede ser un número negativo. Intente de nuevo.")
                else:
                    nuevo_precio = precio
                    break
            except ValueError:
                print("¡Error! Debe ingresar un número entero. Intente de nuevo.")

        #Categoría
        categoria = input(f"Ingrese la nueva categoría del producto, actual {nueva_categoria}:")
        if categoria: #Si se ingresa una categoria, se cambia
            nueva_categoria = categoria
        elif categoria == "":
            print("No se actualizó la categoría del producto.")

        #Preparar la consulta de actualización
        sql_update = """
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?;"""
        
        valores = (nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_categoria, producto)

        cursor.execute(sql_update, valores)
        conexion.commit()

        if cursor.rowcount > 0:
            print(f"Producto con ID {id} actualizado exitosamente.")
        else:
            print(f"No se realizaron cambios en el producto con ID {id}.") # Esto podría pasar si no se cambió nada.        
    
    except sqlite3.Error as e:
        print(f"¡Error! No se pudo actualizar el producto en la base de datos: {e}")
        if conexion:
            conexion.rollback() # Deshacer los cambios en caso de error
    finally:
        conexion.close() # Cerrar la conexión a la base de datos
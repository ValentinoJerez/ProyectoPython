import sqlite3

from colorama import init, Fore, Style, init

DB_NAME = "inventario.db" #Defino Base de datos

def mostrar_productos():
    print("Lista de Productos")
    
    #Conexion DB
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        #Selecciono todos los datos
        sql_select_all = "SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos;"
        cursor.execute(sql_select_all)
        
        #Obtengo todos los resultados
        productos_registrados = cursor.fetchall()
        
        #Verifico si hay productos
        if not productos_registrados:
            print(Fore.RED + Style.BRIGHT + "No hay productos registrados")
            return #Salgo de la funcion
            
        #Itero sobre cada producto
        for producto in productos_registrados:
            #Accedo a elementos por indice
            producto_id = producto[0]
            nombre = producto[1]
            descripcion = producto[2]
            cantidad = producto[3]
            precio = producto[4]
            categoria = producto[5]
            print(Fore.GREEN + Style.BRIGHT + f"{producto_id} - {nombre} - {descripcion} - {cantidad} - {precio} - {categoria} ")
    
    #Manejo de errores
    except sqlite3.Error as e:
        print(Fore.RED + Style.BRIGHT + "¡Error! No se puede recuperar los datos.")
    finally:
        conexion.close()
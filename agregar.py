import sqlite3

from colorama import init, Fore, Style, init

init(autoreset=True)

DB_NAME = "inventario.db" #Defino la base de datos nuevamente

def agregar_producto():
    print("Agregar un nuevo producto")
    
    #Nombre
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if nombre == "":
            print(Fore.RED + Style.BRIGHT + "El nombre del producto no puede estar vacío" + Style.RESET_ALL)
        else:
            break

    #Descripcion
    while True:
        descripcion = input("Ingrese la descripción del producto: ") #Descripcion puede estar vacio
        break

    #Cantidad
    while True:
        cantidad = input("Ingrese la cantidad del producto: ")
        if cantidad == "":
            print(Fore.RED + Style.BRIGHT + "La cantidad del producto no puede estar vacía" + Style.RESET_ALL)
        else:
            break

    #Precio
    while True:
        precio = int(input("Ingrese el precio del producto: ")) #Pido un entero
        if precio == "":
            print(Fore.RED + Style.BRIGHT + "El precio del producto no puede estar vacío" + Style.RESET_ALL)
        elif precio > 0: #Verifico que el precio sea mayor a 0
            break
        else:
            print(Fore.YELLOW + Style.BRIGHT + "El precio debe ser mayor a 0")

    #Categoria
    while True:
        categoria = input("Ingrese la categoria del producto: ")
        if categoria == "":
            print(Fore.RED + Style.BRIGHT + "La categoria del producto no puede estar vacía" + Style.RESET_ALL)
        else:
            break

    #Conexion con Base de Datos
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()
        
        sql_insert = """
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?);
            """
        
        valores = (nombre, descripcion, cantidad, precio, categoria)

        cursor.execute(sql_insert, valores)
        conexion.commit() #Guardo los cambios

        print(Fore.GREEN + Style.BRIGHT + f"Producto {nombre} agregado con exito " + Style.RESET_ALL)

    except sqlite3.Error as e: #Manejo de errores
        print(f"Error al agregar producto: {e}")
        if conexion:
            conexion.rollback() #Desago los cambios en caso de error

    finally:
        conexion.close() #Cierro conexion
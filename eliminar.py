import sqlite3
import mostrar

from colorama import init, Fore, Style, init

DB_NAME = "inventario.db"

def eliminar_productos():
    print("Eliminar Producto")
    #Muestro los productos disponibles
    mostrar.mostrar_productos()

    while True:
        print("¿Que producto desea eliminar?")
        producto = int(input("Ingrese el ID del producto que desea eliminar (o 0 para cancelar): "))
        if producto == 0:
            print(Fore.YELLOW + Style.BRIGHT +"Eliminacion de producto cancelada")
            return
        elif producto < 0:
            print(Fore.RED + Style.BRIGHT + "¡Error! El ID no puede ser un número negativo. Intente de nuevo.")
        else:
            break
    
    #Conexion DB
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor
        
        sql_delete = "DELETE FROM productos WHERE id = ?;"
        
        #Paso ID como tupla
        cursor.execute(sql_delete, (producto,))
        conexion.commit()
        
        #Verifico si se elimino
        if cursor.rowcount > 0:
            print(Fore.GREEN + Style.BRIGHT + f"Producto con ID {producto} eliminado exitosamente.")
        else:
            print(Fore.YELLOW + Style.BRIGHT + f"No se encontró un producto con ID {producto}. No se eliminó nada.")
    
    except sqlite3.Error as e:
        print(f"¡Error! No se pudo eliminar el producto {e}")
        if conexion:
            conexion.rollback() #Borro los cambios en caso de error
    finally:
        conexion.close()
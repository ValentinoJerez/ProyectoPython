import sqlite3 #Importo SQL

import menu
import agregar
import mostrar
import eliminar
import buscar
import actualizar

#Importo Colorama
from colorama import init, Fore, Style, init

#Inicializo Colorama
init(autoreset=True)

#Base de Datos

DB_NAME = "inventario.db"

def crear_base_datos():
    try:
        conexion = sqlite3.connect(DB_NAME) #Conecto con mi base de datos
        cursor = conexion.cursor() #Cursor para ejecutar comando en BD

        sql_crear_tabla = """CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL,descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL, categoria TEXT );"""

        cursor.execute(sql_crear_tabla) #Ejecuto comando para crear tabla
        conexion.commit() #Guardo los cambios

    except sqlite3.Error as e: #Manejo de errores
        print(f"Error al crear la base de datos: {e}")
    finally: #Finalmente cierro la conexion, con o sin errores
        conexion.close()

#LLamo funcion BD antes de iniciar programa
crear_base_datos()

def main():
    while True:
        print(Style.BRIGHT + "Bienvenido al Sistema de Inventario de Productos" + Style.RESET_ALL)
        print(Style.BRIGHT + "\nMenu:" + Style.RESET_ALL)
        menu.mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            print("Agregar Producto")
            agregar.agregar_producto()
        elif opcion == "2":
            print("Ver Productos")
            mostrar.mostrar_productos()
        elif opcion == "3":
            print("Eliminar Producto")
            eliminar.eliminar_productos()
        elif opcion == "4":
            print("Buscar Producto")
            buscar.buscar_producto()
        elif opcion == "5":
            print("Actualizar Producto")
            actualizar.actualizar_producto()
        elif opcion == "6":
            print("Saliendo del Menu, ¡Gracias!")
            break
        else:
            print(f"{Fore.RED}Opción inválida. Por favor, seleccione un número del 1 al 6.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
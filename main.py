import sqlite3 #Importo SQL

import menu
import agregar
import mostrar
import eliminar
import buscar
import actualizar

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
        print("\nMenu:")
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

if __name__ == "__main__":
    main()
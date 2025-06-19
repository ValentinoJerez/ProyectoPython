import sqlite3

from colorama import init, Fore, Style, init

DB_NAME = "inventario.db" # Defino la base de datos


def buscar_productos():
    criterio = ""
    valor = None
    
    while True:
        print("n\¿Como desea buscar su producto?")
        print("1. Por nombre")
        print("2. Por categoria")
        print("3. Por ID")
    
        opcion = int(input("Ingrese una opción (1, 2 o 3): "))
        if opcion == 1:
            criterio = "nombre"
            while True:
                nombre = input("Ingrese el nombre del producto: ")
                #Verifico que el nombre no este vacio
                if nombre:
                    valor = f"%{nombre.lower()}%"
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + "El nombre del producto no puede estar vacío" + Style.RESET_ALL)
                    break
        elif opcion == 2:
            criterio = "categoria"
            while True:
                categoria = input("Ingrese la categoria del producto: ")
                
                #Verifico que la categoria no este vacia
                if categoria:
                    valor = f"%{categoria.lower()}%"
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + "La categoria del producto no puede estar vacía" + Style.RESET_ALL)
                    break
        elif opcion == 3:
            criterio = "id"
            while True:
                id_input = int(input("Ingrese el ID del producto: "))
                try:
                    if id_input > 0:
                        break
                    else:
                        print(Fore.YELLOW + Style.BRIGHT +"El ID del producto debe ser un número positivo" + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + Style.BRIGHT + "Por favor, ingrese un número válido para el ID del producto" + Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + "Opción no válida. Por favor, elija 1, 2 o 3." + Style.RESET_ALL)
                return
        
        #Conexion con Base de Datos
        try:
            conexion = sqlite3.connect(DB_NAME)
            cursor = conexion.cursor()

            #Construyo la consulta SQL dependiendo del criterio
            sql_search = ""
            
            if criterio == "nombre":
                sql_search = "SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE id = ?;"
                #Paso el valor como una tupla
                cursor.execute(sql_search, (valor,))
            elif criterio in ["nombre", "categoria"]:
                #Para nombre y categoría, uso LOWER() y LIKE
                sql_search = f"SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE LOWER({criterio}) LIKE ?;"
                cursor.execute(sql_search, (valor,))
                resultados = cursor.fetchall()

            #Muestro los resultados
            if not resultados:
                print(Fore.RED + Style.BRIGHT + "No se encontraron productos que coincidan con su búsqueda.")
            else:
                print(Fore.GREEN + Style.BRIGHT +"Productos encontrados:")
                #Itero sobre los resultados y muestro cada producto
                for producto in resultados:
                    #Accedo a los elementos por índice
                    producto_id = producto[0]
                    nombre = producto[1]
                    descripcion = producto[2]
                    cantidad = producto[3]
                    precio = producto[4]
                    categoria = producto[5]
                    print(f"{producto_id} - {nombre} - {descripcion} - {cantidad} - {precio} - {categoria}")

        #Manejo de errores
        except sqlite3.Error as e:
            print(Fore.RED + Style.BRIGHT + "¡Error! No se puede recuperar los datos.")
        finally:
            conexion.close() 
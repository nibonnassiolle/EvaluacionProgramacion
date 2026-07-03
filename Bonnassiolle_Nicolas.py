# ==========================================
#       SISTEMA DE GESTIÓN DE LIBROS
# ==========================================
import time

def mostrar_menu():
    # Muestra el menú principal
    print("="*40)
    print('             Menú Principal')
    print("="*40)
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("\n")


def leer_opcion():
    # Lee y valida las opciones del menu
    while True:
        opcion_str = input("Seleccione una opción (1-6): ").strip()
        if opcion_str.isdigit():
            opcion = int(opcion_str)
            if 1 <= opcion <= 6:
                return opcion
            time.sleep(1.5)
        print("Error: opción inválida. Debes ingresar un número del 1 al 6.")
        time.sleep(1.5)

#validan que lo ingresado no sea un espacio en blanco
def validar_titulo(titulo):
    return titulo.strip() != ""

#validan que lo ingresado no sea un numero negativo
def validar_copias(copias_str):
    return copias_str.isdigit() and int(copias_str) >= 0
def validar_prestamo(prestamo_str):
    return prestamo_str.isdigit() and int(prestamo_str) > 0


def buscar_libro(libros, titulo):
    # Busca libro por su título (coincidencia exacta)
    for i, libro in enumerate(libros):
        if libro["titulo"] == titulo:
            return i
    return -1


def agregar_libro(libros):
    #Agregamos un libro dando un título
    print("\n--- AGREGAR LIBRO ---")
    titulo = input("Título: ").strip()
    if not validar_titulo(titulo):
        print("Error: el título no puede estar vacío.")
        return
    time.sleep(0.5)

    #Damos un valor a las copias que están siendo vendidas
    copias_str = input("Copias: ").strip()
    if not validar_copias(copias_str):
        print("Error: copias debe ser un número mayor o igual a 0.")
        return
    time.sleep(0.5)

    #Asignamos los días de préstamo
    prestamo_str = input("Días de préstamo: ").strip()
    if not validar_prestamo(prestamo_str):
        print("Error: préstamo debe ser un número mayor a 0.")
        return
    time.sleep(0.5)

    #Agrega el libro a la lista
    libros.append({
        "titulo": titulo,
        "copias": int(copias_str),
        "prestamo": int(prestamo_str),
        "disponible": False
    })
    print(f"Libro '{titulo}' agregado correctamente.")
    time.sleep(0.5)


#Eliminamos un libro de la lista
def eliminar_libro(libros):
    print("\n--- ELIMINAR LIBRO ---")
    titulo = input("Título a eliminar: ")
    pos = buscar_libro(libros, titulo)

    #En caso de no encontrar un libro...
    if pos == -1:
        print(f"El libro '{titulo}' no se encuentra registrado.")
        return
    time.sleep(1.5)

    #Confimacion de eliminación de un libro
    eliminado = libros.pop(pos)
    print(f"Libro '{eliminado['titulo']}' eliminado correctamente.")


def actualizar_disponibilidad(libros):
    # True si hay mas de 0 copias y False si hay 0 copias
    for libro in libros:
        libro["disponible"] = libro["copias"] >= 1


def mostrar_libros(libros):
    print("\n=== LISTA DE LIBROS ===")
    if not libros:
        #Si no hay libros registrados dice este mensaje
        print("No hay libros registrados.")
        return

    for libro in libros:
        #Revisamos el estado de nuestros libros en nuestra libreria
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"

        print(f"Titulo: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Prestamo: {libro['prestamo']} días")
        print(f"Estado: {estado}")
        print("-" * 30)
        time.sleep(1.5)


def ejecutar_sistema():
    libros = []

    while True:
        #Llamamos al menú por su def
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_libro(libros)
            time.sleep(1.5)
        elif opcion == 2:
            #Buscamos un libro por su nombre
            print("\n--- BUSCAR LIBRO ---")
            titulo = input("Título a buscar: ")
            pos = buscar_libro(libros, titulo)

            if pos == -1:
                #Mensaje cuando no se encontró el libro
                print("Libro no encontrado.")
                time.sleep(1.5)
            else:
                #Estado del libro encontrado por su nombre
                libro = libros[pos]
                print("Libro encontrado:")
                print(f"Título: {libro['titulo']}")
                print(f"Copias: {libro['copias']}")
                print(f"Préstamo: {libro['prestamo']} días")
                print(f"Disponible: {libro['disponible']}")
                time.sleep(1.5)
        elif opcion == 3:
            #Eliminar libro
            eliminar_libro(libros)
            time.sleep(1.5)
        elif opcion == 4:
            #Actualiza la disponibilidad de nuestros libros
            actualizar_disponibilidad(libros)
            print("Disponibilidad actualizada correctamente.")
            time.sleep(1.5)
        elif opcion == 5:
            #muestra los libros actuales
            mostrar_libros(libros)
            time.sleep(1.5)
        elif opcion == 6:
            #Salida del sistema
            print("Gracias por usar el sistema de gestión de libros. Hasta luego!")
            time.sleep(1.5)
            break


if __name__ == "__main__":
    ejecutar_sistema()
import json


def cargar_json(nombre_fichero: str) -> dict:
    """
    Carga el contenido de un fichero JSON.

    Args:
        nombre_fichero (str): Nombre del fichero JSON.

    Returns:
        (dict): Contenido del archivo JSON como un diccionario, o None si no se pudo cargar.
    """
    try:
        with open(nombre_fichero, "r") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")

    except json.JSONDecodeError:
        print("*ERROR* El archivo JSON tiene un formato incorrecto.")

    except Exception as e:
        print(f"*ERROR* Problemas al cargar los datos {e}.")

    return None


def guardar_json(nombre_fichero: str, datos: dict):
    """
    Guarda los datos en un fichero JSON.

    Args:
        nombre_fichero (str): Nombre del fichero JSON.
        datos (dict): Datos a guardar.
    """
    try:
        with open(nombre_fichero, "w") as archivo:
            json.dump(datos, archivo, indent = 4)

    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo '{nombre_fichero}'.")

    except TypeError as e:
        print(f"*ERROR* Los datos no son serializables a JSON. Detalle: {e}")        

    except Exception as e:
        print(f"*ERROR* Problemas al guardar los datos: {e}")


def actualizar_usuario(datos: dict, id_usuario: int, nueva_edad: int):
    """
    Actualiza la edad de un usuario dado su ID.

    Args:
        datos (dict): Diccionario con los datos actuales.
        id_usuario (int): ID del usuario a actualizar.
        nueva_edad (int): Nueva edad del usuario.
    """
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            usuario["edad"] = nueva_edad
            print(f"Usuario con ID {id_usuario} actualizado.")
            return

    print(f"Usuario con ID {id_usuario} no encontrado.")


def insertar_usuario(datos: dict, nuevo_usuario: dict):
    """
    Inserta un nuevo usuario.

    Args:
        datos (dict): Diccionario con los datos actuales.
        nuevo_usuario (dict): Diccionario con los datos del nuevo usuario.
    """
    datos["usuarios"].append(nuevo_usuario)
    print(f"Usuario {nuevo_usuario['nombre']} añadido con éxito.")


def eliminar_usuario(datos: dict, id_usuario: int):
    """
    Elimina un usuario dado su ID.

    Args:
        datos (dict): Diccionario con los datos actuales.
        id_usuario (int): ID del usuario a eliminar.
    """
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            datos["usuarios"].remove(usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
            return

    print(f"Usuario con ID {id_usuario} no encontrado.")
    

def mostrar_datos(usuarios: list):
    """
    Recibe una lista de usuarios y muestra su contenido en consola.
    """

    print("--- Contenido Actual del JSON ---")
    
    if not usuarios:
        print("No hay usuarios en el archivo.")
    else:
        for usuario in usuarios:
            id_usuario = usuario.get("id", "Desconocido")
            nombre = usuario.get("nombre", "Desconocido")
            edad = usuario.get("edad", "No especificada")
            print(f"ID: {id_usuario}, Nombre: {nombre}, Edad: {edad}")
    
    print("--- Fin del Contenido ---")



def inicializar_datos():
    archivo_origen = "datos_usuarios_orig.json"
    archivo_destino = "datos_usuarios.json"

    try:
        with open(archivo_origen, "r", encoding="utf-8") as f:
            datos = json.load(f)  
        with open(archivo_destino, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"Datos inicializados desde '{archivo_origen}' a '{archivo_destino}'.")

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_origen}' no existe.")

    except json.JSONDecodeError:
        print(f"Error: El archivo '{archivo_origen}' tiene un formato JSON inválido.")

    except Exception as e:
        print(f"Error inesperado: {e}")


import os
import json

def main():
    """
    Función principal que realiza las operaciones de gestión de un archivo JSON.
    """

    # RUTA del archivo de trabajo
    nombre_fichero = "datos_usuarios.json"

    # 1. Limpiar la consola
    os.system("cls" if os.name == "nt" else "clear")

    # 2. Inicializar datos
    inicializar_datos()

    # 3. Cargar datos desde datos_usuarios.json
    datos = cargar_json(nombre_fichero)

    if datos is None:
        print("Error al cargar los datos.")
        return

    # 4. Mostrar contenido inicial
    mostrar_datos(datos["usuarios"])
    input("\nPresiona ENTER para continuar...")

    # 5. Actualizar edad de un usuario
    actualizar_usuario(datos, id_usuario=1, nueva_edad=31)
    print("Edad actualizada.\n")
    mostrar_datos(datos["usuarios"])
    input("\nPresiona ENTER para continuar...")

    # 6. Insertar nuevo usuario
    nuevo_usuario = {"id": 3, "nombre": "Pedro", "edad": 40}
    insertar_usuario(datos, nuevo_usuario)
    print("Usuario insertado.\n")
    mostrar_datos(datos["usuarios"])
    input("\nPresiona ENTER para continuar...")

    # 7. Eliminar usuario
    eliminar_usuario(datos, id_usuario=2)
    print("Usuario eliminado.\n")
    mostrar_datos(datos["usuarios"])
    input("\nPresiona ENTER para continuar...")

    # 8. Guardar cambios
    guardar_json(nombre_fichero, datos)

    print("Cambios guardados en datos_usuarios.json ✔")


if __name__ == "__main__":
    main()
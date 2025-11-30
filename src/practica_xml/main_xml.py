import xml.etree.ElementTree as ET
import os

def cargar_xml(nombre_fichero: str):
    """
    Carga un archivo XML y devuelve el árbol y la raíz.
    """
    try:
        arbol = ET.parse(nombre_fichero)
        raiz = arbol.getroot()
        return arbol, raiz
    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")
    except ET.ParseError:
        print(f"*ERROR* El archivo {nombre_fichero} tiene un formato XML inválido.")
    except Exception as e:
        print(f"*ERROR* Problemas al cargar el XML: {e}")
    return None, None


def guardar_xml(arbol: ET.ElementTree, nombre_fichero: str) -> bool:
    """
    Guarda un árbol XML en un archivo.
    """
    try:
        arbol.write(nombre_fichero, encoding="utf-8", xml_declaration=True)
        return True
    except Exception as e:
        print(f"*ERROR* No se pudo guardar el archivo XML: {e}")
        return False


def crear_arbol(nombre_raiz: str):
    """
    Crea un árbol XML vacío con un nodo raíz.
    """
    raiz = ET.Element(nombre_raiz)
    arbol = ET.ElementTree(raiz)
    return arbol, raiz


def inicializar_datos():
    """
    Copia datos_usuarios_orig.xml a datos_usuarios.xml sin usar shutil.
    """
    origen = "datos_usuarios_orig.xml"
    destino = "datos_usuarios.xml"
    try:
        with open(origen, "r", encoding="utf-8") as f_origen:
            contenido = f_origen.read()

        with open(destino, "w", encoding="utf-8") as f_destino:
            f_destino.write(contenido)

        print(f"Datos inicializados desde '{origen}' a '{destino}'.")
    except FileNotFoundError:
        print(f"*ERROR* El archivo origen '{origen}' no existe. No se realizó la copia.")
    except Exception as e:
        print(f"*ERROR* Problemas al copiar: {e}")


def mostrar_datos(raiz):
    """
    Muestra los usuarios del XML de forma organizada.
    """
    usuarios = raiz.findall("usuario")
    print("\n--- Contenido Actual del XML ---")
    if not usuarios:
        print("ERROR El archivo XML no contiene usuarios!")
    else:
        for u in usuarios:
            id_usuario = u.findtext("id", "Desconocido")
            nombre = u.findtext("nombre", "Desconocido")
            edad = u.findtext("edad", "No especificada")
            print(f"ID: {id_usuario}, Nombre: {nombre}, Edad: {edad}")
    print("--- Fin del Contenido ---\n")


def actualizar_usuario(raiz: ET.Element, id_usuario: int, nueva_edad: int):
    for u in raiz.findall("usuario"):
        if u.findtext("id") == str(id_usuario):
            u.find("edad").text = str(nueva_edad)
            print(f"Usuario con ID {id_usuario} actualizado.")
            return
    print(f"Usuario con ID {id_usuario} no encontrado.")


def insertar_usuario(raiz: ET.Element, nuevo_usuario: dict):
    usuario = ET.SubElement(raiz, "usuario")
    ET.SubElement(usuario, "id").text = str(nuevo_usuario["id"])
    ET.SubElement(usuario, "nombre").text = nuevo_usuario["nombre"]
    ET.SubElement(usuario, "edad").text = str(nuevo_usuario["edad"])
    print(f"Usuario {nuevo_usuario['nombre']} añadido con éxito.")


def eliminar_usuario(raiz: ET.Element, id_usuario: int):
    for u in raiz.findall("usuario"):
        if u.findtext("id") == str(id_usuario):
            raiz.remove(u)
            print(f"Usuario con ID {id_usuario} eliminado.")
            return
    print(f"Usuario con ID {id_usuario} no encontrado.")


def main():
    archivo_xml = "datos_usuarios.xml"

    # 1. Limpiar consola
    os.system("cls" if os.name == "nt" else "clear")

    # 2. Inicializar datos
    inicializar_datos()

    # 3. Cargar XML
    arbol, raiz = cargar_xml(archivo_xml)
    if raiz is None:
        print("Inicializando árbol vacío...")
        arbol, raiz = crear_arbol("usuarios")

    # 4. Mostrar contenido inicial
    mostrar_datos(raiz)
    input("Presiona ENTER para continuar...")

    # 5. Actualizar edad de un usuario
    actualizar_usuario(raiz, 1, 31)
    mostrar_datos(raiz)
    input("Presiona ENTER para continuar...")

    # 6. Insertar nuevo usuario
    insertar_usuario(raiz, {"id": 3, "nombre": "Pedro", "edad": 40})
    mostrar_datos(raiz)
    input("Presiona ENTER para continuar...")

    # 7. Eliminar usuario
    eliminar_usuario(raiz, 2)
    mostrar_datos(raiz)
    input("Presiona ENTER para continuar...")

    # 8. Guardar cambios
    guardar_xml(arbol, archivo_xml)
    print("Operaciones completadas. Archivo XML actualizado.\n")


if __name__ == "__main__":
    main()

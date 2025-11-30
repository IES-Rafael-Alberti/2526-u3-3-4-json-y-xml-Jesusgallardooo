'''
Pasar los datos de un archivo XML a un archivo JSON, y luego a su vez, que pase de un archivo JSON a un archivo XML.

    XML -> JSON
    JSON -> XML

'''

import json
import xmltodict
import dicttoxml


def xmlAjson(nombre_archivo: str):
    with open(f"{nombre_archivo}.xml", "r") as f_xml:
        datos_a_convertir = xmltodict.parse(f_xml.read())
        conversion_a_json = json.dumps(datos_a_convertir, indent=4, ensure_ascii=False)

        with open(f"{nombre_archivo}.json", "w") as f_json:
            f_json.write(conversion_a_json)

    print("XML convertido a JSON correctamente")


def jsonAxml(nombre_archivo: str):
    with open(f"{nombre_archivo}.json", "r") as f_json:
        datos_a_convertir = json.load(f_json)

    xml_bytes = dicttoxml.dicttoxml(datos_a_convertir, custom_root="root", attr_type=False)

    with open(f"{nombre_archivo}_convertido.xml", "wb") as f_xml:
        f_xml.write(xml_bytes)

    print("JSON convertido a XML correctamente")


def main(nombre_archivo):
    xmlAjson(nombre_archivo)
    jsonAxml(nombre_archivo)


if __name__ == "__main__":
    main("datos")

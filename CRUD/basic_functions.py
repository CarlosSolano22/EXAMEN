def create_json_peliculas():
    nombre = input("Nombre: ")
    fechaEmision = input("Fecha de Emisión: ")
    autor = input("Autor: ")
    Clasificacion = input("Clasificación: ")


    pelicula = {
        "nombre": nombre,
        "fechaEmision": fechaEmision,
        "autor": autor,
        "Clasificacion": Clasificacion,
    }

    return pelicula


def create_json_update_peliculas():
    print("Menu de opciones ")
    print("1. Modificar todo el documento")
    print("2. Modificar solo un elemento del documento")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        fechaEmision = input("Fecha de emision: ")
        autor = input("Autor: ")
        Clasificacion = input("Clasificacion: ")


        pelicula = {
            "nombre": nombre,
            "fechaEmision": fechaEmision,
            "autor": autor,
            "Clasificacion": Clasificacion,
        }
        return pelicula
    elif opcion == "2":
        indice = input("Ingrese el valor de indice a modificar: ")
        valor = input("Ingrese el valor a modificar")
        pelicula = {indice:valor}
        return pelicula



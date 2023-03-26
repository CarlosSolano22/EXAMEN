from crud import *
from basic_functions import *

while True:
    print("Menu de opciones")
    print("1. Consultar todas las peliculas")
    print("2. Consultar pelicula por titulo")
    print("3. Agregar")
    print("4. Modificar")
    print("5. Eliminar")
    print("6. Consultar por fecha de emisión")
    print("7. Salir de sistema")


    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        read_peliculas()
    elif opcion == "2":
        nombre = input("Ingrese el titulo de la pelicula a buscar: ")
        read_peliculas(nombre)

    elif opcion == "3":
        pelicula = create_json_peliculas()
        create_peliculas(pelicula)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del registro a modificar: ")
        pelicula = create_json_update_peliculas()
        update_peliculas(nombre, pelicula)
    elif opcion == "5":
        nombre = input("Ingrese el nombre de la pelicula a eliminar: ")
        delete_peliculas(nombre)
    elif opcion == "6":
        fechaEmision = input("Ingrese la fecha de emisión a buscar: ")
        read_peliculas_2(fechaEmision)
    elif opcion == "7":
        print("Saliendo del sistema")
        break


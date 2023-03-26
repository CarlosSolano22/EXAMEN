import json
from conection_parameters import collection


def read_peliculas(nombre=None):
    if nombre is not None:
        query = {"nombre": nombre}
        document = collection.find_one(query)
        print(document)
    else:
        documents = collection.find()
        for document in documents:
            print(document)

def read_peliculas_2(fechaEmision=None):
    if fechaEmision is not None:
        query = {"fechaEmision": fechaEmision}
        document = collection.find_one(query)
        print(document)
    else:
        documents = collection.find()
        for document in documents:
            print(document)

def create_peliculas(peliculas):
    result = collection.insert_one(peliculas)
    print(result.inserted_id)



def update_peliculas(nombre, json_indices_values):
    query = {"nombre": nombre}
    new_values = {"$set": json_indices_values}
    result = collection.update_one(query, new_values)
    print(result.modified_count)



def delete_peliculas(nombre=None):
    if nombre is not None:
        query = {"nombre": nombre}
        document = collection.delete_one(query)
        print("registro eliminado")
    else:
        print("Dato ingresado incorrecto")



from pymongo.mongo_client import MongoClient    # Se importa la biblioteca que servirá para interactuar con bases de datos

#CONEXIÓN
def conexion():    # Se define la función "conexion"
    uri = "mongodb+srv://cagomezj:1234@cluster0.cgumkrz.mongodb.net/?retryWrites=true&w=majority"    # Se establece la conexión a la base de datos alojada en py mongo
    # Create a new client and connect to the server
    return MongoClient(uri)   # Devuelve el resultado de la función

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos():   # Se define la función 
    client = conexion()    # Se define un nombre para la función "coneción"
    db = client.actividad4.data_real    # Se define la variable que contiene una colección de la data real
    data_list = []   # Se genera una lista vacia
    for data_real_bd in db.find():   # Se genera un bucle for
        data_list.append(data_real_bd)   # Busca y almacena los datos encontrados en la lista vacía
    return data_list   # Se obtiene la lista resultante

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""
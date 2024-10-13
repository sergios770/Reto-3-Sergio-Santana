import time
import csv
import json
import os
from datetime import datetime

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {}
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    
    data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-2/'
    file_path = os.path.join(data_dir, filename)
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            id = row.get('id', 'Indefinido')
            if id != 'Indefinido':
                catalog[id] = {
                    'title': row.get('title', 'Indefinido'),
                    'original_language': row.get('original_language', 'Indefinido'),
                    'release_date': row.get('release_date', 'Indefinido'),
                    'revenue': row.get('revenue', 'Indefinido'),
                    'runtime': row.get('runtime', 'Indefinido'),
                    'status': row.get('status', 'Indefinido'),
                    'vote_average': row.get('vote_average', 'Indefinido'),
                    'vote_count': row.get('vote_count', 'Indefinido'),
                    'budget': row.get('budget', 'Indefinido'),
                    'genres': json.loads(row.get('genres', '[]')),
                    'production_companies': json.loads(row.get('production_companies', '[]'))
                }
                
def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

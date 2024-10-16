import time
import json
import csv
import os
from datetime import datetime
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(root_dir)
from DataStructures.Map import map_linear_probing as mp

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {}
    
    num_elements = 1000  
    load_factor = 0.75    
    prime = 109345121
    
    catalog["movies"] = mp.new_map(num_elements, load_factor, prime)
    
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    
    data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-2/'
    file_path = os.path.join(data_dir, filename)
   
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
    
        for row in csv_reader:
            
            movie_id = row.get('id')
            
            movie_data = {
                'original_language': row.get('original_language', 'Indefinido'),
                'release_date': row.get('release_date', 'Indefinido'),
                'revenue': row.get('revenue', 'Indefinido'),
                'runtime': row.get('runtime', 'Indefinido'),
                'status': row.get('status', 'Indefinido'),
                'vote_average': row.get('vote_average', 'Indefinido'),
                'budget': row.get('budget', 'Indefinido'),
                'genres': json.loads(row.get('genres', '[]')),
                'production_companies': json.loads(row.get('production_companies', '[]'))
            }
            
            if movie_id:
                mp.put(catalog['movies'], movie_id, movie_data)
                
catalog = new_logic()
load_data(catalog, "movies-large.csv")
print(catalog)

                
def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    if id in catalog:
        return {
            'id': id,
            'original_language': catalog[id].get('original_language', 'Indefinido'),
            'release_date': catalog[id].get('release_date', 'Indefinido'),
            'revenue': catalog[id].get('revenue', 'Indefinido'),
            'runtime': catalog[id].get('runtime', 'Indefinido'),
            'status': catalog[id].get('status', 'Indefinido'),
            'vote_average': catalog[id].get('vote_average', 'Indefinido'),
            'vote_count': catalog[id].get('vote_count', 'Indefinido'),
            'budget': catalog[id].get('budget', 'Indefinido'),
            'genres': catalog[id].get('genres', ['Indefinido']),
            'production_companies': catalog[id].get('production_companies', ['Indefinido'])}

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

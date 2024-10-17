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
from DataStructures.List import array_list as lt

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {}
    
    num_elements = 1000  
    load_factor = 0.75    
    prime = 109345121
    
    catalog = mp.new_map(num_elements, load_factor, prime)
    
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
            
            id = row.get('id')
            
            movie_data = {
                'budget': row.get('budget', 'Indefinido'),
                'genres': json.loads(row.get('genres', '[]')),
                'original_language': row.get('original_language', 'Indefinido'),
                'popularity': row.get('popularity', 'Indefinido'),
                'production_companies': json.loads(row.get('production_companies', '[]')),
                'release_date': row.get('release_date', 'Indefinido'),
                'revenue': row.get('revenue', 'Indefinido'),
                'runtime': row.get('runtime', 'Indefinido'),
                'status': row.get('status', 'Indefinido'),
                'title': row.get('title', 'Indefinido'),
                'vote_average': row.get('vote_average', 'Indefinido'),
                'vote_count': row.get('vote_count', 'Indefinido'),
                }
            
            if id:
                mp.put(catalog, id, movie_data)
                
catalog = new_logic()
load_data(catalog, "movies-small.csv")
"print(catalog)"

                
def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    movie = mp.get(catalog, id)
    
    if movie:
        return movie['value']
    else:
        return None

def req_1(catalog, title, original_language):
    """
    Retorna el resultado del requerimiento 1
    """
    movies = mp.value_set(catalog)
    
    for movie in movies['elements']:
        if movie['title'].lower() == title.lower() and movie['original_language'].lower() == original_language.lower():
            movie['gains'] = int(movie['revenue']) - int(movie['budget']) if movie['revenue'] != 'Indefinido' and movie['revenue'] != 'Indefinido' else 'Indefinido'
            return movie
        
    return None
    
    

print(req_1(catalog, 'BMX Bandits', 'en' ))


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
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

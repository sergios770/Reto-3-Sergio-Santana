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
            
            id = row.get('title', 'Indefinido')

            if id not in catalog:
                catalog[id] = {}
                
            catalog[id]['original_language'] = row.get('original_language', 'Indefinido')
            
            date_str = row.get('release_date', 'Indefinido')
            if date_str != 'Desconocido' and len(date_str) == 10:
                formatted_date = date_str
            else:
                formatted_date = 'Indefinido'
            catalog[id]['release_date'] = formatted_date

            revenue = row.get('revenue', 'Indefinido')
            catalog[id]['revenue'] = revenue if revenue != '0' else 'Indefinido'

            runtime = row.get('runtime', 'Indefinido')
            catalog[id]['runtime'] = runtime if runtime != '[]' else 'Indefinido'

            status = row.get('status', 'Indefinido')
            catalog[id]['status'] = status if status != '[]' else 'Indefinido'

            vote_average = row.get('vote_average', 'Indefinido')
            catalog[id]['vote_average'] = vote_average if vote_average != '[]' else 'Indefinido'

            vote_count = row.get('vote_count', 'Indefinido')
            catalog[id]['vote_count'] = vote_count if vote_count != '[]' else 'Indefinido'

            budget = row.get('budget', 'Indefinido')
            catalog[id]['budget'] = budget if budget != '0' else 'Indefinido'

            genres_str = row.get('genres', '[]')
            genres_list = json.loads(genres_str)
            if genres_list:
                genres_processed = [genre['name'] for genre in genres_list if 'name' in genre]
                catalog[id]['genres'] = genres_processed
            else:
                catalog[id]['genres'] = ['Desconocido']

            production_companies_str = row.get('production_companies', '[]')
            production_companies_list = json.loads(production_companies_str)
            if production_companies_list:
                companies_processed = [company['name'] for company in production_companies_list if 'name' in company]
                catalog[id]['production_companies'] = companies_processed
            else:
                catalog[id]['production_companies'] = ['Indefinida']

                
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

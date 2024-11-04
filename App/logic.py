import time
import csv
import json
from DataStructures.Maps import map_linear_probing as lp
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll
from datetime import datetime

def new_logic():
    """
    Crea el catálogo para almacenar las estructuras de datos
    """
    catalog = {
        "accidents": {
            "elements": al.new_array_list(),
            "index": lp.new_map()
        }
    }
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto desde un archivo CSV y los agrega al catálogo.
    """
    moviesfile = data_dir + 'accidents-' + filename + ".csv"
    input_file = csv.DictReader(open(moviesfile, encoding='utf-8'))
    for accident in input_file:
        add_accident(catalog, accident)
    for accident in catalog["accidents"]["elements"]:
        for variable in accident:
            if accident[variable] == "":
                accident[variable] = "desconocido"
    
    tamaño_catalog = accident_size(catalog)
    return tamaño_catalog

def add_accident(catalog, accident):
    """
    Agrega un accidente al catálogo.
    """
    al.add_last(catalog["accidents"]["elements"], accident)
    lp.put(catalog["accidents"]["index"], accident['ID'], accident)

# Funciones de consulta sobre el catálogo

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    data = lp.get(catalog["accidents"]["index"], id)
    if data is not None:
        return data
    else:
        return "Accidente no encontrado"


def req_1(catalog, fecha_1, fecha_2):
    """
    Retorna los accidentes ocurridos en un rango de fechas, mostrando los primeros 5 y los últimos 5 más recientes.
    """
    accidentes = []
    formato_fecha = "%Y-%m-%d %H:%M:%S"
    
    for accident in catalog["accidents"]["elements"]:
        fecha_inicio = datetime.strptime(accident['Start_Time'], formato_fecha)
        
        if fecha_1 <= fecha_inicio <= fecha_2:
            fecha_fin = datetime.strptime(accident['End_Time'], formato_fecha)
            diferencia_horas = (fecha_fin - fecha_inicio).total_seconds() / 3600
            descripcion = accident['Description'][:40] + "..." if len(accident['Description']) > 40 else accident['Description']
            info = {
                "ID del accidente": accident['ID'],
                "Fecha y hora del accidente": accident['Start_Time'],
                "Ciudad y estado": accident['City'] + ", " + accident['State'],
                "Descripción del accidente": descripcion,
                "Tiempo de duración del accidente": diferencia_horas
            }
            accidentes.append(info)

    # Ordenar los accidentes por fecha de inicio de forma descendente
    accidentes.sort(key=lambda x: datetime.strptime(x["Fecha y hora del accidente"], formato_fecha), reverse=True)

    # Limitar el resultado a los primeros 5 y últimos 5
    if len(accidentes) > 10:
        accidentes = accidentes[:5] + accidentes[-5:]

    return {
        "total_accidentes": len(accidentes),
        "accidentes": accidentes
    }



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

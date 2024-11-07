from DataStructures.List import array_list as lt
import csv
import os
from datetime import datetime
from collections import defaultdict

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'
csv.field_size_limit(2147483647)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog_list = {"accidents": None}
    catalog_list["accidents"] = lt.new_list()    
    return catalog_list 

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    moviesfile = data_dir + 'accidents-' + filename + ".csv"
    input_file = csv.DictReader(open(moviesfile, encoding='utf-8'))
    for accident in input_file:
        add_accident(catalog, accident)
    for accident in catalog["accidents"]["elements"]:
        for variables in accident:
            if accident[variables] == "":
                accident[variables] = "desconocido"
    tamaño_catalog = accident_size(catalog)
    
    return tamaño_catalog

def accident_size(catalog):
    return lt.size(catalog["accidents"])

def add_accident(catalog, accident):
    lt.add_last(catalog['accidents'], accident)
    return catalog

# Funciones de consulta sobre el catálogo

def obtener_primeras_5(catalog):
    accidentes = []
    firsts = lt.sub_list(catalog["accidents"], 0, 5)
    for accident in firsts["elements"]:
        formato_fecha = "%Y-%m-%d %H:%M:%S"
        fecha1 = accident["Start_Time"]
        fecha2 = accident["End_Time"]
        datetime1 = datetime.strptime(fecha1, formato_fecha)
        datetime2 = datetime.strptime(fecha2, formato_fecha)
        diferencia_horas = (datetime2 - datetime1).total_seconds() / 3600
        info = {
            "ID del accidente": accident["ID"], 
            "Fecha y hora del accidente": accident["Start_Time"],
            "Ciudad y estado": accident["City"] + ", " + accident["State"],
            "Descripción del accidente": accident["Description"],
            "Tiempo de duración del accidente": diferencia_horas
        }
        accidentes.append(info)
    return accidentes

def obtener_ultimas_5(catalog):
    accidentes = []
    last_five = lt.sub_list(catalog["accidents"], lt.size(catalog["accidents"]) - 5, 5)
    for accident in last_five["elements"]:
        formato_fecha = "%Y-%m-%d %H:%M:%S"
        fecha1 = accident["Start_Time"]
        fecha2 = accident["End_Time"]
        datetime1 = datetime.strptime(fecha1, formato_fecha)
        datetime2 = datetime.strptime(fecha2, formato_fecha)
        diferencia_horas = (datetime2 - datetime1).total_seconds() / 3600
        info = {
            "ID del accidente": accident["ID"], 
            "Fecha y hora del accidente": accident["Start_Time"],
            "Ciudad y estado": accident["City"] + ", " + accident["State"],
            "Descripción del accidente": accident["Description"],
            "Tiempo de duración del accidente": diferencia_horas
        }
        accidentes.append(info)
    return accidentes



def compare_by_fecha_and_severity(accident1, accident2):
    fecha1 = datetime.strptime(accident1["Start_Time"], "%Y-%m-%d %H:%M:%S")
    fecha2 = datetime.strptime(accident2["Start_Time"], "%Y-%m-%d %H:%M:%S")
    
    if fecha1 < fecha2:
        return False
    elif fecha1 > fecha2:
        return True
    else:
        return float(accident1["Severity"]) > float(accident2["Severity"])
    
def compare_by_lat_long(accident1, accident2):
    lat1_start = accident1["Start_Lat"] if accident1["Start_Lat"] != "desconocido" else None
    long1_start = accident1["Start_Lng"] if accident1["Start_Lng"] != "desconocido" else None
    lat1_end = accident1["End_Lat"] if accident1["End_Lat"] != "desconocido" else None
    long1_end = accident1["End_Lng"] if accident1["End_Lng"] != "desconocido" else None
    lat2_start = accident2["Start_Lat"] if accident2["Start_Lat"] != "desconocido" else None
    long2_start = accident2["Start_Lng"] if accident2["Start_Lng"] != "desconocido" else None
    lat2_end = accident2["End_Lat"] if accident2["End_Lat"] != "desconocido" else None
    long2_end = accident2["End_Lng"] if accident2["End_Lng"] != "desconocido" else None
    if lat1_start is not None and lat2_start is not None:
        if float(lat1_start) < float(lat2_start):
            return True
        elif float(lat1_start) > float(lat2_start):
            return False
    if long1_start is not None and long2_start is not None:
        if float(long1_start) < float(long2_start):
            return True
        elif float(long1_start) > float(long2_start):
            return False
    if lat1_end is not None and lat2_end is not None:
        if float(lat1_end) < float(lat2_end):
            return True
        elif float(lat1_end) > float(lat2_end):
            return False
    if long1_end is not None and long2_end is not None:
        if float(long1_end) < float(long2_end):
            return True
        elif float(long1_end) > float(long2_end):
            return False
    return False

def ordenar_alfabeticamente(accident1, accident2):
    if accident1.get("State", "") > accident2.get("State", ""):
        return True
    elif accident1.get("State", "") < accident2.get("State", ""):
        return False
    if accident1.get("county", "") > accident2.get("county", ""):
        return True
    elif accident1.get("county", "") < accident2.get("county", ""):
        return False
    if accident1.get("City", "") > accident2.get("City", ""):
        return True
    elif accident1.get("City", "") < accident2.get("City", ""):
        return False
    if accident1.get("Street", "") > accident2.get("Street", ""):
        return True
    
    else:
        return False

def comparar_accidentes(ac1, ac2):
    if ac1["total_accidentes"] > ac2["total_accidentes"]:
            return True
    elif ac1["total_accidentes"] == ac2["total_accidentes"]:
        return ac1["promedio_severidad"] > ac2["promedio_severidad"]
    else:
        return False

def prom_visibility(catalog):
    contador = 0
    sumatoria = 0
    for accident in catalog["accidents"]["elements"]:
        visibility = accident.get("Visibility(mi)", "desconocido")
        if visibility != "desconocido":
            sumatoria += float(visibility)
            contador += 1
    return sumatoria / contador if contador > 0 else 0  

def prom_severity(catalog):
    contador = 0
    sumatoria = 0
    for accident in catalog["accidents"]["elements"]:
        severity = accident.get("Severity", "desconocido")
        sumatoria += int(severity)
        contador += 1
    return sumatoria / contador if contador > 0 else 0 

def calcular_duracion_en_horas(fecha_inicio, fecha_fin):
    """
    Calcula la duración en horas entre la fecha de inicio y la fecha de fin.
    """
    formato_fecha = "%Y-%m-%d %H:%M:%S" 
    inicio = datetime.strptime(fecha_inicio, formato_fecha)
    fin = datetime.strptime(fecha_fin, formato_fecha)
    duracion_horas = (fin - inicio).total_seconds() / 3600
    return duracion_horas

# Funciones para medir tiempos de ejecucion




# Funciones de consulta sobre el catálogo

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    data = lt.get(catalog["accidents"]["index"], id)
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
                "Tiempo de duración del accidente": diferencia_horas,
                "Severidad": int(accident['Severity'])
            }
            accidentes.append(info)

    # Ordenar los accidentes por fecha de inicio descendente y luego por severidad descendente
    accidentes.sort(key=lambda x: (datetime.strptime(x["Fecha y hora del accidente"], formato_fecha), x["Severidad"]), reverse=True)

    # Limitar el resultado a los primeros 5 y últimos 5 si hay más de 10
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


def req_4(catalog, fecha_inicio, fecha_fin):
    """
    Requerimiento 4: Encuentra las vías más peligrosas en condiciones de baja visibilidad y alta severidad.
    """
    Severidad3 = lt.new_list()
    Severidad4 = lt.new_list()
    combinar = lt.new_list()
    vias_dict = defaultdict(lambda: {"accidents_severity_3": 0, "accidents_severity_4": 0, "total_visibility": 0, "total_severity": 0, "count": 0})
    for accident in catalog["accidents"]["elements"]:
        fecha_accidente = datetime.strptime(accident["Start_Time"], "%Y-%m-%d %H:%M:%S")
        if fecha_inicio <= fecha_accidente <= fecha_fin:
            visibility = float(accident["Visibility(mi)"]) if accident["Visibility(mi)"] != "desconocido" else 0
            severity = int(accident["Severity"])
            if visibility < 1 and severity in [3, 4]:
                key = (accident["State"], accident["County"], accident["City"], accident["Street"])
                
                if severity == 3:
                    vias_dict[key]["accidents_severity_3"] += 1
                    lt.add_last(Severidad3, accident)
                elif severity == 4:
                    vias_dict[key]["accidents_severity_4"] += 1
                    lt.add_last(Severidad4, accident)
                
                vias_dict[key]["total_visibility"] += visibility
                vias_dict[key]["total_severity"] += severity
                vias_dict[key]["count"] += 1
                
                lt.add_last(combinar, accident)

    for via in vias_dict.values():
        if via["count"] > 0:
            via["avg_visibility"] = via["total_visibility"] / via["count"]
            via["avg_severity"] = via["total_severity"] / via["count"]
        else:
            via["avg_visibility"] = 0
            via["avg_severity"] = 0
    
    lt.merge_sort(combinar, ordenar_alfabeticamente)
    
    promedio_V = sum([via["avg_visibility"] for via in vias_dict.values()]) / len(vias_dict) if len(vias_dict) > 0 else 0
    promedio_severidad = sum([via["avg_severity"] for via in vias_dict.values()]) / len(vias_dict) if len(vias_dict) > 0 else 0
    
   

    return Severidad3, Severidad4, promedio_V, promedio_severidad,combinar, vias_dict 



def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

from datetime import datetime

from datetime import datetime

def req_6(catalog, fecha_inicio, fecha_fin, humedad, condados):
    """
    Retorna el resultado del requerimiento 6
    """
    accidentes = lt.new_list()
    todo = catalog["accidents"]["elements"]
    formato_fecha = "%Y-%m-%d %H:%M:%S"
    
    for acc in todo:
        # Convertir Start_Time a datetime antes de la comparación
        fecha_accidente = datetime.strptime(acc["Start_Time"], formato_fecha)
        
        # Verificar si la humedad es un valor válido y si cumple con las condiciones
        if acc["Humidity(%)"] != "desconocido" and float(acc["Humidity(%)"]) >= humedad:
            if fecha_inicio <= fecha_accidente <= fecha_fin and acc["County"] in condados:
                lt.add_last(accidentes, acc)
    
    condado_info = {}
    for acc in accidentes["elements"]:
        condado = acc["County"]
        if condado not in condado_info:
            condado_info[condado] = {
                "total_accidentes": 0,
                "suma_temperatura": 0,
                "suma_humedad": 0,
                "suma_viento": 0,
                "suma_distancia": 0,
                "accidente_mas_grave": None,
                "max_severidad": 0,
                "accidentes": lt.new_list()
            }
        condado_info[condado]["total_accidentes"] += 1
        
        # Convertir y acumular valores si son válidos, de lo contrario ignorarlos
        if acc["Temperature(F)"] != "desconocido":
            condado_info[condado]["suma_temperatura"] += float(acc["Temperature(F)"])
        if acc["Humidity(%)"] != "desconocido":
            condado_info[condado]["suma_humedad"] += float(acc["Humidity(%)"])
        if acc["Wind_Speed(mph)"] != "desconocido":
            condado_info[condado]["suma_viento"] += float(acc["Wind_Speed(mph)"])
        if acc["Distance(mi)"] != "desconocido":
            condado_info[condado]["suma_distancia"] += float(acc["Distance(mi)"])
        
        lt.add_last(condado_info[condado]["accidentes"], acc)
        
        if int(acc["Severity"]) > condado_info[condado]["max_severidad"]:
            condado_info[condado]["max_severidad"] = int(acc["Severity"])
            condado_info[condado]["accidente_mas_grave"] = acc

    respuesta = []
    for condado, info in condado_info.items():
        promedio_temperatura = info["suma_temperatura"] / info["total_accidentes"]
        promedio_humedad = info["suma_humedad"] / info["total_accidentes"]
        promedio_viento = info["suma_viento"] / info["total_accidentes"]
        promedio_distancia = info["suma_distancia"] / info["total_accidentes"]
        accidente_grave = info["accidente_mas_grave"]
        
        lt.merge_sort(info["accidentes"], compare_by_fecha_and_severity)
        
        respuesta.append({
            "condado": condado,
            "total_accidentes": info["total_accidentes"],
            "promedio_temperatura": promedio_temperatura,
            "promedio_humedad": promedio_humedad,
            "promedio_viento": promedio_viento,
            "promedio_distancia": promedio_distancia,
            "accidente_mas_grave": {
                "ID": accidente_grave["ID"],
                "fecha_inicio": accidente_grave["Start_Time"],
                "temperatura": accidente_grave["Temperature(F)"],
                "humedad": accidente_grave["Humidity(%)"],
                "distancia": accidente_grave["Distance(mi)"],
                "descripcion": accidente_grave["Description"]
            },
            "accidentes": info["accidentes"]["elements"]
        })

    respuesta.sort(key=lambda x: x["total_accidentes"], reverse=True)
    
    return respuesta


    


def req_7(catalog, latitud_m, longitud_m, latitud_M, longitud_M):
    """
    Retorna el resultado del requerimiento 7
    """
    

    
    accidentes = lt.new_list()
    
    for accident in catalog["accidents"]["elements"]:
        if accident["Start_Lat"] != "desconocido" and accident["Start_Lng"] != "desconocido":
            if float(accident["Start_Lat"]) < latitud_M and float(accident["Start_Lat"]) > latitud_m and float(accident["Start_Lng"]) < longitud_M and float(accident["Start_Lng"]) > longitud_m:
                lt.add_last(accidentes,accident)
    
    lt.merge_sort(accidentes,compare_by_lat_long)
    tamaño = lt.size(accidentes)
    respuesta = []
    if lt.size(accidentes)>10:
        respuesta = accidentes["elements"][:5] + accidentes["elements"][-5:]
    else:
        respuesta = accidentes["elements"]
        

    
    return respuesta, tamaño


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion


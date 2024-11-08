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
    lat1_start = float(accident1["Start_Lat"]) if accident1["Start_Lat"] != "desconocido" else None
    long1_start = float(accident1["Start_Lng"]) if accident1["Start_Lng"] != "desconocido" else None
    lat1_end = float(accident1["End_Lat"]) if accident1["End_Lat"] != "desconocido" else None
    long1_end = float(accident1["End_Lng"]) if accident1["End_Lng"] != "desconocido" else None

    lat2_start = float(accident2["Start_Lat"]) if accident2["Start_Lat"] != "desconocido" else None
    long2_start = float(accident2["Start_Lng"]) if accident2["Start_Lng"] != "desconocido" else None
    lat2_end = float(accident2["End_Lat"]) if accident2["End_Lat"] != "desconocido" else None
    long2_end = float(accident2["End_Lng"]) if accident2["End_Lng"] != "desconocido" else None

    if lat1_start is not None and lat2_start is not None and lat1_start != lat2_start:
        return lat1_start < lat2_start
    if long1_start is not None and long2_start is not None and long1_start != long2_start:
        return long1_start < long2_start
    if lat1_end is not None and lat2_end is not None and lat1_end != lat2_end:
        return lat1_end < lat2_end
    if long1_end is not None and long2_end is not None and long1_end != long2_end:
        return long1_end < long2_end

    return False






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
    Retorna los accidentes ocurridos en un rango de fechas, mostrando los primeros 5 y los últimos 5 ordenados cronológicamente.
    """
    formato_fecha = "%Y-%m-%d %H:%M:%S"
    accidentes = []

    for accident in catalog["accidents"]["elements"]:
        fecha_inicio = datetime.strptime(accident['Start_Time'], formato_fecha)
        
        if fecha_1 <= fecha_inicio <= fecha_2:
            fecha_fin = datetime.strptime(accident['End_Time'], formato_fecha)
            diferencia_horas = (fecha_fin - fecha_inicio).total_seconds() / 3600
            descripcion = accident['Description'][:40] + "..." if len(accident['Description']) > 40 else accident['Description']
            accidentes.append({
                "ID del accidente": accident['ID'],
                "Fecha y hora del accidente": accident['Start_Time'],
                "Ciudad y estado": accident['City'] + ", " + accident['State'],
                "Descripción del accidente": descripcion,
                "Tiempo de duración del accidente": diferencia_horas,
                "Severidad": int(accident['Severity'])
            })

    total_accidentes = len(accidentes)

    accidentes.sort( key=lambda x: (datetime.strptime(x["Fecha y hora del accidente"], formato_fecha), -x["Severidad"]),reverse=True)

    if total_accidentes > 10:
        accidentes = accidentes[:5] + accidentes[-5:]

    return {
        "total_accidentes": total_accidentes,
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
    # Diccionario para almacenar los datos de las vías
    vias_dict = defaultdict(lambda: {
        "accidents_severity_3": 0,
        "accidents_severity_4": 0,
        "total_visibility": 0,
        "total_severity": 0,
        "count": 0
    })
    
    # Filtrar y acumular datos de accidentes por rango de fechas, visibilidad y severidad
    for accident in catalog["accidents"]["elements"]:
        fecha_accidente = datetime.strptime(accident["Start_Time"], "%Y-%m-%d %H:%M:%S")
        
        if fecha_inicio <= fecha_accidente <= fecha_fin:
            visibility = float(accident["Visibility(mi)"]) if accident["Visibility(mi)"] != "desconocido" else 0
            severity = int(accident["Severity"])
            
            if visibility < 1 and severity in [3, 4]:
                key = (accident["State"], accident["County"], accident["City"], accident["Street"])
                
                # Actualizar información en el diccionario de vías
                vias_dict[key]["count"] += 1
                vias_dict[key]["total_visibility"] += visibility
                vias_dict[key]["total_severity"] += severity
                
                if severity == 3:
                    vias_dict[key]["accidents_severity_3"] += 1
                elif severity == 4:
                    vias_dict[key]["accidents_severity_4"] += 1

    # Calcular promedios de visibilidad y severidad por vía
    for via in vias_dict.values():
        via["avg_visibility"] = via["total_visibility"] / via["count"] if via["count"] > 0 else 0
        via["avg_severity"] = via["total_severity"] / via["count"] if via["count"] > 0 else 0

    # Crear lista de vías ordenadas alfabéticamente para combinar
    combinar = sorted(
        [{"State": key[0], "County": key[1], "City": key[2], "Street": key[3], **via_data}
         for key, via_data in vias_dict.items()],
        key=lambda x: (x["State"], x["County"], x["City"], x["Street"])
    )

    # Calcular promedios generales
    promedio_visibilidad = sum(via["avg_visibility"] for via in vias_dict.values()) / len(vias_dict) if vias_dict else 0
    promedio_severidad = sum(via["avg_severity"] for via in vias_dict.values()) / len(vias_dict) if vias_dict else 0

    # Listas de accidentes separados por severidad
    Severidad3 = [acc for acc in catalog["accidents"]["elements"] if int(acc["Severity"]) == 3 and acc["Visibility(mi)"] != "desconocido" and float(acc["Visibility(mi)"]) < 1]
    Severidad4 = [acc for acc in catalog["accidents"]["elements"] if int(acc["Severity"]) == 4 and acc["Visibility(mi)"] != "desconocido" and float(acc["Visibility(mi)"]) < 1]

    return Severidad3, Severidad4, promedio_visibilidad, promedio_severidad, combinar, vias_dict




def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass



def req_6(catalog, fecha_inicio, fecha_fin, humedad, condados):
    """
    Retorna el resultado del requerimiento 6
    """
    formato_fecha = "%Y-%m-%d %H:%M:%S"
    
    # Filtrar accidentes que cumplen con las condiciones de fecha, humedad y condado
    accidentes = [
        acc for acc in catalog["accidents"]["elements"]
        if (fecha_inicio <= datetime.strptime(acc["Start_Time"], formato_fecha) <= fecha_fin) and
           (acc["Humidity(%)"] != "desconocido" and float(acc["Humidity(%)"]) >= humedad) and
           (acc["County"] in condados)
    ]
    
    # Diccionario para almacenar datos agregados de cada condado
    condado_info = defaultdict(lambda: {
        "total_accidentes": 0,
        "suma_temperatura": 0,
        "suma_humedad": 0,
        "suma_viento": 0,
        "suma_distancia": 0,
        "accidente_mas_grave": None,
        "max_severidad": 0,
        "accidentes": []
    })
    
    # Acumular información de cada accidente en el diccionario por condado
    for acc in accidentes:
        condado = acc["County"]
        condado_info[condado]["total_accidentes"] += 1
        condado_info[condado]["suma_temperatura"] += float(acc["Temperature(F)"]) if acc["Temperature(F)"] != "desconocido" else 0
        condado_info[condado]["suma_humedad"] += float(acc["Humidity(%)"]) if acc["Humidity(%)"] != "desconocido" else 0
        condado_info[condado]["suma_viento"] += float(acc["Wind_Speed(mph)"]) if acc["Wind_Speed(mph)"] != "desconocido" else 0
        condado_info[condado]["suma_distancia"] += float(acc["Distance(mi)"]) if acc["Distance(mi)"] != "desconocido" else 0
        condado_info[condado]["accidentes"].append(acc)
        
        # Determinar el accidente más grave
        severity = int(acc["Severity"])
        if severity > condado_info[condado]["max_severidad"]:
            condado_info[condado]["max_severidad"] = severity
            condado_info[condado]["accidente_mas_grave"] = acc

    respuesta = []
    for condado, info in condado_info.items():
        total_accidentes = info["total_accidentes"]
        promedio_temperatura = info["suma_temperatura"] / total_accidentes if total_accidentes > 0 else 0
        promedio_humedad = info["suma_humedad"] / total_accidentes if total_accidentes > 0 else 0
        promedio_viento = info["suma_viento"] / total_accidentes if total_accidentes > 0 else 0
        promedio_distancia = info["suma_distancia"] / total_accidentes if total_accidentes > 0 else 0
        accidente_grave = info["accidente_mas_grave"]
        
        info["accidentes"].sort(key=lambda x: (x["Start_Time"], -int(x["Severity"])))
        
        respuesta.append({
            "condado": condado,
            "total_accidentes": total_accidentes,
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
            "accidentes": info["accidentes"]
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


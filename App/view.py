import sys
from tabulate import tabulate
import App.logic as logic
from datetime import datetime

def new_logic():
    """
    Se crea una instancia del controlador
    """
    return logic.new_logic()

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos de accidentes en el catálogo y muestra las primeras y últimas cinco entradas
    """
    tamaño_catalogo = logic.load_data(control, 'small')  # 'large' es el sufijo del archivo CSV

    # Obtener las primeras 5 entradas
    print("Primeros cinco accidentes cargados:\n")
    table = []
    primeros_accidentes = logic.obtener_primeras_5(control)
    for accident in primeros_accidentes:
        id_accidente = accident["ID del accidente"]
        fecha_hora = accident["Fecha y hora del accidente"]
        ciudad_estado = accident["Ciudad y estado"]
        descripcion = accident["Descripción del accidente"][:40]  # Máximo 40 caracteres
        duracion = round(accident["Tiempo de duración del accidente"], 2)
        data = [id_accidente, fecha_hora, ciudad_estado, descripcion, duracion]
        table.append(data)
    
    headers = ["ID", "Fecha y Hora de Inicio", "Ciudad y Estado", "Descripción", "Duración (horas)"]
    print(tabulate(table, headers=headers, tablefmt="outline"))

    # Obtener las últimas 5 entradas
    print("\nÚltimos cinco accidentes cargados:\n")
    table = []
    ultimos_accidentes = logic.obtener_ultimas_5(control)
    for accident in ultimos_accidentes:
        id_accidente = accident["ID del accidente"]
        fecha_hora = accident["Fecha y hora del accidente"]
        ciudad_estado = accident["Ciudad y estado"]
        descripcion = accident["Descripción del accidente"][:40]  # Máximo 40 caracteres
        duracion = round(accident["Tiempo de duración del accidente"], 2)
        data = [id_accidente, fecha_hora, ciudad_estado, descripcion, duracion]
        table.append(data)
    
    print(tabulate(table, headers=headers, tablefmt="outline"))
    print(f"\nEl archivo fue cargado exitosamente. Total de accidentes cargados: {tamaño_catalogo}")





def print_data(accidents, columnas):
    """
    Imprime los detalles de una lista de accidentes
    """
    tabla = []
    for accident in accidents["elements"]:
        accidente_auxiliar = {}
        for columna in columnas:
            accidente_auxiliar[columna] = accident[columna]
        tabla.append(accidente_auxiliar)
    print(tabulate(tabla, headers="keys", tablefmt="grid"))



def print_req_1(control):
    """
    Función que imprime la solución del Requerimiento 1 en consola.
    """
    # Solicitar al usuario las fechas de inicio y fin
    fecha_inicio_str = input("Ingrese la fecha de inicio en formato YYYY-MM-DD HH:MM:SS: ")
    fecha_fin_str = input("Ingrese la fecha final en formato YYYY-MM-DD HH:MM:SS: ")

    # Convertir las fechas de string a objetos datetime
    formato_fecha = "%Y-%m-%d %H:%M:%S"
    fecha_inicio = datetime.strptime(fecha_inicio_str, formato_fecha)
    fecha_fin = datetime.strptime(fecha_fin_str, formato_fecha)

    # Llamar a la función req_1 y obtener los resultados
    resultado = logic.req_1(control, fecha_inicio, fecha_fin)

    # Preparar los datos para la tabla
    headers = ["ID", "Fecha y Hora del Accidente", "Ciudad y Estado", "Descripción", "Duración (horas)"]
    table = []
    for accident in resultado["accidentes"]:
        data = [
            accident["ID del accidente"],
            accident["Fecha y hora del accidente"],
            accident["Ciudad y estado"],
            accident["Descripción del accidente"],
            round(accident["Tiempo de duración del accidente"], 2)
        ]
        table.append(data)
    
    # Imprimir la tabla usando tabulate
    print(f"\nTotal de accidentes en el rango de fechas: {resultado['total_accidentes']}")
    print("Accidentes más recientes y más antiguos en el rango especificado:")
    print(tabulate(table, headers=headers, tablefmt="outline"))



def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
    Función que imprime la solución del Requerimiento 4 en consola.
    """
    # Solicitar al usuario las fechas de inicio y fin
    fecha_inicio_str = input("Ingrese la fecha de inicio en formato YYYY-MM-DD HH:MM:SS: ")
    fecha_fin_str = input("Ingrese la fecha final en formato YYYY-MM-DD HH:MM:SS: ")

    # Convertir las fechas de string a objetos datetime
    formato_fecha = "%Y-%m-%d %H:%M:%S"
    fecha_inicio = datetime.strptime(fecha_inicio_str, formato_fecha)
    fecha_fin = datetime.strptime(fecha_fin_str, formato_fecha)

    # Llamar a la función req_4 y obtener los resultados
    Severidad3, Severidad4, promedio_V, promedio_severidad, combinar, vias_dict = logic.req_4(control, fecha_inicio, fecha_fin)

    # Preparar la tabla para mostrar la información de cada vía
    headers = ["Estado", "Condado", "Ciudad", "Nombre de la vía", "Peligrosidad (Prom. Severidad)",
               "Accidentes Severidad 3", "Accidentes Severidad 4", "Visibilidad Promedio"]
    table = []
    
    for key, via in sorted(vias_dict.items(), key=lambda x: (x[0][0], x[0][1], x[0][2], x[0][3])):  # Ordenar alfabéticamente
        data = [
            key[0],  # Estado
            key[1],  # Condado
            key[2],  # Ciudad
            key[3],  # Nombre de la vía
            round(via["avg_severity"], 2),  # Peligrosidad (Promedio de severidad)
            via["accidents_severity_3"],  # Total accidentes severidad 3
            via["accidents_severity_4"],  # Total accidentes severidad 4
            round(via["avg_visibility"], 2)  # Visibilidad promedio
        ]
        table.append(data)

    # Imprimir la tabla usando tabulate
    print("\nVías identificadas en el rango de fechas:")
    print(tabulate(table, headers=headers, tablefmt="outline"))

    # Mostrar promedios generales de visibilidad y severidad
    print(f"\nPromedio de Visibilidad de todas las vías: {promedio_V:.2f}")
    print(f"Promedio de Severidad de todas las vías: {promedio_severidad:.2f}")



def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass




def print_req_6(control):
    """
    Función que imprime la solución del Req0
    uerimiento 6 en consola.
    """
    # Solicitar al usuario las fechas de inicio y fin
    fecha_inicio_str = input("Ingrese la fecha de inicio en formato YYYY-MM-DD HH:MM:SS: ")
    fecha_fin_str = input("Ingrese la fecha final en formato YYYY-MM-DD HH:MM:SS: ")
    
    # Solicitar la humedad mínima y la lista de condados
    humedad = float(input("Ingrese el nivel mínimo de humedad: "))
    condados_str = input("Ingrese la lista de condados separados por comas: ")
    condados = [c.strip() for c in condados_str.split(",")]

    # Convertir las fechas de string a objetos datetime
    formato_fecha = "%Y-%m-%d %H:%M:%S"
    fecha_inicio = datetime.strptime(fecha_inicio_str, formato_fecha)
    fecha_fin = datetime.strptime(fecha_fin_str, formato_fecha)

    # Llamar a la función req_6 y obtener los resultados
    resultado = logic.req_6(control, fecha_inicio, fecha_fin, humedad, condados)

    # Preparar la tabla para mostrar la información de cada condado
    headers = ["Condado", "Total Accidentes", "Prom. Temperatura (°F)", "Prom. Humedad (%)", 
               "Prom. Viento (mph)", "Prom. Distancia (mi)", "Accidente Más Grave (ID, Fecha, Descripción)"]
    table = []
    
    for info in resultado:
        accidente_grave = info["accidente_mas_grave"]
        data = [
            info["condado"],
            info["total_accidentes"],
            round(info["promedio_temperatura"], 2),
            round(info["promedio_humedad"], 2),
            round(info["promedio_viento"], 2),
            round(info["promedio_distancia"], 2),
            f"{accidente_grave['ID']}, {accidente_grave['fecha_inicio']}, {accidente_grave['descripcion'][:40]}..."
        ]
        table.append(data)

    # Imprimir la tabla usando tabulate
    print("\nInformación de los condados con accidentes bajo las condiciones especificadas:")
    print(tabulate(table, headers=headers, tablefmt="outline"))

    # Mostrar lista de accidentes ordenados por cada condado (opcional)
    for info in resultado:
        print(f"\nDetalles de accidentes en el condado: {info['condado']}")
        accidentes_headers = ["ID", "Fecha", "Temperatura (°F)", "Humedad (%)", "Viento (mph)", "Distancia (mi)", "Descripción"]
        accidentes_table = [
            [
                acc["ID"],
                acc["Start_Time"],
                acc["Temperature(F)"],
                acc["Humidity(%)"],
                acc["Wind_Speed(mph)"],
                acc["Distance(mi)"],
                acc["Description"][:40] + "..."
            ]
            for acc in info["accidentes"]
        ]
        print(tabulate(accidentes_table, headers=accidentes_headers, tablefmt="outline"))





def print_req_7(control):
    """
    Función que imprime la solución del Requerimiento 7 en consola.
    """
    # Solicitar al usuario las coordenadas de latitud y longitud
    latitud_m = float(input("Ingrese la latitud mínima: "))
    longitud_m = float(input("Ingrese la longitud mínima: "))
    latitud_M = float(input("Ingrese la latitud máxima: "))
    longitud_M = float(input("Ingrese la longitud máxima: "))

    # Llamar a la función req_7 y obtener los resultados
    accidentes, tamaño = logic.req_7(control, latitud_m, longitud_m, latitud_M, longitud_M)

    # Preparar los datos para mostrar la información de cada accidente
    headers = ["ID", "Fecha y Hora del Accidente", "Latitud", "Longitud", "Ciudad", "Estado", "Descripción"]
    table = []
    
    for accident in accidentes:
        data = [
            accident["ID"],
            accident["Start_Time"],
            accident["Start_Lat"],
            accident["Start_Lng"],
            accident["City"],
            accident["State"],
            accident["Description"][:40] + "..."  # Limitar la descripción a 40 caracteres
        ]
        table.append(data)

    # Imprimir el número total de accidentes y los resultados en formato tabulado
    print(f"\nTotal de accidentes en el área especificada: {tamaño}")
    print("Detalles de los primeros y últimos accidentes en el área especificada:")
    print(tabulate(table, headers=headers, tablefmt="outline"))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

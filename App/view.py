import sys
from tabulate import tabulate 
from DataStructures.List import array_list as lt
import App.logic as logic
from datetime import datetime
import os
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

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

from tabulate import tabulate

def load_data(control):
    """
    Carga los datos de accidentes en el catálogo y muestra las primeras y últimas cinco entradas
    """
    # Cargar los datos usando la función de lógica
    tamaño_catalogo = logic.load_data(control, 'large')  # 'large' es el sufijo del archivo CSV

    # Obtener las primeras 5 entradas
    print("Primeros cinco accidentes cargados:\n")
    table = []
    primeros_accidentes = logic.obtener_primeras_5(control)
    for accident in primeros_accidentes:
        id_accidente = accident["ID del accidente"]
        fecha_hora = accident["Fecha y hora del accidente"]
        ciudad_estado = accident["Ciudad y estado"]
        descripcion = accident["Descripcin del accidente"][:40]  # Máximo 40 caracteres
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
        descripcion = accident["Descripcin del accidente"][:40]  # Máximo 40 caracteres
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
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


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
    fecha_inicio = input("Ingrese la fecha de inicio en formato YYYY-MM-DD HH:MM:SS: ")
    fecha_fin = input("Ingrese la fecha final en formato YYYY-MM-DD HH:MM:SS: ")
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M:%S")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d %H:%M:%S")

    # Llamada a la función req_4 y obtención de los resultados
    Severidad3, Severidad4, promedio_V, promedio_severidad, tiempo, combinar, vias_dict = logic.req_4(control, fecha_inicio, fecha_fin)

    # Encabezados de la tabla
    headers = ["Estado", "Condado", "Ciudad", "Nombre de la vía", "Peligrosidad",
               "Total accidentes severidad 3", "Total accidentes severidad 4", "Visibilidad promedio"]
    
    # Preparar datos en el formato correcto
    data = [
        [
            key[0],  # Estado
            key[1],  # Condado
            key[2],  # Ciudad
            key[3],  # Nombre de la vía
            round(via["accidents_severity_3"] + via["accidents_severity_4"], 2),  # Peligrosidad
            via["accidents_severity_3"],  # Total accidentes severidad 3
            via["accidents_severity_4"],  # Total accidentes severidad 4
            round(via["avg_visibility"], 2)  # Visibilidad promedio
        ]
        for key, via in sorted(vias_dict.items(), key=lambda x: (x[0][0], x[0][1], x[0][2], x[0][3]))  # Ordenar alfabéticamente
    ]
    
    # Imprimir la tabla usando tabulate
    print("\nVías identificadas en el rango de fechas:")
    print(tabulate(data, headers=headers, tablefmt="grid"))
    print(f"\nTiempo de ejecución: {tiempo:.2f} segundos")



def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


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

def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad.

    :param datos_temperaturas: Diccionario donde las claves son los nombres de las ciudades
                               y los valores son listas de listas con temperaturas semanales.
    :return: Diccionario con las temperaturas promedio por ciudad.
    """
    promedios = {}

    for ciudad, semanas in datos_temperaturas.items():
        temperaturas_totales = sum([sum(semana) for semana in semanas])
        cantidad_dias = sum([len(semana) for semana in semanas])
        promedio_ciudad = temperaturas_totales / cantidad_dias
        promedios[ciudad] = promedio_ciudad

    return promedios


# Datos de ejemplo (temperaturas en grados Celsius)
datos_temperaturas = {
    "Quito": [[30, 32, 31, 29, 28, 30, 31], [29, 28, 27, 26, 30, 31, 32], [28, 27, 26, 25, 29, 30, 31],
              [27, 26, 25, 24, 28, 29, 30]],
    "Guayaquil": [[15, 17, 16, 14, 13, 15, 16], [14, 13, 12, 11, 15, 16, 17], [13, 12, 11, 10, 14, 15, 16],
                  [12, 11, 10, 9, 13, 14, 15]],
    "Cuenca": [[22, 24, 23, 21, 20, 22, 23], [21, 20, 19, 18, 22, 23, 24], [20, 19, 18, 17, 21, 22, 23],
               [19, 18, 17, 16, 20, 21, 22]]
}

# Llamada a la función y mostrar resultados
promedios = calcular_temperatura_promedio(datos_temperaturas)
for ciudad, promedio in promedios.items():
    print(f"Temperatura promedio en {ciudad}: {promedio:.2f}°C")

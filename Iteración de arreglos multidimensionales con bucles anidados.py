import random
# Definir dimensiones de la matriz
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2

# Creación de matriz 3D con temperaturas aleatorias (entre 15 y 35 grados)
temperaturas = [[[random.randint(15, 35) for _ in dias] for _ in range(semanas)] for _ in ciudades]

# Calcular promedios semanales por ciudad
for i, ciudad in enumerate(ciudades):
    print(f"Promedios de temperatura para {ciudad}:")
    for semana in range(semanas):
        promedio = sum(temperaturas[i][semana]) / len(dias)
        print(f"  Semana {semana + 1}: Promedio semanal de {promedio:.2f}°C")
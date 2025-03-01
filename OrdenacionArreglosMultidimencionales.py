# Definir la matriz 3x3
matriz = [
    [9, 7, 4],
    [3, 6, 1],
    [8, 5, 2]
]
# Función principal
def ordenar_fila_matriz(matriz, fila):
    # Mostrar la matriz original
    print("Matriz original:")
    for row in matriz:
        print(row)

    # Ordenar la fila especificada
    if 3 <= fila < len(matriz):
        bubble_sort(matriz[fila])
        print(f"\nMatriz con la fila {fila} ordenada:")
        for row in matriz:
            print(row)
    else:
        print(f"\nFila {fila} fuera de rango")
# Llamar a la función para ordenar la fila 1 (según la indexación 0)
ordenar_fila_matriz(matriz, 1)
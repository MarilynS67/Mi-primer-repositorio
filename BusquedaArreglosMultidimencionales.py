#definimos la matriz 3*3
matriz = [
    [5, 8, 3],
    [4, 1, 9],
    [6, 7, 2]
]

def buscar_valor (matriz,valor):
   #recorrer y buscar el valor
   for i in range(len(matriz)):
       for j in range(len(matriz[i])):
          if matriz[i][j]==valor:
             return i,j #retorna la posicion


   return None

#solicito el valor a buscar
numero_buscar= 4

#llamo a la funcion
resultado = buscar_valor(matriz,numero_buscar)

if resultado:
    print(f"el resultado del numero {numero_buscar} se encuentra en la posicion  {resultado[0]} {resultado[1]} ")
else:
    print(f"el resultado no se encontro en la matriz")



#ordenacion arreglo
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
# 25. Niveles de infección (propagación), modelar cómo se propaga una infección desde un punto inicial,
#     asumiendo que en cada paso se propaga a vecinos.
#   - BFS ayuda a calcular el tiempo total de propagación.

from collections import deque

def mostrar_matriz_simbolos(matriz):
    print("\nMatriz actual:")
    for fila in matriz:
        print(" ".join(fila))
    print()

def mostrar_matriz_infeccion(matriz):
    print("\nMatriz con tiempos de infección:")
    for fila in matriz:
        fila_mostrada = []
        for celda in fila:
            if celda == -2:
                fila_mostrada.append('P')  # Pared
            elif celda == -1:
                fila_mostrada.append('.')  # No infectada
            else:
                fila_mostrada.append(str(celda))  # Tiempo de infección
        print(" ".join(fila_mostrada))
    print()

def pedir_infecciones(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    mostrar_matriz_simbolos(matriz)

    print("Ingresa coordenadas de infección inicial (ej: 1,2). Escribe 'fin' para terminar")
    while True:
        entrada = input("Posición de infección: ").strip().lower()
        if entrada == "fin":
            break
        try:
            f, c = map(int, entrada.split(','))
            if not (0 <= f < filas and 0 <= c < columnas):
                print("Fuera de rango")
            elif matriz[f][c] == 'P':
                print("No se puede infectar una pared")
            else:
                matriz[f][c] = 'I'
                print(f"Infección inicial en ({f}, {c})")
        except:
            print("Entrada inválida")

def BFS_infeccion(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    tiempo = [[-1] * columnas for _ in range(filas)]
    cola = deque()
    direcciones = [(-1,0), (1,0), (0,-1), (0,1)]

    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] == 'I':
                tiempo[f][c] = 0
                cola.append((f, c))
            elif matriz[f][c] == 'P':
                tiempo[f][c] = -2

    max_tiempo = 0
    while cola:
        f, c = cola.popleft()
        for df, dc in direcciones:
            nf, nc = f + df, c + dc
            if 0 <= nf < filas and 0 <= nc < columnas:
                if matriz[nf][nc] == 'L' and tiempo[nf][nc] == -1:
                    tiempo[nf][nc] = tiempo[f][c] + 1
                    max_tiempo = max(max_tiempo, tiempo[nf][nc])
                    cola.append((nf, nc))
    return max_tiempo, tiempo


matriz = [
    ['L', 'L', 'P', 'L'],
    ['L', 'L', 'L', 'L'],
    ['P', 'L', 'L', 'P'],
    ['L', 'L', 'L', 'L']
]

pedir_infecciones(matriz)
tiempo_total, matriz_tiempo = BFS_infeccion(matriz)

print(f"\nTiempo total de propagación: {tiempo_total}")
mostrar_matriz_infeccion(matriz_tiempo)
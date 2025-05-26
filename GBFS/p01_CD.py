#41. Buscar en un laberinto con celda objetivo-conocida, usar GBFS con una heurística Manhattan para llegar a una celda destino.
#   - Matriz con paredes (1) y caminos (0).

from queue import PriorityQueue

# Heurística: Distancia Manhattan
def heuristica(actual, destino):
    return abs(actual[0] - destino[0]) + abs(actual[1] - destino[1])

# Verifica las celdas vecinas válidas (que no son paredes)
def obtener_vecinos(celda, laberinto):
    fila, columna = celda
    movimientos = [(1,0), (-1,0), (0,1), (0,-1)]
    vecinos = []

    for mov_fila, mov_col in movimientos:
        nueva_fila = fila + mov_fila
        nueva_col = columna + mov_col

        if 0 <= nueva_fila < len(laberinto) and 0 <= nueva_col < len(laberinto[0]):
            if laberinto[nueva_fila][nueva_col] == 0:  # 0 = camino libre
                vecinos.append((nueva_fila, nueva_col))
    
    return vecinos

# Reconstruye el camino desde el destino al inicio
def reconstruir_camino(came_from, actual):
    camino = [actual]
    while actual in came_from:
        actual = came_from[actual]
        camino.append(actual)
    camino.reverse()
    return camino

# Algoritmo GBFS
def GreedyBestFirstSearch(laberinto, inicio, destino):
    cola_prioridad = PriorityQueue()
    cola_prioridad.put((heuristica(inicio, destino), inicio)) #enqueue
    
    visitado = set()
    came_from = {}

    while not cola_prioridad.empty():
        _, actual = cola_prioridad.get() #dequeue

        if actual == destino:
            return reconstruir_camino(came_from, actual)

        visitado.add(actual)

        for vecino in obtener_vecinos(actual, laberinto):
            if vecino not in visitado:
                came_from[vecino] = actual
                cola_prioridad.put((heuristica(vecino, destino), vecino))
    
    return None


laberinto = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

celda_inicio = (0, 0)
celda_destino = (2, 4)

camino = GreedyBestFirstSearch(laberinto, celda_inicio, celda_destino)

if camino:
    print("Camino encontrado:")
    for paso in camino:
        print(paso)
else:
    print("No hay camino disponible")
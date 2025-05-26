# 44. Resolver laberinto con portales o llaves (espacio de estados complejo), usar GBFS para llegar al
#     objetivo considerando celdas especiales que reducen distancias.

from queue import PriorityQueue

# Movimientos posibles: 4 direcciones
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

PORTAL = 'P'
INICIO = 'S'
META = 'E'
PARED = '#'

# Función heurística: distancia de Manhattan
def heuristica(fila, col, meta):
    return abs(fila - meta[0]) + abs(col - meta[1])

# Validar si una celda es accesible
def es_valido(fila, col, visitado):
    if 0 <= fila < len(laberinto) and 0 <= col < len(laberinto[0]):
        # La celda debe ser libre o un portal
        if laberinto[fila][col] != PARED:
            return not visitado[fila][col]
    return False

def GreedyBestFirstSearch(laberinto, inicio, meta):
    visitado = [[False] * len(laberinto[0]) for _ in range(len(laberinto))]
    cola_prioridad = PriorityQueue()

    # Inicializamos la cola con el inicio
    fila, col = inicio
    cola_prioridad.put((0, fila, col))  # (heurística, fila, col)
    visitado[fila][col] = True

    while not cola_prioridad.empty():
        _, fila, col = cola_prioridad.get()

        if (fila, col) == meta:
            return True

        # Probar los 4 movimientos posibles
        for mov_fila, mov_col in movimientos:
            nueva_fila, nueva_col = fila + mov_fila, col + mov_col
            if es_valido(nueva_fila, nueva_col, visitado):
                # Si encontramos un portal, nos teletransportamos
                if laberinto[nueva_fila][nueva_col] == PORTAL:
                    # Verificamos las condiciones para teletransportar
                    if (nueva_fila, nueva_col) == (6, 2):  # Portal en fila 6, col 2
                        nueva_fila, nueva_col = 1, 4  # Teletransporte al portal 1, 4
                        print(f"Te teletransportaste con el portal desde (6, 2) a: ({nueva_fila}, {nueva_col})")
                    elif (nueva_fila, nueva_col) == (4, 6):  # Portal en fila 4, col 6
                        nueva_fila, nueva_col = 1, 8  # Teletransporte al portal 1, 8
                        print(f"Te teletransportaste con el portal desde (4, 6) a: ({nueva_fila}, {nueva_col})")
                
                # Calculamos la heurística (distancia de Manhattan)
                heur = heuristica(nueva_fila, nueva_col, meta)
                visitado[nueva_fila][nueva_col] = True
                cola_prioridad.put((heur, nueva_fila, nueva_col))

    return False


laberinto = [
    ['S', '.', '.', '.', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '.', '#', '.', '.', '.', '#', '.', '#'],
    ['#', '.', '.', '#', '#', '#', '.', '#', '.', '#'],
    ['#', '#', '.', '.', '.', '#', '.', '#', '.', '#'],
    ['#', '#', '#', '#', '.', '#', 'P', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '#', '#', '#', '.', 'E'],
    ['.', '#', 'P', '#', '#', '#', '#', '#', '#', '#']
]

# Definir el inicio (S) y la meta (E)
inicio = (0, 0)  # S
meta = (5, 9)    # E

resultado = GreedyBestFirstSearch(laberinto, inicio, meta)

if resultado:
    print("✅ Meta alcanzada")
else:
    print("❌ Meta no alcanzada")
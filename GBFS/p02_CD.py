# 42. Búsqueda de palabra en una cuadrícula (tipo Boggle), Buscar una palabra específica en un tablero
#     de letras, guiándose por proximidad al final de la palabra.

from queue import PriorityQueue

# Movimientos posibles: 8 direcciones (vertical, horizontal y diagonal)
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# Heurística: Distancia Manhattan entre una celda y la próxima letra de la palabra
def heuristica(fila, col, siguiente_letra, tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == siguiente_letra:
                return abs(i - fila) + abs(j - col)
    return float('inf')

def es_valido(fila, col, tablero, visitado):
    return 0 <= fila < len(tablero) and 0 <= col < len(tablero[0]) and not visitado[fila][col]

def GreedyBestFirstSearch(tablero, palabra):
    visitado = [[False] * len(tablero[0]) for _ in range(len(tablero))]
    
    cola_prioridad = PriorityQueue()

    for fila in range(len(tablero)):
        for col in range(len(tablero[0])):
            if tablero[fila][col] == palabra[0]:
                cola_prioridad.put((0, fila, col, 0))  # (heurística, fila, col, índice de letra en la palabra)
                visitado[fila][col] = True

    while not cola_prioridad.empty():
        _, fila, col, idx = cola_prioridad.get()

        if idx == len(palabra) - 1:
            return True

        siguiente_letra = palabra[idx + 1]

        for mov_fila, mov_col in movimientos:
            nueva_fila, nueva_col = fila + mov_fila, col + mov_col
            if es_valido(nueva_fila, nueva_col, tablero, visitado) and tablero[nueva_fila][nueva_col] == siguiente_letra:
                heur = heuristica(nueva_fila, nueva_col, siguiente_letra, tablero)
                visitado[nueva_fila][nueva_col] = True
                cola_prioridad.put((heur, nueva_fila, nueva_col, idx + 1))

    return False


tablero = [
    ['T', 'R', 'E', 'E'],
    ['A', 'P', 'P', 'L'],
    ['E', 'P', 'P', 'I'],
    ['L', 'E', 'R', 'S']
]

palabra = "APPLE"
resultado = GreedyBestFirstSearch(tablero, palabra)

if resultado:
    print("✅ Palabra encontrada")
else:
    print("❌ Palabra no encontrada")

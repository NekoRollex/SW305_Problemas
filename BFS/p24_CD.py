# 24. Escape del laberinto, dada una matriz de 0 (libre) y 1 (pared), encuentra el número mínimo de
#     pasos para ir del punto A al punto B.

from collections import deque

def BFS_laberinto(laberinto, inicio, fin):
    filas = len(laberinto)
    columnas = len(laberinto[0])
    
    movimientos = [(-1,0), (1,0), (0,-1), (0,1)]
    
    distancia = [[-1]*columnas for _ in range(filas)]
    
    fila_inicio, col_inicio = inicio
    fila_fin, col_fin = fin
    
    cola = deque()
    cola.append((fila_inicio, col_inicio))
    distancia[fila_inicio][col_inicio] = 0
    
    while cola:
        fila, col = cola.popleft()
        
        if (fila, col) == (fila_fin, col_fin):
            return distancia[fila][col]
        
        for df, dc in movimientos:
            n_fila, n_col = fila + df, col + dc
            if 0 <= n_fila < filas and 0 <= n_col < columnas:
                if laberinto[n_fila][n_col] == 0 and distancia[n_fila][n_col] == -1:
                    distancia[n_fila][n_col] = distancia[fila][col] + 1
                    cola.append((n_fila, n_col))

    return -1


laberinto = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

inicio = (0, 0)
fin = (4, 4)

pasos_minimos = BFS_laberinto(laberinto, inicio, fin)
print("Número mínimo de pasos:", pasos_minimos)
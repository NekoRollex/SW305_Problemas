# 29. Islas en una matriz (Contar componentes conectados), dada una matriz de 0s y 1s, contar
#     cuántas islas (grupos conectados de 1s) hay usando BFS

from collections import deque

def BFS_islas(matriz, visitados, fila, col):
    filas, columnas = len(matriz), len(matriz[0])
    cola = deque()
    cola.append((fila, col))
    visitados[fila][col] = True
    
    direcciones = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while cola:
        f, c = cola.popleft()
        for df, dc in direcciones:
            nf, nc = f + df, c + dc
            if 0 <= nf < filas and 0 <= nc < columnas:
                if matriz[nf][nc] == 1 and not visitados[nf][nc]:
                    visitados[nf][nc] = True
                    cola.append((nf, nc))

def contar_islas(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    visitados = [[False]*columnas for _ in range(filas)]
    contador = 0
    
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 1 and not visitados[i][j]:
                BFS_islas(matriz, visitados, i, j)
                contador += 1
    return contador

matriz = [
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
]

print("Número de islas:", contar_islas(matriz))
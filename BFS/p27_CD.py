# 27. Resolver rompecabezas (como el 8-puzzle), Buscar la secuencia mínima de movimientos para alcanzar
#     una configuración objetivo.
#   - Cada estado del tablero es un nodo.

from collections import deque

def matriz_a_cadena(matriz):
    # Convertimos la matriz 3x3 en un string para guardar en visitados
    return ''.join(str(num) for fila in matriz for num in fila)

def obtener_pos_0(matriz):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 0:
                return i, j

def copiar_matriz(matriz):
    return [fila[:] for fila in matriz]

def generar_vecinos(matriz):
    vecinos = []
    i0, j0 = obtener_pos_0(matriz)
    movimientos = [(-1,0),(1,0),(0,-1),(0,1)]
    
    for di, dj in movimientos:
        ni, nj = i0 + di, j0 + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            nueva = copiar_matriz(matriz)
            nueva[i0][j0], nueva[ni][nj] = nueva[ni][nj], nueva[i0][j0]
            vecinos.append(nueva)
    return vecinos

def BFS_8puzzle(inicial, objetivo):
    inicial_cad = matriz_a_cadena(inicial)
    objetivo_cad = matriz_a_cadena(objetivo)
    
    queue = deque([(inicial, [])])
    visitados = set([inicial_cad])
    
    while queue:
        estado, path = queue.popleft()
        estado_cad = matriz_a_cadena(estado)
        
        if estado_cad == objetivo_cad:
            return path + [estado]
        
        for vecino in generar_vecinos(estado):
            vecino_cad = matriz_a_cadena(vecino)
            if vecino_cad not in visitados:
                visitados.add(vecino_cad)
                queue.append((vecino, path + [estado]))
    
    return None


estado_inicial = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]

estado_objetivo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solucion = BFS_8puzzle(estado_inicial, estado_objetivo)
if solucion:
    print(f"Solución encontrada en {len(solucion)-1} movimientos:")
    i = 0
    for paso in solucion:
        if i == 0:
            print("Estado inicial:")
            for fila in paso:
                print(fila)
            print("------")
        else:
            print(f"Paso {i}:")
            for fila in paso:
                print(fila)
            print("------")
        i += 1
else:
    print("No se encontró solución")
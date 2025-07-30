def DFS(Matriz: list, vistados: list, i: int, n: int):
    vistados[i] = True
    j = 0

    while j < n:
        if j != i:
            if (Matriz[i][j] != None) and (vistados[j] == False):
               DFS(Matriz, vistados, j, n)
        j += 1

def ContarComponentes(Matriz : list):
    n = len(Matriz)
    vistados = [False for i in range(n)]
    cont = 0
    n = len(Matriz)
    for i in range(n):
        if vistados[i] != True:
            DFS(Matriz, vistados, i, n)
            cont += 1
    
    return cont

MatrizAdyacencia = [
    [0, 1, None, None, None, None],
    [1, 0, 1, None, None, None],
    [None, 1, 0, None, None, None],
    [None, None, None, 0, 1, None],
    [None, None, None, 1, 0, None],
    [None, None, None, None, None, 0]
]

c = ContarComponentes(MatrizAdyacencia)

print(f"La cantidad de componenes del grafo es: {c}")
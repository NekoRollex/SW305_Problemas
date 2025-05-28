def FloydWarshall(Matriz):
    Dist = Matriz.copy()
    cont = 0
    i = Dist[0]
    while i != Dist[-1]:
        cont += 1
        i = Dist[cont]
    cont += 1

    k = 0

    while k < cont:
        i = 0
        while i < cont:
            j = 0
            while j < cont:
                if Dist[i][j] == None:
                    if (Dist[i][k] != None) and (Dist[k][j] != None):
                        Dist[i][j] = Dist[i][k] + Dist[k][j]
                else:
                    if (Dist[i][k] != None) and (Dist[k][j] != None):
                        if  Dist[i][j] > Dist[i][k] + Dist[k][j]:
                            Dist[i][j] = Dist[i][k] + Dist[k][j]
                j += 1
            i += 1
        k += 1
    return Dist

MatrizAdyacencia = [[0, 3, None, 7], [8, 0, 2, None], [5, None, 0, 1], [2, None, None, 0]]

MatrizDistancias = FloydWarshall(MatrizAdyacencia)
print("La matriz de Distancias mínimas es: ")
print(MatrizDistancias)

print(f"\nLa distancia minima entre A y C es: {MatrizDistancias[0][2]}")
# 14. Partición de conjunto con diferencia mínima
#   - Dividir un conjunto de enteros en dos subconjuntos de suma lo más igual posible.
#	- Poda: Si una rama lleva a una diferencia mayor que la mejor actual, se elimina.

def particion_minima_diferencia(numeros):
    n = len(numeros)
    mejor_diferencia = [float('inf')]
    mejor_particion = [[], []]

    def backtracking(i, suma1, suma2, subconjunto1, subconjunto2):
        if i == n:
            diferencia = abs(suma1 - suma2)
            if diferencia < mejor_diferencia[0]:
                mejor_diferencia[0] = diferencia
                mejor_particion[0] = subconjunto1[:]
                mejor_particion[1] = subconjunto2[:]
            return

        if abs(suma1 - suma2) >= mejor_diferencia[0]:
            return

        subconjunto1.append(numeros[i])
        backtracking(i + 1, suma1 + numeros[i], suma2, subconjunto1, subconjunto2)
        subconjunto1.pop()

        subconjunto2.append(numeros[i])
        backtracking(i + 1, suma1, suma2 + numeros[i], subconjunto1, subconjunto2)
        subconjunto2.pop()

    backtracking(0, 0, 0, [], [])

    print("Subconjuntos:", mejor_particion[0], "y", mejor_particion[1])
    print("Diferencia mínima:", mejor_diferencia[0])


numeros = [3, 1, 4, 2, 2, 1, 6, 7, 3, 4, 2]
#nums = [1, 6, 11, 5]
particion_minima_diferencia(numeros)
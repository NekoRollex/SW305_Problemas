# 3. Generar todas las permutaciones de una lista de números, No es estrictamente un árbol, pero el espacio de búsqueda puede representarse como un árbol de decisiones.
#   - Cada nivel representa una posición en la permutación.

def permutaciones(numeros):
    resultado = []
    backtracking(numeros, [], [False] * len(numeros), resultado)
    return resultado

def backtracking(numeros, camino_actual, usado, resultado):
    if len(camino_actual) == len(numeros):
        resultado.append(list(camino_actual))
        return

    for i in range(len(numeros)):
        if not usado[i]:
            usado[i] = True
            camino_actual.append(numeros[i])

            backtracking(numeros, camino_actual, usado, resultado)

            camino_actual.pop()
            usado[i] = False


numeros = [1, 2, 3]
permutaciones_generadas = permutaciones(numeros)

for permutacion in permutaciones_generadas:
    print(permutacion)
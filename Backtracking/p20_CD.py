# 20. Permutaciones restringidas
#   - Generar todas las permutaciones de un conjunto que cumplan ciertas reglas (por ejemplo, no repetir patrones).
#   - Poda: Si una regla se viola, no se sigue construyendo esa permutación.

def permutaciones_restringidas(numeros):
    resultado = []
    numeros.sort()
    n = len(numeros)
    visitado = [False] * n

    def backtracking(actual):
        if len(actual) == n:
            resultado.append(actual[:])
            return

        for i in range(n):
            if visitado[i]:
                continue

            if i > 0 and numeros[i] == numeros[i - 1] and not visitado[i - 1]:
                continue

            if actual and actual[-1] == 1 and numeros[i] == 2:
                continue

            visitado[i] = True
            actual.append(numeros[i])
            backtracking(actual)
            actual.pop()
            visitado[i] = False

    backtracking([])
    return resultado


numeros = [1, 2, 3, 4, 6, 2, 3]
permutaciones = permutaciones_restringidas(numeros)

for permutacion in permutaciones:
    print(permutacion)
print("Total:", len(permutaciones))
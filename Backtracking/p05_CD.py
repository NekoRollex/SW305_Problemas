# 5. Árbol de decisiones para combinaciones con restricción, dado un conjunto de números y un objetivo,
#    encuentra todas las combinaciones que suman el objetivo.
#   - Similar al problema "Combinación Sum" de LeetCode.

def combinaciones_con_objetivo(numeros, objetivo):
    soluciones = []
    backtracking(numeros, objetivo, [], 0, soluciones)
    return soluciones

def backtracking(numeros, objetivo, combinacion_actual, indice, soluciones):
    if sum(combinacion_actual) == objetivo:
        soluciones.append(combinacion_actual.copy())
        return

    if sum(combinacion_actual) > objetivo:
        return

    for i in range(indice, len(numeros)):
        combinacion_actual.append(numeros[i])
        backtracking(numeros, objetivo, combinacion_actual, i, soluciones)
        combinacion_actual.pop()


numeros = [2, 3, 6, 7]
objetivo = int(input("Ingrese el valor objetivo: "))
soluciones = combinaciones_con_objetivo(numeros, objetivo)

print(f"Las combinaciones que suman {objetivo} son:")
for solucion in soluciones:
    print(solucion)
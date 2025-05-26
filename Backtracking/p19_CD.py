# 19. Asignación de tareas con costo mínimo (Assignment Problem)
#   - Asignar N tareas a N personas minimizando el costo total.
#   - Poda: Si la suma actual del costo supera el mínimo global, se descarta.

def asignacion_tareas_minimo(costo):
    n = len(costo)
    visitado = [False] * n
    mejor_costo = [float('inf')]
    mejor_asignacion = [None]
    asignacion_actual = [None] * n

    def backtracking(tarea_actual, suma_actual):
        if tarea_actual == n:
            if suma_actual < mejor_costo[0]:
                mejor_costo[0] = suma_actual
                mejor_asignacion[0] = asignacion_actual[:]
            return

        if suma_actual >= mejor_costo[0]:
            return

        for persona in range(n):
            if not visitado[persona]:
                visitado[persona] = True
                asignacion_actual[tarea_actual] = persona
                backtracking(tarea_actual + 1, suma_actual + costo[persona][tarea_actual])
                visitado[persona] = False

    backtracking(0, 0)
    return mejor_costo[0], mejor_asignacion[0]


costos = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

min_costo = asignacion_tareas_minimo(costos)
print("Costo mínimo de asignación:", min_costo)
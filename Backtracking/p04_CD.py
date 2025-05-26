# 4. N-Queens sobre árbol de decisiones, coloca N reinas en un tablero NxN sin que se ataquen entre sí.
#    Representa el árbol de soluciones donde cada nivel es una fila del tablero.
#   - Usa backtracking con poda por columnas y diagonales.

def n_queens(n):
    soluciones = []
    backtracking(0, n, [], set(), set(), set(), soluciones)
    return soluciones

def backtracking(fila, n, tablero, columnas, diag_pos, diag_neg, solucion):
    if fila == n:
        solucion.append(tablero.copy())
        return True

    for col in range(n):
        if col in columnas or (fila + col) in diag_pos or (fila - col) in diag_neg:
            continue

        tablero.append(col)
        columnas.add(col)
        diag_pos.add(fila + col)
        diag_neg.add(fila - col)

        if backtracking(fila + 1, n, tablero, columnas, diag_pos, diag_neg, solucion):
            return True

        tablero.pop()
        columnas.remove(col)
        diag_pos.remove(fila + col)
        diag_neg.remove(fila - col)

def mostrar_solucion(solucion, n):
    if solucion:
        for fila in solucion[0]:
            linea = ['.'] * n
            linea[fila] = '♕'
            print(' '.join(linea))
        print('-' * (2 * n - 1))


n = 8
if n<=0:
    print(f"No es posible mostrar solucion para {n}-Queens")
else:
    solucion = n_queens(n)
    if len(solucion) > 0:
        print(f"Se encontro solucion para {n}-Queens:")
        mostrar_solucion(solucion, n)
    else:
        print(f"No se encontro soluciones para {n}-Queens")
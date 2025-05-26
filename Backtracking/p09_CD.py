#9.	Sudoku Solver con árbol de opciones, cada nodo es una celda y el árbol representa las decisiones de posibles números.
#   - Requiere poda agresiva y validaciones en cada paso.

def imprimir_tablero(tablero):
    for fila in range(9):
        if fila % 3 == 0 and fila != 0:
            print("-" * 21)

        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")

            num = tablero[fila][col]
            if num == 0:
                print(".", end=" ")
            else:
                print(num, end=" ")
        print()

def resolver_sudoku(tablero):
    def es_valido(fila, col, num):
        for i in range(9):
            if tablero[fila][i] == num or tablero[i][col] == num:
                return False

        inicio_fila = (fila // 3) * 3
        inicio_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if tablero[inicio_fila + i][inicio_col + j] == num:
                    return False

        return True

    def backtracking():
        for fila in range(9):
            for col in range(9):
                if tablero[fila][col] == 0:
                    for num in range(1, 10):
                        if es_valido(fila, col, num):
                            tablero[fila][col] = num
                            if backtracking():
                                return True
                            tablero[fila][col] = 0
                    return False
        return True

    backtracking()


tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku original:\n")
imprimir_tablero(tablero)

resolver_sudoku(tablero)

print("\nSudoku resuelto:\n")
imprimir_tablero(tablero)
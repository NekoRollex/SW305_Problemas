# 18. Sudoku Solver Mejorado
#   - Resolver un tablero de Sudoku usando Backtracking + validaciones parciales.
#   - Poda: Si en la celda actual no hay opciones válidas, cortar.

def resolver_sudoku(tablero):
    filas = [set() for _ in range(9)]
    columnas = [set() for _ in range(9)]
    cajas = [[set() for _ in range(3)] for _ in range(3)]
    vacias = []

    for i in range(9):
        for j in range(9):
            num = tablero[i][j]
            if num != 0:
                filas[i].add(num)
                columnas[j].add(num)
                cajas[i // 3][j // 3].add(num)
            else:
                vacias.append((i, j))

    def poda(fila, col, num):
        return (
            num in filas[fila] or
            num in columnas[col] or
            num in cajas[fila // 3][col // 3]
        )

    def backtracking(indice):
        if indice == len(vacias):
            return True

        fila, col = vacias[indice]
        for num in range(1, 10):
            if not poda(fila, col, num):
                tablero[fila][col] = num
                filas[fila].add(num)
                columnas[col].add(num)
                cajas[fila // 3][col // 3].add(num)

                if backtracking(indice + 1):
                    return True

                tablero[fila][col] = 0
                filas[fila].remove(num)
                columnas[col].remove(num)
                cajas[fila // 3][col // 3].remove(num)

        return False

    backtracking(0)

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

tablero = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

print("Sudoku original:\n")
imprimir_tablero(tablero)

resolver_sudoku(tablero)

print("\nSudoku resuelto:\n")
imprimir_tablero(tablero)
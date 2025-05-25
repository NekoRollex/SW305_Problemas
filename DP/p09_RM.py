# dp[i][j] : camino de menor costo desde (0, 0) hasta (i, j)

m = int(input("m: "))
n = int(input("n: "))

costos = []

for i in range(m+1):
    lista = input(f"Ingrese los costos de la fila {i}: ").split()
    for i in range(n+1):
        lista[i] = int(lista[i])
    costos.append(lista)

dp = [[-1 for _ in range(n+1)] for __ in range(m+1)]

def Dp(i, j):
    if i == 0 and j == 0:
        return costos[0][0]
    if dp[i][j] != -1:
        return dp[i][j]
    if i == 0:
        dp[i][j] = Dp(i, j-1) + costos[i][j]
    elif j == 0:
        dp[i][j] = Dp(i-1, j) + costos[i][j]
    else:
        dp[i][j] = min(Dp(i, j-1), Dp(i-1, j)) + costos[i][j]
    return dp[i][j]

print("Costo mínimo:", Dp(m, n))
    
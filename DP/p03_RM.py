# dp[i][j] : número de formas de llegar desde (0, 0) a (i, j)
# 
# dp[i][j] = dp[i-1][j] + dp[i][j-1]

m = int(input("Número de filas: "))
n = int(input("Número de columnas: "))

dp = [[-1 for _ in range(n+1)] for __ in range(m+1)]
# dp[i][j] = -1 significa que no se ha calculado

def Dp(i, j):
    if i == 0 or j == 0:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = Dp(i-1, j) + Dp(i, j-1)
    return dp[i][j]

print("El número de formas es:", Dp(m, n))
# print(dp)

# 1  1  1  1  1
# 1  2  3  4  5
# 1  3  6 10 15
# 1  4 10 20 35
# 1  5 15 35 70
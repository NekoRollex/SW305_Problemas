# dp[i][w] : máximo valor que se puede obtener
#            con los primeros i objetos y un peso máximo de w
#
# dp[i][w] = max(dp[i-1][w], dp[i-1][w-pesos[i]] + valores[i])

n = int(input("Cantidad de objetos: "))
pesos = [0]*(n+1)
valores = [0]*(n+1)

# indexado en 1
for i in range(1, n+1):
    print(f"Objeto {i}")
    pesos[i] = int(input("Peso: "))
    valores[i] = int(input("Valor: "))

capacidad = int(input("Capacidad de la mochila: "))

dp = [[-1 for _ in range(capacidad+1)] for __ in range(n+1)]
# dp[i][w] = -1 significa que no se ha calculado

def Dp(i, w):
    if i == 0:
        return 0
    if dp[i][w] != -1:
        return dp[i][w]
    dp[i][w] = Dp(i-1, w)
    if pesos[i] <= w:
        dp[i][w] = max(dp[i][w], Dp(i-1, w-pesos[i]) + valores[i])
    return dp[i][w]

print("Máximo valor total:", Dp(n, capacidad))
# print(dp)

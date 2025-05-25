# dp[i][j] : longitud de la subsecuencia común más larga considerando
#            las primeras i letras de la primera cadena y
#            las primeras j letras de la segunda cadena
#

s = input("Primera cadena: ")
t = input("Segunda cadena: ")
n = len(s)
m = len(t)

dp = [[-1 for _ in range(m+1)] for __ in range(n+1)]

def Dp(i, j):
    if i == 0 or j == 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    # restamos 1 ya que está indexado en 0
    if s[i-1] == t[j-1]:
        dp[i][j] = Dp(i-1, j-1) + 1
    else:
        dp[i][j] = max(Dp(i, j-1), Dp(i-1, j))
    return dp[i][j]

Dp(n, m)

def get_lcs(i, j, lcs):
    if i == 0 or j == 0:
        return lcs
    if s[i-1] == t[j-1]:
        lcs = s[i-1] + lcs
        return get_lcs(i-1, j-1, lcs)
    elif dp[i-1][j] == dp[i][j]:
        return get_lcs(i-1, j, lcs)
    else:
        return get_lcs(i, j-1, lcs)

lcs = get_lcs(n, m, "")
print("LCS:", lcs)
print("Longitud:", dp[n][m])
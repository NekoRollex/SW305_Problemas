n = int(input("Cantidad de vértices: "))
m = int(input("Cantidad de aristas: "))
print("Ingresar las aristas")

adj = [[] for _ in range(n)]

for i in range(m):
    aux = input(f"Arista {i+1}: ").split()
    aux[0] = int(aux[0])
    aux[1] = int(aux[1])
    adj[aux[0]].append(aux[1])
    adj[aux[1]].append(aux[0])

vis = [False for _ in range(n)]

def dfs(u):
    vis[u] = True
    for v in adj[u]:
        if not vis[v]:
            dfs(v)

cc = 0
for i in range(n):
    if not vis[i]:
        dfs(i)
        cc += 1

print(f"Hay {cc} componentes conexas")

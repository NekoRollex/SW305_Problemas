# dis[i][j] : distancia mínima de i a j

inf = 1000000000
# se inicia con las aristas dirigidas
# 0 : es porque son del mismo vertice a si mismo
# inf : no hay arista dirigida entre esos vertices
dis = [[0, 3, inf, 7], [8, 0, 2, inf], [5, inf, 0, 1], [2, inf, inf, 0]]
n = len(dis)

for i in range(n):
    for j in range(n):
        for k in range(n):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    
for i in range(n):
    print(dis[i])

print("Ruta más corta de A a C es", dis[0][2])


# Union find = Disjoin set union
class Dsu:
    def __init__(self, n):
        self.t = [i for i in range(n)]

    # find() halla el identificador de la componente conexa
    def find(self, x):
        if self.t[x] == x:
            return x
        self.t[x] = self.find(self.t[x])
        return self.t[x]
    
    # join() combina dos componentes conexas
    def join(self, a, b):
        self.t[self.find(a)] = self.find(b)

# A B C D E F G H I J K -> 0 1 2 3 4 5 6 7 8 9 10
n = 11
dsu = Dsu(n)
# (a, b, peso)
aristas = []
aristas.append((0, 1, 8))
aristas.append((0, 10, 3))
aristas.append((0, 9, 12))
aristas.append((0, 8, 6))
aristas.append((0, 7, 10))
aristas.append((0, 6, 9))
aristas.append((1, 2, 10))
aristas.append((1, 4, 2))
aristas.append((1, 10, 7))
aristas.append((2, 10, 5))
aristas.append((2, 3, 9))
aristas.append((3, 4, 13))
aristas.append((3, 5, 12))
aristas.append((4, 5, 10))
aristas.append((4, 6, 6))
aristas.append((5, 6, 8))
aristas.append((6, 7, 7))
aristas.append((7, 8, 3))
aristas.append((8, 9, 10))
aristas.append((9, 10, 8))

m = len(aristas)

for i in range(m):
    for j in range(i+1, m):
        if aristas[i][2] > aristas[j][2]:
            aristas[i], aristas[j] = aristas[j], aristas[i]

indices = []
mst = 0
for i in range(m):
    a, b, w = aristas[i]
    # verificamos que no forme ciclo
    if dsu.find(a) != dsu.find(b):
        dsu.join(a, b)
        indices.append(i)
        mst += w

print("Aristas seleccionadas:")
for i in indices:
    a, b, w = aristas[i]
    print(a, "-", b, ":", w)

print("valor del mst:", mst)

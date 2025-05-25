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

# A B C D E F -> 0 1 2 3 4 5
n = 6
dsu = Dsu(n)
# (a, b, peso)
aristas = []
aristas.append((0, 1, 4))
aristas.append((0, 2, 2))
aristas.append((1, 2, 1))
aristas.append((1, 3, 5))
aristas.append((2, 3, 8))
aristas.append((2, 4, 10))
aristas.append((3, 4, 2))
aristas.append((3, 5, 6))
aristas.append((4, 5, 3))

m = len(aristas)

for i in range(m):
    for j in range(i+1, m):
        if aristas[i][2] > aristas[j][2]:
            aristas[i], aristas[j] = aristas[j], aristas[i]

def f(x):
    if x == 0:
        return 'A'
    elif x == 1:
        return 'B'
    elif x == 2:
        return 'C'
    elif x == 3:
        return 'D'
    elif x == 4:
        return 'E'
    else:
        return 'F'

mst = 0
for i in range(m):
    a, b, w = aristas[i]
    # verificamos que no forme ciclo
    if dsu.find(a) != dsu.find(b):
        dsu.join(a, b)
        print("La arista " + f(a) + "-" + f(b) + f":{w} se agrega al mst")
        mst += w
    else:
        print("La arista " + f(a) + "-" + f(b) + f":{w} genera un ciclo")

print("valor del mst:", mst)

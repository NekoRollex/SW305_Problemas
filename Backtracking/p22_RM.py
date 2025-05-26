class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
class Cola:
    def __init__(self):
        self.inicio = None
        self.final = None

    def enqueue(self, valor):
        nodo = Nodo(valor)
        if self.final is not None:
            self.final.siguiente = nodo
        self.final = nodo
        if self.inicio is None:
            self.inicio = nodo
    
    def dequeue(self):
        nodo = self.inicio
        if nodo is not None:
            self.inicio = nodo.siguiente

    def peek(self):
        if self.inicio is not None:
            return self.inicio.valor
        return None
            
    def is_empty(self):
        return self.inicio is None

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

s = int(input("Nodo inicial: "))
t = int(input("Nodo final: "))

inf = 1000000000
cola = Cola()
dis = [inf for _ in range(n)]
cola.enqueue(s)
dis[s] = 0

while not cola.is_empty():
    u = cola.peek()
    cola.dequeue()
    for v in adj[u]:
        if dis[v] == inf:
            dis[v] = dis[u] + 1
            cola.enqueue(v)

if dis[t] == inf:
    print(f"Los nodos {s} y {t} no están conectados")
else: 
    print(f"Distancia minima entre {s} y {t}: {dis[t]}")
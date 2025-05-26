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
    
a = int(input("Primer número: "))
b = int(input("Segundo número: "))

inf = 1000000000
dis = {a:0}
cola = Cola()
cola.enqueue(a)

while True:
    u = cola.peek()
    cola.dequeue()
    found = False
    for v in {u-1, 2*u}:
        if v not in dis.keys():
            if v == b:
                found = True
            dis[v] = dis[u] + 1
            cola.enqueue(v)
    if found:
        break

lista = [b]

while b != a:
    if b+1 in dis.keys() and dis[b+1]+1 == dis[b]:
        lista.append(b+1)
        b += 1
    else:
        lista.append(b//2)
        b = b//2

lista.reverse()

print("minimo numero de pasos:", dis[b])
print(lista)
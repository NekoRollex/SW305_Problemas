class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
class Pila:
    def __init__(self):
        self.cima = None

    def push(self, valor):
        nodo = Nodo(valor)
        nodo.siguiente = self.cima
        self.cima = nodo
    
    def pop(self):
        nodo = self.cima
        if not self.is_empty():
            self.cima = nodo.siguiente

    def peek(self):
        if not self.is_empty():
            return self.cima.valor
        return None
            
    def is_empty(self):
        return self.cima is None
    
    def print(self):
        nodo = self.cima
        while nodo is not None:
            print(nodo.valor, end=" -> ")
            nodo = nodo.siguiente
        print(end="\n")

pila_de_pilas = Pila()
n = int(input("Ingrese el número de pilas: "))

for i in range(n):
    m = int(input(f"Ingrese el tamaño de la pila {i+1}: "))
    pila = Pila()

    for j in range(m):
        valor = input(f"Ingrese el valor para la pila {i+1}: ")
        pila.push(valor)

    pila_de_pilas.push(pila)

print("Contenido de las pilas:")
for i in range(n):
    print(f"Pila {n-i}: ", end="")
    pila_de_pilas.peek().print()
    pila_de_pilas.pop()

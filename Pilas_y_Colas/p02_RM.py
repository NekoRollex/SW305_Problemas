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
        print("Pila: ", end="")
        while nodo is not None:
            print(nodo.valor, end=" -> ")
            nodo = nodo.siguiente
        print(end="\n")

pila = Pila()
n = int(input("Ingrese el tamaño de la pila: "))

for i in range(n):
    valor = input("Ingrese el valor: ")
    pila.push(valor)

pila.print()
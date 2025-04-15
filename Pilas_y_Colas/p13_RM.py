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

def eliminarRepetidosConsecutivos(pila):
    pila_aux = Pila()

    while not pila.is_empty():
        valor = pila.peek()
        if pila_aux.is_empty() or valor != pila_aux.peek():
            pila_aux.push(valor)
        pila.pop()
    
    while not pila_aux.is_empty():
        pila.push(pila_aux.peek())
        pila_aux.pop()

pila = Pila()
n = int(input("Ingrese el tamaño de la pila: "))

for i in range(n):
    valor = input("Ingrese el valor: ")
    pila.push(valor)

pila.print()
eliminarRepetidosConsecutivos(pila)
pila.print()
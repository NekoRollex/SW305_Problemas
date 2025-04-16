class NodoPila:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        
class Pila:
    def __init__(self):
        self.top = None

    def push(self, valor):
        nodo = NodoPila(valor)
        nodo.next = self.top
        self.top = nodo
    
    def pop(self):
        if not self.is_empty():
            nodo = self.top
            self.top = nodo.next

    def peek(self):
        if self.top is not None:
            return self.top.valor
        return None

    def is_empty(self):
        return self.top is None

    def print(self):
        nodo = self.top
        while nodo is not None:
            print(nodo.valor, end = (" -> " if nodo.next is not None else "\n"))
            nodo = nodo.next

    def clear(self):
        while not self.is_empty():
            self.pop()

p = Pila()

p.push(10)
p.push(20)
p.push(30)

print("Contenido de la pila antes de vaciarla:")
p.print()
p.clear()
print("Contenido de la pila después de vaciarla:")
p.print()

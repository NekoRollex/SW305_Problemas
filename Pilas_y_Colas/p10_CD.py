class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, valor):
        self.items.append(valor)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0
    
class Pila:
    def __init__(self):
        self.items = []

    def push(self, valor):
        self.items.append(valor)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("La pila esta vacia")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0
    
cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print(f"Cola actual: {cola.items}")

pila = Pila()

while not cola.is_empty():
    pila.push(cola.dequeue())

while not pila.is_empty():
    cola.enqueue(pila.pop())

print(f"Cola invertida: {cola.items}")
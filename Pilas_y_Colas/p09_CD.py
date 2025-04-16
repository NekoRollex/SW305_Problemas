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
    
    def contar(self):
        cont = 0
        for valor in self.items:
            cont += 1
        return cont

cola = Cola()

cola.enqueue("1")
cola.enqueue(2)
cola.enqueue("Hola")

print(f"Cantidad de elementos en la cola: {cola.contar()}")
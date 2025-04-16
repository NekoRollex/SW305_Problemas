class Pila:
    def __init__(self):
        self.items = []

    def push(self, valor):
        self.items.append(valor)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Algo salio mal")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0
    

pila = Pila()
print(f"Pila vacia: {pila.items}")

pila.push(10)
pila.push(20)
pila.push(30)

print(f"Pila luego de agregar elemento: {pila.items}")
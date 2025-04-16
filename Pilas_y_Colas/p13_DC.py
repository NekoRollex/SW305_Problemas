class Pila:
    def __init__(self):
        self.items = []

    def push(self, valor):
        self.items.append(valor)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def eliminar_duplicados_consecutivos(self):
        if self.is_empty():
            return
        temp_pila = Pila()
        temp_pila.push(self.pop()) 

        while not self.is_empty():
            top = self.pop()
            if temp_pila.peek() != top:
                temp_pila.push(top)
        
        while not temp_pila.is_empty():
            self.push(temp_pila.pop())

    def print(self):
        for item in reversed(self.items):
            print(item, end=" ")

pila = Pila()

pila.push(5)
pila.push(5)
pila.push(3)
pila.push(3)
pila.push(1)
pila.push(6)
pila.push(1)
pila.push(2)
pila.push(2)

print("Pila antes de eliminar duplicados consecutivos:")
pila.print()

pila.eliminar_duplicados_consecutivos()

print("\nPila después de eliminar duplicados consecutivos:")
pila.print()

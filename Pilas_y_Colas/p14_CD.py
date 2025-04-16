class NodoCola:
    def __init__ (self,valor):
        self.valor = valor
        self.punt = None

class ColaCircular:
    def __init__(self):
        self.pinicio = None
        self.pfinal = None

    def enqueue(self, valor):
        nuevo_nodo = NodoCola(valor)
        if self.is_empty():
            self.pinicio = nuevo_nodo
            self.pfinal = nuevo_nodo
            self.pfinal.punt = self.pinicio
        else:
            self.pfinal.punt = nuevo_nodo
            self.pfinal = nuevo_nodo
            self.pfinal.punt = self.pinicio

    def dequeue(self):
        if self.is_empty():
            raise IndexError("La cola está vacía.")
        
        valor = self.pinicio.valor
        if self.pinicio == self.pfinal:
            self.pinicio = None
            self.pfinal = None
        else:
            self.pinicio = self.pinicio.punt
            self.pfinal.punt = self.pinicio
        return valor

    def peek(self):
        if self.is_empty():
            raise IndexError("La cola está vacía.")
        return self.pinicio.valor

    def is_empty(self):
        return self.pinicio is None
    
    def imprimir(self):
        if self.is_empty():
            print("La cola está vacía.")
            return

        actual = self.pinicio
        print("Cola Circular:", end=" ")
        while True:
            print(actual.valor, end=" -> ")
            actual = actual.punt
            if actual == self.pinicio:
                break
        print("...")

cola = ColaCircular()

cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.imprimir()

print("Frente de la cola:", cola.peek())
print("Sacando:", cola.dequeue())
cola.imprimir()

print("Agregando mas elementos")
cola.enqueue(40)
cola.enqueue(50)
cola.imprimir() 

print("Frente de la cola:", cola.peek())
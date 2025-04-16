class Documento:
    def __init__(self, nombre, paginas):
        self.nombre = nombre
        self.paginas = paginas

    def __repr__(self):
        return f"Documento({self.nombre}, {self.paginas} páginas)"

class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, documento):
        self.items.append(documento)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0
    
    def imprimir(self):
        if self.is_empty():
            print("La cola está vacía.")
            return

        print("Cola de Documentos:")
        for documento in self.items:
            print(f"{documento.nombre} - {documento.paginas} páginas")

cola = Cola()

cola.enqueue(Documento("Documento1", 10))
cola.enqueue(Documento("Documento2", 20))
cola.enqueue(Documento("Documento3", 15))

print("Cola después de agregar documentos:")
cola.imprimir()

print("Frente de la cola:", cola.peek().nombre)

print("Imprimiendo:", cola.dequeue().nombre)

print("Cola después de imprimir un documento:")
cola.imprimir()

cola.enqueue(Documento("Documento4", 25))
cola.enqueue(Documento("Documento5", 30))

print("Cola final después de agregar más documentos:")
cola.imprimir()

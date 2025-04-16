import time
class Documento:
    def __init__(self, nombre, num_paginas):
        self.nombre = nombre
        self.num_paginas = num_paginas

class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, documento):
        self.items.append(documento)

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

    def mostrar(self):
        if self.is_empty():
            print("La cola está vacía")
            return

        documentos = []
        for doc in self.items:
            documentos.append(f"{doc.nombre} ({doc.num_paginas} páginas)")
        print("Cola de impresión:", end=" ")

        for i in range(len(documentos)):
            if i < len(documentos) - 1:
                print(documentos[i], end=" -> ")
            else:
                print(documentos[i])


def imprimir_documento(cola):
    if cola.is_empty():
        print("No hay documentos en la cola para imprimir.")
        return

    documento = cola.peek()

    print(f"Imprimiendo el documento: {documento.nombre} ({documento.num_paginas} páginas)")

    while documento.num_paginas > 0:
        time.sleep(1)
        documento.num_paginas -= 1
        print(f"Imprimiendo página... {documento.num_paginas} páginas restantes.")

    print(f"El documento {documento.nombre} ha sido impreso.\n")
    cola.dequeue()


cola_impresion = Cola()

cola_impresion.enqueue(Documento("Documento 1", 10))
cola_impresion.enqueue(Documento("Documento 2", 5))
cola_impresion.enqueue(Documento("Documento 3", 12))

cola_impresion.mostrar()

imprimir_documento(cola_impresion)
cola_impresion.mostrar()

imprimir_documento(cola_impresion)
cola_impresion.mostrar()

imprimir_documento(cola_impresion)
cola_impresion.mostrar()

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def _agregarValor(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._agregarValor(nodo.izquierda, valor)
        else:
            nodo.derecha = self._agregarValor(nodo.derecha, valor)
        return nodo

    def agregarValor(self, valor):
        self.raiz = self._agregarValor(self.raiz, valor)

    def _buscarValor(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscarValor(nodo.izquierda, valor)
        else:
            return self._buscarValor(nodo.derecha, valor)
        
    def buscarValor(self, valor):
        return self._buscarValor(self.raiz, valor)
    

arbol = ArbolBinario()
n = int(input("Ingrese el número de nodos: "))

for i in range(n):
    x = int(input("Ingrese un valor para agregar: "))
    arbol.agregarValor(x)

valor = int(input("Ingrese el valor a buscar: "))

if arbol.buscarValor(valor):
    print(f"El valor {valor} está en el árbol.")
else:
    print(f"El valor {valor} no está en el árbol.")
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

    def obtenerValorMinimo(self):
        nodo = self.raiz
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo.valor

    def obtenerValorMaximo(self):
        nodo = self.raiz
        while nodo.derecha is not None:
            nodo = nodo.derecha
        return nodo.valor

arbol = ArbolBinario()
n = int(input("Ingrese el número de nodos: "))

for i in range(n):
    x = int(input("Ingrese un valor para agregar: "))
    arbol.agregarValor(x)

print("Valor mínimo:", arbol.obtenerValorMinimo())
print("Valor máximo:", arbol.obtenerValorMaximo())
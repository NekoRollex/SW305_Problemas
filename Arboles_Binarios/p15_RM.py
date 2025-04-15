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

    def _inOrden(self, nodo):
        if nodo is not None:
            self._inOrden(nodo.izquierda)
            print(nodo.valor, end=' -> ')
            self._inOrden(nodo.derecha)

    def inOrden(self):
        self._inOrden(self.raiz)
        print(end="\n")

    def _mostrarNodosEnProfundidadK(self, nodo, profundidad, k):
        if nodo is not None:
            if profundidad == k:
                print(nodo.valor, end=', ')
            elif profundidad < k:
                self._mostrarNodosEnProfundidadK(nodo.izquierda, profundidad + 1, k)
                self._mostrarNodosEnProfundidadK(nodo.derecha, profundidad + 1, k)

    def mostrarNodosEnProfundidadK(self, k):
        print("Nodos a profundidad", k, end = ": ")
        return self._mostrarNodosEnProfundidadK(self.raiz, 1, k)


arbol = ArbolBinario()
n = int(input("Ingrese el número de nodos: "))

for i in range(n):
    x = int(input("Ingrese un valor para agregar: "))
    arbol.agregarValor(x)

k = int(input("Ingresar profundidad: "))
arbol.mostrarNodosEnProfundidadK(k)
print(end="\n")
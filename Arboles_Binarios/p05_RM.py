class NodoArbolBinario:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class ArbolBinario:
    def __init__(self):
        self.root = None
        self.size = 0

    def _add(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.left is None:
                nodo.left = NodoArbolBinario(valor)
            else:
                self._add(nodo.left, valor)
        else:
            if nodo.right is None:
                nodo.right = NodoArbolBinario(valor)
            else:
                self._add(nodo.right, valor)

    def add(self, valor):
        self.size += 1
        if self.root is None:
            self.root = NodoArbolBinario(valor)
        else:
            self._add(self.root, valor)

    def _print(self, nodo):
        if nodo is not None:
            self._print(nodo.left)
            self._print(nodo.right)
            print(nodo.valor, end=' -> ')

    def print(self):
        self._print(self.root)
        print(end = "\n")

arbol = ArbolBinario()

arbol.add(5)
arbol.add(3)
arbol.add(7)
arbol.add(2)
arbol.add(4)
arbol.add(6)
arbol.add(8)

print("Recorrido PostOrden")
arbol.print()


class NodoArbolBinario:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class ArbolBinario:
    def __init__(self):
        self.root = None
        self.size = 0
        self.max_depth = 0

    def _add(self, nodo, valor, depth):
        if valor < nodo.valor:
            if nodo.left is None:
                nodo.left = NodoArbolBinario(valor)
                self.max_depth = max(self.max_depth, depth + 1)
            else:
                self._add(nodo.left, valor, depth+1)
        else:
            if nodo.right is None:
                nodo.right = NodoArbolBinario(valor)
                self.max_depth = max(self.max_depth, depth + 1)
            else:
                self._add(nodo.right, valor, depth+1)

    def add(self, valor):
        self.size += 1
        if self.root is None:
            self.root = NodoArbolBinario(valor)
        else:
            self._add(self.root, valor, 1)

    def _print(self, nodo):
        if nodo is not None:
            self._print(nodo.left)
            print(nodo.valor, end=' -> ')
            self._print(nodo.right)

    def print(self):
        self._print(self.root)
        print(end = "\n")

    def _find_max_depth(self, nodo, depth):
        if nodo is None:
            return depth - 1
        else:
            return max(self._find_max_depth(nodo.left, depth + 1), 
                       self._find_max_depth(nodo.right, depth + 1))

    def find_max_depth(self):
        if self.root is None:
            return 0
        return self._find_max_depth(self.root, 1)

arbol = ArbolBinario()

arbol.add(5)
arbol.add(3)
arbol.add(7)
arbol.add(2)
arbol.add(4)
arbol.add(6)
arbol.add(8)
arbol.add(1)

print("Máxima profundidad:", arbol.max_depth)
print("Máxima profundidad:", arbol.find_max_depth())
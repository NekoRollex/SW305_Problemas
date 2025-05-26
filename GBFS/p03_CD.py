# 43. Búsqueda en árbol con valor objetivo, Explorar un árbol donde los nodos tienen un valor asociado,
#     y la heurística es la diferencia absoluta con el objetivo.

from queue import PriorityQueue

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

def imprimir_arbol(nodo, nivel=0):
    if nodo is not None:
        imprimir_arbol(nodo.derecha, nivel + 1)
        print(' ' * 4 * nivel + '->', nodo.valor)
        imprimir_arbol(nodo.izquierda, nivel + 1)

# Función de heurística: la diferencia absoluta con el valor objetivo
def heuristica(nodo, objetivo):
    return abs(nodo.valor - objetivo)

def GreedyBestFirstSearch(arbol, objetivo):
    if arbol.raiz is None:
        return None

    frontera = PriorityQueue()
    # Agregamos el nodo raíz a la frontera con su heurística
    frontera.put((heuristica(arbol.raiz, objetivo), arbol.raiz))

    while not frontera.empty():
        # Extraemos el nodo con la heurística más baja
        _, nodo_actual = frontera.get()

        if nodo_actual.valor == objetivo:
            return nodo_actual
        
        # Agregar los hijos del nodo actual a la frontera
        if nodo_actual.izquierda:
            frontera.put((heuristica(nodo_actual.izquierda, objetivo), nodo_actual.izquierda))
        if nodo_actual.derecha:
            frontera.put((heuristica(nodo_actual.derecha, objetivo), nodo_actual.derecha))

    return None

if __name__ == "__main__":
    arbol = ArbolBinario()
    valores = [10, 5, 15, 3, 7, 12, 18, 2, 4, 11]

    for valor in valores:
        arbol.agregarValor(valor)

    print("\nEstructura del árbol:")
    imprimir_arbol(arbol.raiz)

    objetivo = 3

    nodo_objetivo = GreedyBestFirstSearch(arbol, objetivo)

    if nodo_objetivo:
        print(f"Objetivo encontrado en el nodo con valor: {nodo_objetivo.valor}")
    else:
        print("Objetivo no encontrado.")


#           10
#         /    \
#        5      15
#       / \     / \
#      3   7  12   18
#     / \     /  
#    2   4   11
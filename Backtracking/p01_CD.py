# 1. Suma de caminos en un árbol binario, dado un árbol binario, encuentra todas las rutas desde la raíz
#    hasta las hojas cuya suma de nodos sea igual a un valor objetivo.
#   - Ejercicio clásico de backtracking con poda por suma.

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

    def encontrarCaminos(self, objetivo):
            caminos = []
            self.backtracking(self.raiz, 0, objetivo, [], caminos)
            return caminos
    
    def backtracking(self, nodo, suma_actual, objetivo, camino_actual, caminos):
        if nodo is None:
            return
        
        suma_actual += nodo.valor
        camino_actual.append(nodo.valor)

        if nodo.izquierda is None and nodo.derecha is None:
            if suma_actual == objetivo:
                caminos.append(list(camino_actual))

        self.backtracking(nodo.izquierda, suma_actual, objetivo, camino_actual, caminos)
        self.backtracking(nodo.derecha, suma_actual, objetivo, camino_actual, caminos)


        camino_actual.pop()


arbol = ArbolBinario()
valores = [10, 5, 15, 3, 7, 12, 18, 2, 4, 11]
for valor in valores:
    arbol.agregarValor(valor)

# Suma = 22
objetivo = int(input("Ingresa el valor objetivo: "))

caminos = arbol.encontrarCaminos(objetivo)

if caminos:
    print(f"Los caminos que suman {objetivo} son:")
    for camino in caminos:
        print(" -> ".join(map(str, camino)))
else:
    print(f"No se encontraron caminos que sumen {objetivo}")
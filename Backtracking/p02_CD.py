# 2. Contar caminos con suma específica, cuenta cuántos caminos desde la raíz hasta cualquier nodo suman un valor dado.
#   - Variante del anterior, requiere recorrer todos los caminos.

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
    def contarCaminos(self, objetivo):
            self.contador = 0
            self.caminos = []
            self.backtracking(self.raiz, 0, objetivo, [])
            return self.contador, self.caminos
    
    def backtracking(self, nodo, suma_actual, objetivo, camino_actual):
        if nodo is None:
            return

        suma_actual += nodo.valor
        camino_actual.append(nodo.valor)

        if suma_actual == objetivo:
            self.contador += 1
            self.caminos.append(list(camino_actual))

        self.backtracking(nodo.izquierda, suma_actual, objetivo, camino_actual)
        self.backtracking(nodo.derecha, suma_actual, objetivo, camino_actual)

        camino_actual.pop()


arbol = ArbolBinario()

valores = [10, 5, 15, 3, 7, 12, 18, 2, 4, 11]
for valor in valores:
    arbol.agregarValor(valor)

objetivo = int(input("Ingresa el valor objetivo: "))

cantidad, caminos = arbol.contarCaminos(objetivo)
print(f"Cantidad de caminos desde la raíz hasta algún nodo con suma {objetivo}: {cantidad}")

if cantidad > 0:
    print("Caminos encontrados:")
    for camino in caminos:
        print(" -> ".join(str(nodo) for nodo in camino))
class Nodo_AVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class AVL_Tree:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        return nodo.altura if nodo else 0
    
    def actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

    def obtener_balance(self, nodo):
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha) if nodo else 0

    def _insertar(self, nodo, valor):
        if not nodo:
            return Nodo_AVL(valor)
        elif valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        else:
            nodo.derecha = self._insertar(nodo.derecha, valor)

        return self.balancear_nodo(nodo)
    
    def rotacion_izquierda(self, z):
        y = z.derecha
        x = y.izquierda
        y.izquierda = z
        z.derecha = x
        self.actualizar_altura(z)
        self.actualizar_altura(y)
        return y
    
    def rotacion_derecha(self, z):
        y = z.izquierda
        x = y.derecha
        y.derecha = z
        z.izquierda = x
        self.actualizar_altura(z)
        self.actualizar_altura(y)
        return y

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _obtener_minimo(self, nodo):
        if nodo is None or nodo.izquierda is None:
            return nodo.valor
        return self._obtener_minimo(nodo.izquierda)

    def _eliminar(self, nodo, valor):
        if not nodo:
            return nodo
        elif valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            nodo.valor = self._obtener_minimo(nodo.derecha)
            nodo.derecha = self._eliminar(nodo.derecha, nodo.valor)
        
        return self.balancear_nodo(nodo)
    
    def balancear_nodo(self, nodo):
        self.actualizar_altura(nodo)
        balance = self.obtener_balance(nodo)

        if balance == 2:
            if self.obtener_balance(nodo.izquierda) >= 0:
                return self.rotacion_derecha(nodo)
            else:
                nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
                return self.rotacion_derecha(nodo)
        if balance == -2:
            if self.obtener_balance(nodo.derecha) <= 0:
                return self.rotacion_izquierda(nodo)
            else:
                nodo.derecha = self.rotacion_derecha(nodo.derecha)
                return self.rotacion_izquierda(nodo)

        return nodo

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _imprimir_inorden(self, nodo):
        if nodo:
            self._imprimir_inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            # print(nodo.valor, " : ", " -> ", self.obtener_balance(nodo))
            # if nodo.izquierda:
                # print("\tIzquierda de", nodo.valor, ":", nodo.izquierda.valor)
            # if nodo.derecha:
                # print("\tDerecha de", nodo.valor, ":", nodo.derecha.valor)
            self._imprimir_inorden(nodo.derecha)
    
    def imprimir_inorden(self):
        print("Recorrido inorden del árbol AVL:")
        self._imprimir_inorden(self.raiz)
        print()
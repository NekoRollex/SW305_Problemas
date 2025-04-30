class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.altura = 1  # La altura se inicializa como 1 cuando se crea el nodo
        self.izquierda = None
        self.derecha = None


class AVLTree:
    def __init__(self):
        self.raiz = None

    # Obtener la altura de un nodo
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    # Obtener el balance de un nodo
    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    # Rotación a la izquierda
    def rotacion_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        # Realizar la rotación
        y.izquierda = z
        z.derecha = T2

        # Actualizar las alturas
        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    # Rotación a la derecha
    def rotacion_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        # Realizar la rotación
        y.derecha = z
        z.izquierda = T3

        # Actualizar las alturas
        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    # Insertar un valor en el árbol AVL
    def insertar(self, raiz, valor):
        if not raiz:
            return NodoAVL(valor)
        
        # Inserción en el subárbol izquierdo o derecho
        if valor < raiz.valor:
            raiz.izquierda = self.insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = self.insertar(raiz.derecha, valor)

        # Actualizar la altura del nodo ancestro
        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierda), self.obtener_altura(raiz.derecha))

        # Obtener el balance del nodo
        balance = self.obtener_balance(raiz)

        # Caso de rotación a la izquierda
        if balance > 1 and valor < raiz.izquierda.valor:
            return self.rotacion_derecha(raiz)

        # Caso de rotación a la derecha
        if balance < -1 and valor > raiz.derecha.valor:
            return self.rotacion_izquierda(raiz)

        # Caso de rotación izquierda-derecha
        if balance > 1 and valor > raiz.izquierda.valor:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)

        # Caso de rotación derecha-izquierda
        if balance < -1 and valor < raiz.derecha.valor:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz

    # Método para insertar un valor en el árbol
    def insertar_valor(self, valor):
        self.raiz = self.insertar(self.raiz, valor)

    # Recorrido inorden (izquierda-raíz-derecha)
    def recorrido_inorden(self, raiz):
        if raiz:
            self.recorrido_inorden(raiz.izquierda)
            print(raiz.valor, end=" ")
            self.recorrido_inorden(raiz.derecha)

arbol = AVLTree()

numeros = [10, 20, 30, 40, 50, 25]

for num in numeros:
    arbol.insertar_valor(num)
    print(f"Árbol después de insertar {num}:")
    arbol.recorrido_inorden(arbol.raiz)

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

    # Eliminar un nodo en el árbol AVL
    def eliminar(self, raiz, valor):
        # Paso 1: Realizar la eliminación convencional en el BST
        if not raiz:
            return raiz

        if valor < raiz.valor:
            raiz.izquierda = self.eliminar(raiz.izquierda, valor)
        elif valor > raiz.valor:
            raiz.derecha = self.eliminar(raiz.derecha, valor)
        else:
            # Si el nodo es el que debe eliminarse
            if not raiz.izquierda:
                return raiz.derecha
            elif not raiz.derecha:
                return raiz.izquierda

            # Nodo con dos hijos, obtener el sucesor (el más pequeño en el subárbol derecho)
            temp = self.min_value_node(raiz.derecha)
            raiz.valor = temp.valor
            raiz.derecha = self.eliminar(raiz.derecha, temp.valor)

        # Paso 2: Actualizar la altura del nodo
        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierda), self.obtener_altura(raiz.derecha))

        # Paso 3: Obtener el balance del nodo para ver si hay un desbalance
        balance = self.obtener_balance(raiz)

        # Casos de rotación (derecha-izquierda o izquierda-derecha)
        if balance > 1 and self.obtener_balance(raiz.izquierda) >= 0:
            return self.rotacion_derecha(raiz)

        if balance < -1 and self.obtener_balance(raiz.derecha) <= 0:
            return self.rotacion_izquierda(raiz)

        if balance > 1 and self.obtener_balance(raiz.izquierda) < 0:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)

        if balance < -1 and self.obtener_balance(raiz.derecha) > 0:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz

    # Buscar el nodo con el valor más pequeño en un subárbol
    def min_value_node(self, raiz):
        current = raiz
        while current.izquierda:
            current = current.izquierda
        return current

    # Método para eliminar un valor en el árbol
    def eliminar_valor(self, valor):
        self.raiz = self.eliminar(self.raiz, valor)


arbol = AVLTree()

numeros = [10, 20, 30, 40, 50, 25]

for num in numeros:
    arbol.insertar_valor(num)
    print(f"Árbol después de insertar {num}:")
    arbol.recorrido_inorden(arbol.raiz)
    print()

arbol.eliminar_valor(30)
print("Árbol después de eliminar 30:")
arbol.recorrido_inorden(arbol.raiz)
print()

class Nodo:
    def __init__(self, val):
        self.valor = val
        self.izquierdo = None
        self.derecho = None
        self.padre = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, val):
        n = Nodo(val)
        if self.raiz != None:
            paux = self.raiz
            while paux != None:
                ppadre = paux
                if val < paux.valor:
                    paux = paux.izquierdo
                else:
                    paux = paux.derecho
            n.padre = ppadre
            if val < ppadre.valor:
                ppadre.izquierdo = n
            else:
                ppadre.derecho = n
        else:
            self.raiz = n

def Backtracking(nodo, suma, ruta, rutasencontradas, sumadeseada):
        if nodo:
            suma += nodo.valor
            ruta.append(nodo.valor)
    
            if not nodo.izquierdo and not nodo.derecho:
                if suma == sumadeseada:
                    rutasencontradas[0] += 1 
    
            Backtracking(nodo.izquierdo, suma, ruta, rutasencontradas, sumadeseada)
            Backtracking(nodo.derecho, suma, ruta, rutasencontradas, sumadeseada)
    
            ruta.pop()

def EncontrarRutas(arbol):
    suma = 0
    sumadeseada = int(input("Ingrese la suma que desea buscar: "))
    ruta = []
    rutasencontradas = [0]

    Backtracking(arbol.raiz, suma, ruta, rutasencontradas, sumadeseada)
    return rutasencontradas

arbol = ArbolBinario()

print("Ingrese el arbol binario")
print("Si quiere salir ingrese 0")

valor = 1
while valor != 0:
    valor = int(input("Ingrese un elemento: "))
    if valor != 0:
        arbol.insertar(valor)

rutas = EncontrarRutas(arbol)
print("El numero de rutas encontradas son: ")
print(rutas[0])

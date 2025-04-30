class FenwickTree:
    def __init__(self, longitud):
        self.tamaño = longitud
        self.arr = [0]*(longitud+1)

    def update(self, i, valor):
        while i <= self.tamaño:
            self.arr[i] += valor
            i += i & -i
    def query(self, i):
        suma = 0
        while i > 0:
            suma += self.arr[i]
            i -= i & -i 
        return suma
    def range_query(self, izquierda, derecha):
        return self.query(derecha) - self.query(izquierda - 1)
    
def build(arreglo):
    arbol = FenwickTree(len(arreglo))
    for i in range(arbol.tamaño):
        arbol.update(i+1, arreglo[i])

    return arbol        

arreglo = [1, 3, 5, 7, 9, 11]

arbol = build(arreglo)
print("Suma entre los elementos 1 y 3")
print(arbol.range_query(1, 3))
arbol.update(1, 10)
print("Suma entre los elementos 1 y 3, con el valor de 10 en el 1er elemento")
print(arbol.range_query(1, 3))
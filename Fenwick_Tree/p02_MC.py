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

arreglo = [1, 7, 3, 0, 7, 8, 3, 2, 6, 2]

arbol = build(arreglo)

print("Suma de los 5 primeros elementos: ")
print(arbol.query(5))

print("la suma entre los elementos 3 y 7 es: ")
print(arbol.range_query(3, 7))
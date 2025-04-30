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
i = -1
j = -1

while i<=0:
    i = int(input("Ingrese l: "))
    while j<=i or j>arbol.tamaño:
        j = int(input("Ingrese r: "))

print("la suma entre los elementos l y r es: ")
print(arbol.range_query(i, j))
class FenwickTree:
    def __init__(self, longitud):
        self.tamaño = longitud
        self.arr = ["a"]*(longitud+1)

    def update(self, i, valor):
        while i <= self.tamaño:
            if self.arr[i] == "a":
                self.arr[i] = valor
            else:
                if self.arr[i]>valor:
                    self.arr[i] = valor
            i += i & -i
    def query(self, i):
        min = "a"
        while i > 0:
            if min == "a":
                min = self.arr[i]
            else:
                if min>self.arr[i]:
                    min = self.arr[i]
            i -= i & -i 
        return min

    def range_query(self, izquierda, derecha):
        if self.query(derecha) > self.query(izquierda - 1):
            return self.query(izquierda - 1)
        else:
            return self.query(derecha)
    
def build(arreglo):
    arbol = FenwickTree(len(arreglo))
    for i in range(arbol.tamaño):
        arbol.update(i+1, arreglo[i])

    return arbol        

arreglo = [2, 6, 1, 4, 5, 7, 3]

arbol = build(arreglo)
print("Minimo entre los elementos 2 y 5")
print(arbol.range_query(2, 5))
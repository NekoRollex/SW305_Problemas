class FenwickTree:
    def __init__(self, longitud):
        self.tamaño = longitud
        self.arr = ["a"]*(longitud+1)

    def update(self, i, valor):
        while i <= self.tamaño:
            if self.arr[i] == "a":
                self.arr[i] = valor
            else:
                if self.arr[i]<valor:
                    self.arr[i] = valor
            i += i & -i
    def query(self, i):
        max = "a"
        while i > 0:
            if max == "a":
                max = self.arr[i]
            else:
                if max<self.arr[i]:
                    max = self.arr[i]
            i -= i & -i 
        return max
    
def build(arreglo):
    arbol = FenwickTree(len(arreglo))
    for i in range(arbol.tamaño):
        arbol.update(i+1, arreglo[i])

    return arbol        

n = -1
while n <= 0:
    n = int(input("Ingrese el tamaño del arreglo: "))

arbol = FenwickTree(n)

for i in range(n):
    elemento = int(input("Ingrese un elemento: "))
    arbol.update(i+1, elemento)

i = -1

while i<=0 or i>arbol.tamaño:
    i = int(input("Ingrese un indice cualquiera: "))

print("Minimo entre los primeros {i} elementos:")
print(arbol.query(i))
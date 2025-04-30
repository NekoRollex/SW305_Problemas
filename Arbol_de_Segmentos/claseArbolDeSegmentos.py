class ArbolDeSegmentos:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)  # Inicializa el árbol de segmentos con ceros 

    def operation(self, a, b):
        return a + b  # Define la operación de suma para el árbol de segmentos

    # Construye el árbol de segmentos a partir del arreglo dado
    # para llamar el método: start = 0, end = n-1, node = 1 (rangos cerrados y la raiz es 1)
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node, start, mid)
            self.build(arr, 2 * node + 1, mid + 1, end)
            self.tree[node] = self.operation(self.tree[2 * node], self.tree[2 * node + 1])

    # node, start, end son los mismos que en el método build
    # idx es el índice del elemento a actualizar y value es el nuevo valor
    def update(self, idx, value, node, start, end):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(idx, value, 2 * node, start, mid)
            else:
                self.update(idx, value, 2 * node + 1, mid + 1, end)
            self.tree[node] = self.operation(self.tree[2 * node], self.tree[2 * node + 1])

    # L y R son los límites del rango de consulta
    # node, start, end son los mismos que en el método build
    def query(self, L, R, node, start, end):
        if R < start or end < L:
            return 0  # Valor neutro para la operación de suma
        if L <= start and end <= R: # Rango completamente dentro del rango de consulta
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(L, R, 2 * node, start, mid)
        right_sum = self.query(L, R, 2 * node + 1, mid + 1, end)
        return self.operation(left_sum, right_sum)

sgt = ArbolDeSegmentos(10)
sgt.build([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 0, 9)
print(sgt.query(0, 4, 1, 0, 9))  # Suma de los primeros 5 elementos (1+2+3+4+5 = 15)
sgt.update(2, 10, 1, 0, 9)  # Cambia el valor del índice 2 a 10
print(sgt.query(0, 4, 1, 0, 9))  # Suma de los primeros 5 elementos (1+2+10+4+5 = 22)
print(sgt.query(0, 9, 1, 0, 9))  # Suma de todos los elementos (1+2+10+4+5+6+7+8+9+10 = 52)
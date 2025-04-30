class ArbolDeSegmentos:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)  

    def operation(self, a, b):
        return a + b 

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node, start, mid)
            self.build(arr, 2 * node + 1, mid + 1, end)
            self.tree[node] = self.operation(self.tree[2 * node], self.tree[2 * node + 1])

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

    def query(self, L, R, node, start, end):
        if R < start or end < L:
            return 0 
        if L <= start and end <= R: 
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(L, R, 2 * node, start, mid)
        right_sum = self.query(L, R, 2 * node + 1, mid + 1, end)
        return self.operation(left_sum, right_sum)

arreglo = [1, 3, 5, 7, 9, 11]
sgt = ArbolDeSegmentos(5)
sgt.build(arreglo, 1, 0, 5)

i = int(input("Ingrese el l (indexado desde 0): "))
j = int(input("Ingrese el r: "))

dif = sgt.query(i, j, 1, 0, 5)
print(f"La suma de los elementos en el rango de [{i}: {j}], es: {dif}")
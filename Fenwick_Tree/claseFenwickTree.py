class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # Inicializa el árbol de Fenwick con ceros

    def update(self, idx, value):
        """Actualiza el índice idx con el valor value."""
        while idx <= self.n:
            self.tree[idx] += value
            idx += idx & -idx

    def query(self, idx):
        """Devuelve la suma de los elementos desde el índice 1 hasta idx."""
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx
        return result
    
    def range_query(self, left, right):
        """Devuelve la suma de los elementos desde el índice left hasta right."""
        return self.query(right) - self.query(left - 1)
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fenwick = FenwickTree(len(arr))

for i in range(len(arr)):
    fenwick.update(i + 1, arr[i])  # Actualiza el árbol de Fenwick con los valores del arreglo

print(fenwick.range_query(1, 5))  # Suma de los primeros 5 elementos (1+2+3+4+5 = 15)
print(fenwick.range_query(1, 10))  # Suma de todos los elementos (1+2+3+4+5+6+7+8+9+10 = 55)
fenwick.update(3, 10)  # Suma 10 al índice 3 (4 en el arreglo original)
print(fenwick.range_query(1, 5))  # Suma de los primeros 5 elementos (1+2+13+4+5 = 25)
print(fenwick.range_query(1, 10))  # Suma de todos los elementos (1+2+13+4+5+6+7+8+9+10 = 65)
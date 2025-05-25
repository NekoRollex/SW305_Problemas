class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heap = self.heap
        heap.append(value)
        index = len(heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if heap[index][2] >= heap[parent][2]:
                break
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent

    def extract_min(self):
        heap = self.heap
        if heap:
            heap[0], heap[-1] = heap[-1], heap[0]
            heap.pop()
            self.heapify(0)

    def heapify(self, index):
        heap = self.heap
        smallest = index
        for child in [2 * index + 1, 2 * index + 2]:
            if child < len(heap) and heap[child][2] < heap[smallest][2]:
                smallest = child
        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            self.heapify(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None
    
min_heap = MinHeap()

# A B C D E -> 0 1 2 3 4
n = 5
aristas = []
aristas.append((0, 1, 2))
aristas.append((0, 2, 3))
aristas.append((1, 2, 1))
aristas.append((1, 3, 4))
aristas.append((2, 3, 5))
aristas.append((2, 4, 6))
aristas.append((3, 4, 7))

vecinos = [[] for _ in range(n)]

for a, b, w in aristas:
    vecinos[a].append((b, w))
    vecinos[b].append((a, w))

visitado = [False for _ in range(n)]

# iniciamos desde A
visitado[0] = True
for v, w in vecinos[0]:
    min_heap.insert((0, v, w))

def f(x):
    if x == 0:
        return 'A'
    elif x == 1:
        return 'B'
    elif x == 2:
        return 'C'
    elif x == 3:
        return 'D'
    elif x == 4:
        return 'E'

print("Empezamos desde A")
mst = 0
while min_heap.heap:
    # u ya fue visitado
    u, v, w = min_heap.get_min()
    min_heap.extract_min()

    if not visitado[v]:
        mst += w
        visitado[v] = True
        print("Nuevo vértice agregado:", f(v))
        print(f"Arista usada: " + f(u) + "-" + f(v) + f":{w}")
        for x, we in vecinos[v]:
            min_heap.insert((v, x, we))

print("Valor del mst:", mst)

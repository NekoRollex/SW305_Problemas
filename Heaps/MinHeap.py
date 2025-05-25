class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heap = self.heap
        heap.append(value)
        index = len(heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if heap[index] >= heap[parent]:
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
            if child < len(heap) and heap[child] < heap[smallest]:
                smallest = child
        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            self.heapify(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None
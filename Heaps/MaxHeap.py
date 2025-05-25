class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heap = self.heap
        heap.append(value)
        index = len(heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if heap[index] <= heap[parent]:
                break
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent

    def extract_max(self):
        heap = self.heap
        if heap:
            heap[0], heap[-1] = heap[-1], heap[0]
            heap.pop()
            self.heapify(0)

    def heapify(self, index):
        heap = self.heap
        largest = index
        for child in [2 * index + 1, 2 * index + 2]:
            if child < len(heap) and heap[child] > heap[largest]:
                largest = child
        if largest != index:
            heap[index], heap[largest] = heap[largest], heap[index]
            self.heapify(largest)

    def get_max(self):
        return self.heap[0] if self.heap else None
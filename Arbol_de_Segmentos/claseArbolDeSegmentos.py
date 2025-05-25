class Segment_Tree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1, arr)

    def merge(self, left, right):
        return left + right

    def build(self, node, start, end, arr):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node + 1, start, mid, arr)
            self.build(2 * node + 2, mid + 1, end, arr)
            self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left= self._query(2 * node + 1, start, mid, l, r)
        right = self._query(2 * node + 2, mid + 1, end, l, r)
        return self.merge(left, right)

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)
    
    def _update(self, node, start, end, idx, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self._update(2 * node + 1, start, mid, idx, value)
            else:
                self._update(2 * node + 2, mid + 1, end, idx, value)
            self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, idx, value):
        self._update(0, 0, self.n - 1, idx, value)
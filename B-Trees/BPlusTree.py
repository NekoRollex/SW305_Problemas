class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.next_leaf = None  # Enlace a la siguiente hoja

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(True)
        self.t = t  # Grado mínimo

    def search(self, key, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if node.leaf:
            return True if key in node.keys else False

        return self.search(key, node.children[i])

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BPlusTreeNode()
            self.root = new_root
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(key)
            while i >= 0 and key < node.keys[i]:
                node.keys[i], node.keys[i + 1] = node.keys[i + 1], node.keys[i]
                i -= 1
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, i):
        t = self.t
        child = parent.children[i]
        new_child = BPlusTreeNode(child.leaf)

        parent.children.insert(i + 1, new_child)

        if child.leaf:
            # En B+ las hojas conservan todas sus claves
            new_child.keys = child.keys[t:]      # segunda mitad
            child.keys = child.keys[:t]          # primera mitad

            # Encadenar hojas
            new_child.next_leaf = child.next_leaf
            child.next_leaf = new_child

            # Promueve la primera clave del nuevo hijo
            parent.keys.insert(i, new_child.keys[0])
        else:
            # Para nodos internos, se promueve la clave del medio
            mid_key = child.keys[t - 1]
            parent.keys.insert(i, mid_key)

            new_child.keys = child.keys[t:]          # derecha sin la del medio
            child.keys = child.keys[:t - 1]          # izquierda sin la del medio

            new_child.children = child.children[t:]
            child.children = child.children[:t]

    def print_leaves(self):
        node = self.root
        while not node.leaf:
            node = node.children[0]
        
        while node:
            print(node.keys)
            node = node.next_leaf

# Ejemplo de uso
bptree = BPlusTree(t=3)
lista = [10, 20, 5, 6, 12, 30, 7, 17]

for key in lista:
    bptree.insert(key)
    bptree.print_leaves()
    print()

print("B+-tree creado correctamente. Recorrido de hojas:")
bptree.print_leaves()

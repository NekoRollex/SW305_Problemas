class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Grado mínimo del B-tree

    def search(self, key, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return True

        if node.leaf:
            return False

        return self.search(key, node.children[i])

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:  # Si el nodo está lleno
            new_root = BTreeNode()
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
        new_child = BTreeNode(child.leaf)
        parent.children.insert(i + 1, new_child)
        parent.keys.insert(i, child.keys[t - 1])

        new_child.keys = child.keys[t:(2 * t - 1)]
        child.keys = child.keys[:t - 1]

        if not child.leaf:
            new_child.children = child.children[t:(2 * t)]
            child.children = child.children[:t]

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root

        print("Nivel", level, ": ", node.keys)

        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)

# Ejemplo de uso
btree = BTree(t=3)  # Grado mínimo 3

# lista = [10, 20, 5, 6, 12, 30, 7, 17]
lista = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for key in lista:
    btree.insert(key)
    btree.print_tree()
    print()

print("B-tree creado correctamente.")

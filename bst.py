from node_bst import Node

class BinarySearchTree:

    def __init__(self):
        self.root = None

    # Menambah Lagu
    def insert(self, lagu):
        if self.root is None:
            self.root = Node(lagu)
        else:
            self._insert(self.root, lagu)

    def _insert(self, current, lagu):
        if lagu.judul.lower() < current.lagu.judul.lower():
            if current.left is None:
                current.left = Node(lagu)
            else:
                self._insert(current.left, lagu)

        else:
            if current.right is None:
                current.right = Node(lagu)
            else:
                self._insert(current.right, lagu)

    # Mencari Lagu
    def search(self, judul):
        return self._search(self.root, judul.lower())

    def _search(self, node, judul):

        if node is None:
            return None

        if node.lagu.judul.lower() == judul:
            return node.lagu

        if judul < node.lagu.judul.lower():
            return self._search(node.left, judul)

        return self._search(node.right, judul)

    # Menampilkan Semua Lagu (Urut A-Z)
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            node.lagu.tampil()
            self._inorder(node.right)

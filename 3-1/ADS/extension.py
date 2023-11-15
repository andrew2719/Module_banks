class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.parent = None

class SplayTree:
    def __init__(self):
        self.root = None

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def splay(self, x):
        while x.parent:
            if not x.parent.parent:
                if x == x.parent.left:
                    self.right_rotate(x.parent)
                else:
                    self.left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self.right_rotate(x.parent.parent)
                self.right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self.left_rotate(x.parent.parent)
                self.left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self.left_rotate(x.parent)
                self.right_rotate(x.parent)
            else:
                self.right_rotate(x.parent)
                self.left_rotate(x.parent)

    def insert(self, key):
        node = Node(key)
        y = None
        x = self.root
        while x:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if not y:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        self.splay(node)
        return node

    def find(self, key):
        z = self.root
        while z:
            if z.key < key:
                z = z.right
            elif key < z.key:
                z = z.left
            else:
                self.splay(z)
                return z
        return None

    def remove(self, node):
        self.splay(node)
        if not node.left:
            self.replace(node, node.right)
        elif not node.right:
            self.replace(node, node.left)
        else:
            y = node.left
            while y.right:
                y = y.right
            if y.parent != node:
                self.replace(y, y.left)
                y.left = node.left
                y.left.parent = y
            self.replace(node, y)
            y.right = node.right
            y.right.parent = y

    def replace(self, old, new):
        if not old.parent:
            self.root = new
        elif old == old.parent.left:
            old.parent.left = new
        else:
            old.parent.right = new
        if new:
            new.parent = old.parent

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_size = 0
        self.tree = SplayTree()

    def access(self, key):
        node = self.tree.find(key)
        if not node:
            if self.current_size < self.capacity:
                self.current_size += 1
            else:
                # Evict the least recently accessed item
                self.evict()
            self.tree.insert(key)
        # if it's already in the tree, splay will move it to the root

    def evict(self):
        if not self.tree.root:
            return

        # the leftmost leaf is one of the least accessed items
        node = self.tree.root
        while node.left:
            node = node.left
        self.tree.remove(node)

    def display(self):
        self._print_tree(self.tree.root)

    def _print_tree(self, node, indent="", position="root"):
        if node:
            print(indent, node.key, position)
            if node.left or node.right:
                indent += "  "
                self._print_tree(node.left, indent, "L")
                self._print_tree(node.right, indent, "R")

cache = Cache(3)
cache.access(1)
cache.access(2)
cache.access(3)
cache.access(4)  # this will evict 1
cache.display()  # should show 4 at the root and one of 2 or 3 as the deepest leaf (least recently accessed)

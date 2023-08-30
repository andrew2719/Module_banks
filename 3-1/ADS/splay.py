class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class SplayTree:
    def __init__(self):
        self.root = None
        self.rotation_count = {'Zig': 0, 'Zag': 0, 'Zig-Zig': 0, 'Zag-Zag': 0, 'Zig-Zag': 0, 'Zag-Zig': 0}

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
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
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def splay(self, x):
        while x.parent:
            if x.parent.parent is None:
                if x == x.parent.left:
                    self.right_rotate(x.parent)
                    self.rotation_count['Zig'] += 1
                else:
                    self.left_rotate(x.parent)
                    self.rotation_count['Zag'] += 1
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self.right_rotate(x.parent.parent)
                self.right_rotate(x.parent)
                self.rotation_count['Zig-Zig'] += 1
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self.left_rotate(x.parent.parent)
                self.left_rotate(x.parent)
                self.rotation_count['Zag-Zag'] += 1
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self.left_rotate(x.parent)
                self.right_rotate(x.parent)
                self.rotation_count['Zig-Zag'] += 1
            else:
                self.right_rotate(x.parent)
                self.left_rotate(x.parent)
                self.rotation_count['Zag-Zig'] += 1

    def insert(self, key):
        node = Node(key)
        if self.root is None:
            self.root = node
        else:
            x = self.root
            while x:
                y = x
                if node.key < x.key:
                    x = x.left
                else:
                    x = x.right
            node.parent = y
            if node.key < y.key:
                y.left = node
            else:
                y.right = node
            self.splay(node)

    def print_rotation_count(self):
        for rotation_type, count in self.rotation_count.items():
            print(f"{rotation_type} rotations: {count}")

# Example usage
tree = SplayTree()
tree.insert(5)
tree.insert(9)
tree.insert(13)
tree.insert(2)
tree.insert(7)
tree.print_rotation_count()

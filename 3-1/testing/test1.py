class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def right_rotate(x):
    y = x.left
    x.left = y.right
    y.right = x
    return y

def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

def splay(root, key):
    if root is None or root.key == key:
        return root
    
    if root.key > key:
        if root.left is None:
            return root
        root.left = splay(root.left, key)
        return right_rotate(root)
    
    if root.key < key:
        if root.right is None:
            return root
        root.right = splay(root.right, key)
        return left_rotate(root)

def insert(root, key):
    if root is None:
        return Node(key)
    root = splay(root, key)
    if root.key == key:
        return root
    
    new_node = Node(key)
    if root.key > key:
        new_node.right = root
        new_node.left = root.left
        root.left = None
    else:
        new_node.left = root
        new_node.right = root.right
        root.right = None
    return new_node

def search(root, key):
    return splay(root, key)

def calculate_potential(root, depth=0):
    if root is None:
        return 0
    return depth + calculate_potential(root.left, depth + 1) + calculate_potential(root.right, depth + 1)

def inorder(root):
    result = []
    if root:
        result.extend(inorder(root.left))
        result.append(root.key)
        result.extend(inorder(root.right))
    return result

# Test the Splay Tree
root = None

root = insert(root, 20)
print("Inorder after inserting 20:", inorder(root))
print("Potential function value:", calculate_potential(root))

root = insert(root, 15)
print("Inorder after inserting 15:", inorder(root))
print("Potential function value:", calculate_potential(root))

root = insert(root, 25)
print("Inorder after inserting 25:", inorder(root))
print("Potential function value:", calculate_potential(root))

root = insert(root, 5)
print("Inorder after inserting 5:", inorder(root))
print("Potential function value:", calculate_potential(root))

root = search(root, 15)
print("Inorder after searching 15:", inorder(root))
print("Potential function value:", calculate_potential(root))

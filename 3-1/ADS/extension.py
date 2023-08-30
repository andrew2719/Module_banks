class Block:
    def __init__(self, start, size):
        self.start = start
        self.size = size
        self.left = None
        self.right = None
        self.parent = None

class MemoryManager:
    def __init__(self, total_size):
        self.root = Block(0, total_size)
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

    def allocate(self, size):
        x = self.root
        best_fit = None
        while x:
            if x.size >= size:
                best_fit = x
                x = x.left
            else:
                x = x.right
        if best_fit:
            self.splay(best_fit)
            remaining_size = best_fit.size - size
            if remaining_size > 0:
                new_block = Block(best_fit.start + size, remaining_size)
                new_block.left = best_fit.left
                if new_block.left:
                    new_block.left.parent = new_block
                best_fit.left = new_block
                new_block.parent = best_fit
                best_fit.size = size
            return best_fit.start
        else:
            return None

    def deallocate(self, start, size):
        new_block = Block(start, size)
        x = self.root
        while x:
            if new_block.start < x.start:
                x = x.left
            else:
                x = x.right
        self.splay(x)
        # Insert and possibly merge adjacent blocks here

        

    def print_rotation_count(self):
        for rotation_type, count in self.rotation_count.items():
            print(f"{rotation_type} rotations: {count}")

# Example usage
mem_manager = MemoryManager(1000)
print("Allocated at:", mem_manager.allocate(200))
print("Allocated at:", mem_manager.allocate(300))
print("Allocated at:", mem_manager.allocate(100))
mem_manager.print_rotation_count()

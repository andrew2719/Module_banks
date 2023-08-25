import random

class GlassBoxesProblem:
    def __init__(self):
        self.start_state = 1
        self.goal_state = 6
        self.box_keys = [i for i in range(1, 7)]
        self.box_to_key = {}
        self.shuffle_keys()

    def shuffle_keys(self):
        random.shuffle(self.box_keys)
        for i in range(6):
            self.box_to_key[i + 1] = self.box_keys[i]

    def bfs(self):
        visited_boxes = set()
        keys_possessed = {self.start_state}  # You start with the key to the first box
        queue = [self.start_state]

        while queue:
            current_box = queue.pop(0)
            print(f"Agent is at box {current_box}")

            if current_box == self.goal_state:
                print(f"Agent found the banana in box {current_box}!")
                return f"Banana found in box {current_box}!"

            if current_box not in visited_boxes:
                visited_boxes.add(current_box)
                key_found = self.box_to_key[current_box]
                keys_possessed.add(key_found)
                print(f"Agent unlocked box {current_box} and found the key for box {key_found}")

                for i in range(1, 7):
                    if i in keys_possessed and i not in visited_boxes:
                        queue.append(i)

        print("Agent couldn't find the banana.")
        return "Banana not found"

    def print_box_keys(self):
        for i in range(1, 7):
            print(f"Box {i} contains key to box {self.box_to_key[i]}")

# Test
problem = GlassBoxesProblem()
problem.print_box_keys()
problem.bfs()

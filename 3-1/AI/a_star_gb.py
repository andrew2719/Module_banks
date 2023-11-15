# from queue import PriorityQueue

# def heuristic(state):
#     return 6 - state['current_box']

# def a_star():
#     start_state = {'current_box': 1, 'path_cost': 0}
#     frontier = PriorityQueue()
#     frontier.put((0, start_state))
#     explored = set()

#     while not frontier.empty():
#         _, current_state = frontier.get()
#         print(f"Agent is in box {current_state['current_box']}")
#         current_box = current_state['current_box']

#         print(f"Agent is considering box {current_box}")

#         if current_box == 6:  # Goal test
#             print(f"Agent found the banana in box {current_box}!")
#             return current_state['path_cost']

#         explored.add(current_box)

#         for action in ['unlock_next_box']:
#             new_box = current_box + 1
#             if new_box not in explored:
#                 print(f"Agent unlocked box {current_box} and is moving to box {new_box}")
#                 new_state = {'current_box': new_box, 'path_cost': current_state['path_cost'] + 1}
#                 priority = new_state['path_cost'] + heuristic(new_state)
#                 frontier.put((priority, new_state))
#             else:
#                 print(f"Agent already visited box {new_box}, skipping.")

# print("Minimum steps to get the banana:", a_star())

from queue import PriorityQueue

def heuristic(box_number):
    """Estimate the distance from the current box to the goal (box 6)."""
    return 6 - box_number

def get_next_state(current_box):
    """Get the next state after unlocking the current box."""
    return {'current_box': current_box + 1, 'path_cost': current_box}

def a_star_search():
    """Perform A* search to find the shortest path to the banana."""
    
    # Initialize the starting state and priority queue
    start_state = {'current_box': 1, 'path_cost': 0}
    frontier = PriorityQueue()
    frontier.put((0, start_state))
    explored_boxes = set()

    while not frontier.empty():
        _, current_state = frontier.get()
        current_box = current_state['current_box']

        print(f"Agent is in box {current_box}")

        # Check if the current box is the goal
        if current_box == 6:
            print(f"Agent found the banana in box {current_box}!")
            return current_state['path_cost']

        explored_boxes.add(current_box)

        # Try to move to the next box
        new_box = current_box + 1
        if new_box not in explored_boxes:
            print(f"Agent unlocked box {current_box} and is moving to box {new_box}")
            new_state = get_next_state(current_box)
            priority = new_state['path_cost'] + heuristic(new_box)
            frontier.put((priority, new_state))
        else:
            print(f"Agent already visited box {new_box}, skipping.")

print("Minimum steps to get the banana:", a_star_search())

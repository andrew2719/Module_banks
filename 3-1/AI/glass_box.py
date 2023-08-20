from collections import deque

def unlock_next(state):
    # Find the first locked box and unlock it
    for i in range(len(state) - 1):  # -1 because we don't need to unlock the banana
        if state[i] == "unlocked" and state[i+1] == "locked":
            new_state = list(state)
            new_state[i+1] = "unlocked"
            return tuple(new_state)
    return state

def glass_boxes_problem():
    initial_state = ("unlocked", "locked", "locked", "locked", "locked", "locked", "banana")
    goal_state = ("unlocked", "unlocked", "unlocked", "unlocked", "unlocked", "unlocked", "banana")
    
    visited = set()
    queue = deque([(initial_state, [])])
    
    while queue:
        state, path = queue.popleft()
        
        if state == goal_state:
            return path + [goal_state]
        
        if state not in visited:
            visited.add(state)
            next_state = unlock_next(state)
            queue.append((next_state, path + [state]))

print(glass_boxes_problem())

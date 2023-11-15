from queue import PriorityQueue

def heuristic(state):
    return sum(1 for char in state if char != 'E')

def apply_transformation(sequence, transformation):
    if transformation == 'AC=E':
        return sequence.replace('AC', 'E', 1)
    elif transformation == 'AB=BC':
        return sequence.replace('AB', 'BC', 1)
    elif transformation == 'BB=E':
        return sequence.replace('BB', 'E', 1)
    elif transformation == 'Exx=xx':
        for char in 'ABCDE':
            sequence = sequence.replace(f'E{char}', f'{char}', 1)
            sequence = sequence.replace(f'{char}E', f'{char}', 1)
    return sequence

def a_star(initial_sequence):
    start_state = {'sequence': initial_sequence, 'path_cost': 0}
    frontier = PriorityQueue()
    frontier.put((0, start_state))
    explored = set()

    while not frontier.empty():
        _, current_state = frontier.get()
        current_sequence = current_state['sequence']

        if current_sequence == 'E':  # Goal test
            return current_state['path_cost']

        explored.add(current_sequence)

        for transformation in ['AC=E', 'AB=BC', 'BB=E', 'Exx=xx']:
            new_sequence = apply_transformation(current_sequence, transformation)
            if new_sequence not in explored:
                new_state = {'sequence': new_sequence, 'path_cost': current_state['path_cost'] + 1}
                priority = new_state['path_cost'] + heuristic(new_state)
                frontier.put((priority, new_state))

print("Minimum steps to transform to 'E':", a_star('ABABAECCEC'))

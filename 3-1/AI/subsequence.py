from collections import deque

def transform_sequence(seq):
    transformations = {
        "AC": "E",
        "AB": "BC",
        "BB": "E"
    }
    results = []
    for k, v in transformations.items():
        index = seq.find(k)
        if index != -1:
            results.append(seq[:index] + v + seq[index+len(k):])
    # For Exx = xx transformation
    for i in range(len(seq) - 1):
        if seq[i] == 'E' and seq[i+1] == seq[i+2]:
            results.append(seq[:i] + seq[i+1:i+3] + seq[i+3:])
    return results

def sequence_transformation_problem(initial_sequence="ABABAECCEC"):
    goal_sequence = "E"
    
    visited = set()
    queue = deque([(initial_sequence, [])])
    
    while queue:
        seq, path = queue.popleft()
        
        if seq == goal_sequence:
            return path + [goal_sequence]
        
        if seq not in visited:
            visited.add(seq)
            for next_seq in transform_sequence(seq):
                queue.append((next_seq, path + [seq]))

print(sequence_transformation_problem())

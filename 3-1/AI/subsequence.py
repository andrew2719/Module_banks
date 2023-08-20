def transform_sequence(seq):
    transformations = {
        "AC": "E",
        "AB": "BC",
        "BB": "E"
    }
    results = []

    for k, v in transformations.items():
        index = seq.find(k)
        while index != -1:
            transformed = seq[:index] + v + seq[index+len(k):]
            results.append(transformed)
            index = seq.find(k, index + 1)

    # For Ex = x transformation
    for i in range(len(seq) - 1):
        if seq[i] == 'E':
            transformed = seq[:i] + seq[i+1] + seq[i+2:]
            results.append(transformed)

    return results

def dfs(seq, path, visited):
    if seq == "E":
        return path + [seq]
    
    if seq in visited:
        return None

    visited.add(seq)
    for next_seq in transform_sequence(seq):
        result = dfs(next_seq, path + [seq], visited)
        if result:
            return result
    return None

initial_seq = input("Enter the sequence: ")
visited = set()
result = dfs(initial_seq, [], visited)

if result:
    print("Transformation Process:")
    for step in result:
        print(step)
else:
    print("False")

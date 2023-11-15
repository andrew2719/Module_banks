from scipy.optimize import linear_sum_assignment
import numpy as np

# Given distance matrix from the problem
distance_matrix = np.array([
    [140, 100, 175, 190, 200],
    [135, 120, 130, 160, 175],
    [140, 110, 155, 170, 185],
    [ 50,  50,  80,  80, 110],
    [ 55,  35,  70,  80, 105]
])

# Apply the Hungarian algorithm (linear_sum_assignment) to find the minimum cost
row_ind, col_ind = linear_sum_assignment(distance_matrix)

# Compute the minimum distance using the optimal assignment
min_distance = distance_matrix[row_ind, col_ind].sum()
assignments = list(zip(row_ind, col_ind))

# Print the results
print(f"The minimum distance is: {min_distance}")
print("The optimal assignment is:")
for row, col in assignments:
    print(f"Town {chr(ord('A') + row)} is assigned to depot {chr(ord('a') + col)}")

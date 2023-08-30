from scipy.optimize import linprog

# Coefficients for inequalities (left-hand side)
A = [[15, 10], [10, 20], [15, 20]]
# Constants for inequalities (right-hand side)
b = [180, 200, 210]
# Coefficients for the objective function (note the negative signs for maximization)
c = [-5, -8]

# Solve the linear programming problem
res = linprog(c, A_ub=A, b_ub=b, method='highs')

# Output the results
print(f"Optimal value of x (Type A circuits): {res.x[0]}")
print(f"Optimal value of y (Type B circuits): {res.x[1]}")
print(f"Maximum Profit: {-res.fun}")

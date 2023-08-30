import matplotlib.pyplot as plt
import numpy as np

# Define the inequality constraints
x = np.linspace(0, 20, 400)
y1 = (180 - 15*x) / 10
y2 = (200 - 10*x) / 20
y3 = (210 - 15*x) / 20

# Plot the inequalities
plt.figure(figsize=(10,10))
plt.plot(x, y1, label=r'$15x + 10y \leq 180$')
plt.fill_between(x, 0, y1, alpha=0.1, color='black')
plt.plot(x, y2, label=r'$10x + 20y \leq 200$')
plt.fill_betweenx(x, 0, y2, alpha=0.1, color='black')
plt.plot(x, y3, label=r'$15x + 20y \leq 210$')
plt.fill_between(x, 0, y3, alpha=0.1, color='black')

# Add some labels and a legend
plt.xlim((0, 20))
plt.ylim((0, 20))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

# Add grid
plt.grid(True, linestyle='--')

# Add legend
plt.legend()

# Show the plot
plt.show()

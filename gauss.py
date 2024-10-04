import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the Gaussian
mu = 53  # mean centered at 53%
sigma = 3  # standard deviation of 3%

# Create an array for percent values from 0 to 100
x = np.linspace(0, 100, 1000)

# Compute the Gaussian function
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Plot the curve
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Percent Voting for Candidate A over B', color='blue')

# Fill under the curve
plt.fill_between(x, y, color='blue', alpha=0.3)

# Label the axes
plt.xlabel('Percent Voting for Candidate A (%)')
plt.ylabel('Probability Density')
plt.title('Gaussian Distribution of Percent Voting for Candidate A over B')

# Show the plot
plt.legend()
plt.grid(True)
plt.show()

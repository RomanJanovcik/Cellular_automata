#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the size of the grid
grid_size = (50, 50)

# Set the initial state of the grid
initial_state = np.random.choice([0, 1], size=grid_size, p=[0.9, 0.1])

# Create a figure and axis
fig, ax = plt.subplots()

# Display the grid as an image
img = ax.imshow(initial_state, cmap='binary')

# Define the rules for the Game of Life
def update(frame):
    global initial_state
    new_state = np.copy(initial_state)
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Count the number of live neighbors
            neighbors = initial_state[(i-1):(i+2), (j-1):(j+2)]
            neighbors_count = np.sum(neighbors) - initial_state[i, j]

            # Apply the rules
            if initial_state[i, j] == 1:
                if neighbors_count < 2 or neighbors_count > 3:
                    new_state[i, j] = 0
            else:
                if neighbors_count == 3:
                    new_state[i, j] = 1

    initial_state = np.copy(new_state)
    img.set_array(initial_state)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=200)

# Show the animation
plt.show()

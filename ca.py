import numpy as np

class CellularAutomaton:
    def __init__(self, grid_size, rules, initial_state):
        """
        Initializes a CellularAutomaton object.

        Args:
            grid_size (tuple): A tuple specifying the size of the grid.
            rules (function): A function that determines the next state based on the current state and the number of neighbors.
            initial_state (numpy.ndarray): A 2D NumPy array representing the initial state of the grid.
        """
        self.grid_size = grid_size
        self.rules = rules
        self.state = initial_state

    def update(self):
        """
        Updates the state of the cellular automaton based on the rules.

        The update is performed by iterating over each cell in the grid, calculating the number of neighbors,
        and applying the rules to determine the new state of each cell.
        """
        new_state = np.copy(self.state)
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                neighbors = self.state[(i-1):(i+2), (j-1):(j+2)]
                neighbors_count = np.sum(neighbors) - self.state[i, j]
                new_state[i, j] = self.rules(self.state[i, j], neighbors_count)
        self.state = new_state

    def simulate(self, num_steps):
        """
        Simulates the cellular automaton for a specified number of steps.

        Args:
            num_steps (int): The number of simulation steps to perform.

        Returns:
            list: A list containing the states of the cellular automaton at each step, including the initial state.
        """
        states = [self.state]
        for _ in range(num_steps):
            self.update()
            states.append(self.state)
        return states

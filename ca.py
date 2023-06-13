import numpy as np

class CellularAutomaton:
    def __init__(self, grid_size, rules, initial_state):
        self.grid_size = grid_size
        self.rules = rules
        self.state = initial_state

    def update(self):
        new_state = np.copy(self.state)
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                neighbors = self.state[(i-1):(i+2), (j-1):(j+2)]
                neighbors_count = np.sum(neighbors) - self.state[i, j]
                new_state[i, j] = self.rules(self.state[i, j], neighbors_count)
        self.state = new_state

    def simulate(self, num_steps):
        states = [self.state]
        for _ in range(num_steps):
            self.update()
            states.append(self.state)
        return states

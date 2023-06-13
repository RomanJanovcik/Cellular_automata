import numpy as np
import unittest
from ca import CellularAutomaton

# Make a list of rules to be tested
# Rule 1 is the Conway's Game of Life rule
def rule1(cell, neighbors_count):
    if cell == 1:
        if neighbors_count < 2 or neighbors_count > 3:
            return 0
        else:
            return 1
    else:
        if neighbors_count == 3:
            return 1
        else:
            return 0

def rule2(cell, neighbors_count):
    if cell == 0 and (neighbors_count == 2 or neighbors_count == 3):
        return 1
    else:
        return 0

rules = [rule1, rule2]

class CellularAutomatonTestCase(unittest.TestCase):
    def test_simulation(self):
        grid_size = (50, 50)
        initial_state = np.random.choice([0, 1], size=grid_size, p=[0.9, 0.1])

        for rule in rules:
            #Create an instance of the CellularAutomaton class from the ca.py module
            automaton = CellularAutomaton(grid_size, rule, initial_state)

            # Simulate for a certain number of steps
            num_steps = 10
            states = automaton.simulate(num_steps)

            # Verify the rule is correctly applied
            for i in range(1, num_steps + 1):
                for x in range(grid_size[0]):
                    for y in range(grid_size[1]):
                        current_state = states[i - 1][x, y]
                        neighbors = states[i - 1][(x - 1):(x + 2), (y - 1):(y + 2)]
                        neighbors_count = np.sum(neighbors) - current_state
                        expected_state = rule(current_state, neighbors_count)
                        self.assertEqual(states[i][x, y], expected_state)

# Run the unit test
unittest.main()

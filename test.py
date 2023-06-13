import numpy as np
import unittest
from ca import CellularAutomaton

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

rule2 = lambda cell, neighbors_count: 1 if cell == 0 and (neighbors_count == 2 or neighbors_count == 3) else 0

class CellularAutomatonTestCase(unittest.TestCase):
    def test_simulation_rule1(self):
        # Set up initial state for Rule 1
        grid_size = (50, 50)
        initial_state = np.random.choice([0, 1], size=grid_size, p=[0.9, 0.1])

        # Create the cellular automaton
        automaton = CellularAutomaton(grid_size, rule1, initial_state)

        # Simulate for 3 steps
        num_steps = 3
        states = automaton.simulate(num_steps)

        # Verify the rule is correctly applied
        for i in range(1, num_steps + 1):
            for x in range(grid_size[0]):
                for y in range(grid_size[1]):
                    current_state = states[i - 1][x, y]
                    neighbors = states[i - 1][(x - 1):(x + 2), (y - 1):(y + 2)]
                    neighbors_count = np.sum(neighbors) - current_state
                    expected_state = rule1(current_state, neighbors_count)
                    self.assertEqual(states[i][x, y], expected_state)

    def test_simulation_rule2(self):
        # Set up initial state for Rule 2
        grid_size = (50, 50)
        initial_state = np.random.choice([0, 1], size=grid_size, p=[0.8, 0.2])

        # Create the cellular automaton
        automaton = CellularAutomaton(grid_size, rule2, initial_state)

        # Simulate for 3 steps
        num_steps = 3
        states = automaton.simulate(num_steps)

        # Verify the rule is correctly applied
        for i in range(1, num_steps + 1):
            for x in range(grid_size[0]):
                for y in range(grid_size[1]):
                    current_state = states[i - 1][x, y]
                    neighbors = states[i - 1][(x - 1):(x + 2), (y - 1):(y + 2)]
                    neighbors_count = np.sum(neighbors) - current_state
                    expected_state = rule2(current_state, neighbors_count)
                    self.assertEqual(states[i][x, y], expected_state)

# Run the unit test
unittest.main()

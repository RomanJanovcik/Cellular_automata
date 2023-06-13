import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from ca import CellularAutomaton

def rules(cell, neighbors_count):
    """
    Determines the next state of a cell based on the current state and the number of neighbors.

    Args:
        cell (int): The current state of the cell (0 means dead and 1 means alive).
        neighbors_count (int): The number of neighboring cells.

    Returns:
        int: The new state of the cell (0 or 1) based on the rules.
    
    This particular case is the Conway's Game of life rule.
    """
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

grid_size = (50, 50)
initial_state = np.random.choice([0, 1], size=grid_size, p=[0.9, 0.1])

# Create an instance of the CellularAutomaton class from the ca.py module
automaton = CellularAutomaton(grid_size, rules, initial_state)

# Simulate the automaton for a certain number of steps
states = automaton.simulate(num_steps=100)

def toggle_animation():
    """
    Toggles the animation between pause and resume.

    This function is called when the pause/resume button is clicked in the GUI.
    """
    if window.animation_running:
        window.animation_running = False
        window.ani.event_source.stop()
        window.start_pause_button.setText("Resume")
    else:
        window.animation_running = True
        window.ani.event_source.start()
        window.start_pause_button.setText("Pause")

# Create the GUI
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cellular Automaton")
        self.animation_running = True

        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)

        self.fig, self.ax = plt.subplots()

        # Create an image plot of the initial state
        self.img = self.ax.imshow(states[0], cmap='binary')

        def update(frame):
            """
            Update the image plot with the state at the current frame.

            Args:
                frame (int): The current frame number.
            """
            self.img.set_array(states[frame])

        # Create an animation using the update function
        self.ani = animation.FuncAnimation(self.fig, update, frames=len(states), interval=200)

        # Create a canvas to display the animation
        self.canvas = FigureCanvas(self.fig)

        self.layout.addWidget(self.canvas)

        # Create the pause button
        self.start_pause_button = QPushButton("Pause", self)
        self.start_pause_button.clicked.connect(toggle_animation)
        self.layout.addWidget(self.start_pause_button)

        self.setCentralWidget(self.central_widget)

        # Start the animation
        self.ani._start()

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

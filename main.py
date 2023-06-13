#! /usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from ca import CellularAutomaton

def rules(cell, neighbors_count):
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

automaton = CellularAutomaton(grid_size, rules, initial_state)
states = automaton.simulate(num_steps=100)

def toggle_animation():
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

        # Create a central widget and layout
        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)

        # Create a figure and axis
        self.fig, self.ax = plt.subplots()

        # Display the states as an animation
        self.img = self.ax.imshow(states[0], cmap='binary')

        def update(frame):
            self.img.set_array(states[frame])

        self.ani = animation.FuncAnimation(self.fig, update, frames=len(states), interval=200)

        # Create a canvas for the animation
        self.canvas = FigureCanvas(self.fig)

        # Add the canvas to the layout
        self.layout.addWidget(self.canvas)

        # Create buttons
        self.start_pause_button = QPushButton("Pause", self)
        self.start_pause_button.clicked.connect(toggle_animation)
        self.layout.addWidget(self.start_pause_button)

        # Set the central widget
        self.setCentralWidget(self.central_widget)

        # Start the animation
        self.ani._start()

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

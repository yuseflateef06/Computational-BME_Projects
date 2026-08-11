# Hopfield Networks Visualization & Analysis

This project provides tools to generate, simulate, and visualize Hopfield Networks[cite: 4, 5, 6]. Created for Assignment 4 on Hopfield Networks by Yusef Lateef, this codebase includes interactive network topology generation and heatmap visualizations tracking state transitions across iterations[cite: 4, 5, 6].

## Features

* **Interactive Network Builder**: Generates fully connected Hopfield network topologies using `PyVis` with nodes laid out on a grid and initialized with random binary states ($\{-1, 1\}$).
* **State Transition Heatmaps**: Creates interactive `Altair` heatmaps equipped with slider controls to inspect node state updates across iterations.
* **Quarto Integration**: Formatted to support automated reporting and web publishing via Quarto.

## Requirements

The codebase depends on the following Python packages[cite: 4, 5]:

* `numpy`[cite: 4, 5]
* `pandas`
* `altair`
* `pyvis`

Install the required dependencies via pip:

```bash
pip install numpy pandas altair pyvis
```
## Usage Example
```
import numpy as np
from network import create_hopfield_network
from visualization import create_state_visualization

# 1. Generate a 16-node fully connected network graph
net = create_hopfield_network(num_nodes=16)
net.show("hopfield_network.html")

# 2. Visualize simulated state iterations using a heatmap
num_nodes = 16
simulated_history = [np.random.choice([-1, 1], size=num_nodes) for _ in range(10)]

heatmap = create_state_visualization(simulated_history, slider_label="Step")
heatmap.save("state_history.html")


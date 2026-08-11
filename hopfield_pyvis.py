import numpy as np
from pyvis.network import Network

def create_hopfield_network(num_nodes):
    # Create a PyVis network
    net = Network(notebook=True, height="500px",
    width= "500px",
    cdn_resources="remote")

    # Add nodes to the network
    nrows = int(np.sqrt(num_nodes))
    for i in range(num_nodes):
        net.add_node(i, 
                     value = int(np.random.choice([-1,1])),
                     x = i%nrows*100, y = i//nrows*100,
                     fixed = False, physics = False)

    # Add edges to the network (fully connected)
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            net.add_edge(i, j)

    return net

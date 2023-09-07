import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the rectangular domain
width = 5.0  # Width of the rectangle
height = 3.0  # Height of the rectangle

# Define the number of nodes in the x and y directions
num_nodes_x = 4
num_nodes_y = 3

# Create a grid of points within the rectangular domain
x = np.linspace(0, width, num_nodes_x)
y = np.linspace(0, height, num_nodes_y)
X, Y = np.meshgrid(x, y)

# Flatten the grid into 1D arrays
X_flat = X.flatten()
Y_flat = Y.flatten()

# Create a list to store the nodes
nodes = []

# Add nodes to the list
for i in range(len(X_flat)):
    nodes.append((X_flat[i], Y_flat[i]))

# Create a list to store the elements (connectivity)
elements = []

# Generate elements by connecting nodes
for i in range(num_nodes_y - 1):
    for j in range(num_nodes_x - 1):
        node1 = i * num_nodes_x + j
        node2 = node1 + 1
        node3 = node1 + num_nodes_x
        node4 = node2 + num_nodes_x
        elements.append((node1, node2, node4))
        elements.append((node1, node4, node3))

# Print nodes and elements (connectivity)
print("Nodes:")
for i, node in enumerate(nodes):
    print(f"Node {i + 1}: ({node[0]}, {node[1]})")

print("\nElements (Node Indices):")
for i, element in enumerate(elements):
    print(f"Element {i + 1}: {element}")

# Plot the mesh
plt.figure(figsize=(8, 6))
for element in elements:
    x_coords = [nodes[node_idx][0] for node_idx in element]
    y_coords = [nodes[node_idx][1] for node_idx in element]
    plt.plot(x_coords + [x_coords[0]], y_coords + [y_coords[0]], 'b-')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('3-Node Mesh for Rectangular Domain')
plt.grid(True)
plt.show()

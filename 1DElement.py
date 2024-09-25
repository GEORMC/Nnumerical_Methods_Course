import numpy as np
import matplotlib.pyplot as plt

# Define the function to assemble the global stiffness matrix
def assemble_stiffness_matrix(nodal_coords, nodal_connectivity, material_props):
    num_nodes = len(nodal_coords)
    K_global = np.zeros((num_nodes, num_nodes))

    for element in nodal_connectivity:
        node1, node2 = element
        x1, x2 = nodal_coords[node1], nodal_coords[node2]
        length = x2 - x1
        k = material_props['E'] * material_props['A'] / length

        # Element stiffness matrix for 1D linear element
        K_local = (k / length) * np.array([[1, -1], [-1, 1]])

        # Assembly into the global stiffness matrix
        K_global[node1:node2+1, node1:node2+1] += K_local

    return K_global

# Apply boundary conditions (Dirichlet)
def apply_boundary_conditions(K, F, bc):
    for node, value in bc.items():
        # Modify stiffness matrix and force vector to enforce boundary condition
        K[node, :] = 0
        K[:, node] = 0
        K[node, node] = 1
        F[node] = value
    return K, F

# Define function to solve FEM problem
def fem_1d(nodal_coords, nodal_connectivity, material_props, boundary_conditions, load):
    num_nodes = len(nodal_coords)

    # Step 1: Assemble global stiffness matrix
    K_global = assemble_stiffness_matrix(nodal_coords, nodal_connectivity, material_props)

    # Step 2: Assemble global force vector
    F_global = np.zeros(num_nodes)
    for node, value in load.items():
        F_global[node] = value

    # Step 3: Apply boundary conditions
    K_global, F_global = apply_boundary_conditions(K_global, F_global, boundary_conditions)

    # Step 4: Solve the system of equations
    displacements = np.linalg.solve(K_global, F_global)
    
    return displacements

# Example Input Data
nodal_coords = np.array([0.0, 0.5, 1.0])  # Coordinates of nodes
nodal_connectivity = np.array([[0, 1], [1, 2]])  # Elements defined by node numbers
material_props = {'E': 210e9, 'A': 1e-4}  # Material properties: E (Young's modulus) and A (Cross-sectional area)
boundary_conditions = {0: 0.0}  # Boundary condition: node 0 is fixed (Dirichlet condition)
load = {2: 1000.0}  # Load applied at node 2

# Solve the FEM problem
displacements = fem_1d(nodal_coords, nodal_connectivity, material_props, boundary_conditions, load)

# Output displacements
print("Nodal Displacements:", displacements)

# Plot the displacements
plt.plot(nodal_coords, displacements, '-o')
plt.xlabel('Position (m)')
plt.ylabel('Displacement (m)')
plt.title('1D FEM Nodal Displacements')
plt.grid(True)
plt.show()

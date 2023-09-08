import tkinter as tk
import numpy as np
from scipy.spatial import Delaunay
import pandas as pd

class MeshGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mesh Generator")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()
        self.polygon_points = []
        self.clicked_points = []

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.node_label = tk.Label(root, text="")
        self.node_label.pack()

        self.draw_button = tk.Button(root, text="Generate Mesh", command=self.generate_mesh)
        self.draw_button.pack()

        self.node_counter = 1
        self.element_counter = 1

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        self.clicked_points.append((x, y))
        self.node_label.config(text=f"Node: ({x}, {y})")

        # Draw a circle at the clicked point with node number
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red")
        self.canvas.create_text(x + 5, y - 5, text=str(self.node_counter))
        self.node_counter += 1

        # Connect the points to form a polygon
        if len(self.clicked_points) > 1:
            x1, y1 = self.clicked_points[-2]
            x2, y2 = self.clicked_points[-1]
            self.canvas.create_line(x1, y1, x2, y2)
            self.element_counter += 1

    def generate_mesh(self):
        if len(self.clicked_points) < 3:
            return  # Need at least 3 points to form a polygon

        # Convert clicked points to numpy array
        points = np.array(self.clicked_points)

        # Perform Delaunay triangulation
        tri = Delaunay(points)

        # Save nodal coordinates and node connectivity to Excel files
        self.save_nodal_coordinates(points)
        self.save_node_connectivity(tri.simplices)

        # Draw the triangular elements with element numbers at centroids
        for simplex in tri.simplices:
            simplex_points = points[simplex]
            for i in range(3):
                x1, y1 = simplex_points[i]
                x2, y2 = simplex_points[(i + 1) % 3]
                self.canvas.create_line(x1, y1, x2, y2, fill="blue")

                centroid_x = (x1 + x2) / 2
                centroid_y = (y1 + y2) / 2
                self.canvas.create_text(centroid_x, centroid_y, text=str(self.element_counter))
            self.element_counter += 1

    def save_nodal_coordinates(self, points):
        df = pd.DataFrame(points, columns=["X", "Y"])
        df.to_excel("nodal_coordinates.xlsx", index=False)

    def save_node_connectivity(self, triangles):
        df = pd.DataFrame(triangles, columns=["Node 1", "Node 2", "Node 3"])
        df.to_excel("node_connectivity.xlsx", index=False)

if __name__ == "__main__":
    root = tk.Tk()
    app = MeshGeneratorApp(root)
    root.mainloop()

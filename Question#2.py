import numpy as np
import matplotlib.pyplot as plt


with open('seq.txt', 'r') as file:
    seq = file.read().strip()

seq_list = list(seq)
seq_list_len = len(seq_list)

t = np.linspace(0, 4 * np.pi, seq_list_len) 
x = np.cos(t)
y = np.sin(t)
z = np.linspace(0, 5, seq_list_len)  

coordinates = np.column_stack((x, y, z))
color_map = {
    "A": "red",
    "C": "green",
    "T": "blue",
    "G": "yellow"
}
colors = [color_map[n] for n in seq_list if n in color_map] 

# Step 4: Visualize the helix with colors
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot each point with its respective color
ax.scatter(x, y, z, c=colors, s=70)  

# Labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Helix Representation with Nucleotide Colors")

plt.show()
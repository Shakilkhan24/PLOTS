import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Generate data
data = np.random.randn(1000, 3)

# 3D Histogram
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
hist, xedges, yedges = np.histogram2d(data[:,0], data[:,1], bins=20)

# Construct arrays for the anchor positions of the bars
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the bars
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', cmap='viridis')

# Add labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Frequency')
plt.title('3D Histogram')
plt.show()

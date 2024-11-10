import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Load the tips dataset ... 
tips = sns.load_dataset('tips')

# Convert categorical columns to numerical for 3D plotting
tips['time_num'] = tips['time'].apply(lambda x: 1 if x == 'Dinner' else 0)
tips['sex_num'] = tips['sex'].apply(lambda x: 1 if x == 'Male' else 0)

# 3D Scatter Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(tips['total_bill'], tips['tip'], tips['time_num'], c=tips['sex_num'], cmap='viridis')

# Add labels
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
ax.set_zlabel('Time (0=Lunch, 1=Dinner)')
legend = ax.legend(*scatter.legend_elements(), title='Sex (0=Female, 1=Male)')
ax.add_artist(legend)
plt.title('3D Scatter Plot')
plt.show()

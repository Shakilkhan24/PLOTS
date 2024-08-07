import matplotlib.pyplot as plt 
import seaborn as sns 
from imports import tips
import numpy as np 


# Compute the correlation matrix
correlation_matrix = tips.corr()

# Visualize the correlation matrix with a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

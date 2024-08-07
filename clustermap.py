import matplotlib.pyplot as plt 
import seaborn as sns 
from imports import tips
import numpy as np

# Create a pivot table for clustermap
pivot_table = tips.pivot_table(index='day', columns='time', values='total_bill', aggfunc=np.mean)

# Visualize the pivot table with a clustermap
sns.clustermap(pivot_table, annot=True, cmap='coolwarm', figsize=(10, 8), cbar_kws={'label': 'Average Total Bill'})
plt.title('Pivot Table Clustermap')
plt.show()

import matplotlib.pyplot as plt 
import seaborn as sns 
from imports import tips 
import numpy as np 

# Create a pivot table
pivot_table = tips.pivot_table(index='day', columns='time', values='total_bill', aggfunc=np.mean)

# Visualize the pivot table with a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(pivot_table, annot=True, cmap='coolwarm', cbar_kws={'label': 'Average Total Bill'})
plt.title('Pivot Table Heatmap')
plt.show()

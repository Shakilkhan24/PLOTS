import matplotlib.pyplot as plt 
import seaborn as sns 
from imports import tips
import numpy as np

# Create a pivot table with multiple aggregations
pivot_table = tips.pivot_table(index='day', columns='time', values='total_bill', aggfunc=[np.mean, np.std])

# Flatten the MultiIndex columns for better visualization
pivot_table.columns = ['_'.join(col).strip() for col in pivot_table.columns.values]

# Visualize the pivot table with a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, cmap='coolwarm', cbar_kws={'label': 'Value'})
plt.title('Pivot Table with Multiple Aggregations')
plt.show()

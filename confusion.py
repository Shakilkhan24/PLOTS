import matplotlib.pyplot as plt 
import seaborn as sns 
from imports import tips
import numpy as np 

# Sample confusion matrix
confusion_matrix = np.array([[35, 5, 2], [4, 45, 6], [1, 3, 50]])
labels = ['Class A', 'Class B', 'Class C']

# Visualize the confusion matrix with a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Heatmap')
plt.show()

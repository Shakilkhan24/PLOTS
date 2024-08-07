import matplotlib.pyplot as plt 
import seaborn as sns 
from imports import tips 

sns.pairplot(tips)
plt.title('pairplot')
plt.show()

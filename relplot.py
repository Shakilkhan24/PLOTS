from imports import tips 
import seaborn as sns 
import matplotlib.pyplot as plt 


# Scatter plot
sns.relplot(x="total_bill", y="tip", data=tips)
plt.title('SCATTER PLOT')
plt.show()

# Line plot
sns.relplot(x="size", y="tip", kind="line", data=tips)
plt.title('Line Plot')
plt.show()

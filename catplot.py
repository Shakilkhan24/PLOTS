import matplotlib.pyplot as plt 
import seaborn as sns 
from imports import tips




# Strip plot
sns.catplot(x="day", y="total_bill", data=tips, kind="strip")
plt.title('strip')
plt.show()

# Swarm plot
sns.catplot(x="day", y="total_bill", data=tips, kind="swarm")
plt.title('swarm')
plt.show()

# Box plot
sns.catplot(x="day", y="total_bill", data=tips, kind="box")
plt.title('box')
plt.show()

# Violin plot
sns.catplot(x="day", y="total_bill", data=tips, kind="violin")
plt.title('violin')
plt.show()

# Point plot
sns.catplot(x="day", y="total_bill", data=tips, kind="point")
plt.title('point')
plt.show()

# Bar plot
sns.catplot(x="day", y="total_bill", data=tips, kind="bar")
plt.title('bar')
plt.show()

# Count plot
sns.catplot(x="day", data=tips, kind="count")
plt.title('count')
plt.show()

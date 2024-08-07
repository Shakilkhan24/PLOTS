import matplotlib.pyplot as plt 
import seaborn as sns 
from imports import tips 


sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")
plt.title('joint_scatter')
plt.show()

sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
plt.title('joint_hex')
plt.show()

sns.jointplot(x="total_bill", y="tip", data=tips, kind="kde")
plt.title('joint_kde')
plt.show()

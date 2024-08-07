import matplotlib.pyplot as plt 
import seaborn as sns 
from imports import tips 

# Univariate distribution
sns.displot(tips["total_bill"], kde=True)
plt.title('histogram')
plt.show()

# Bivariate distribution
sns.displot(tips, x="total_bill", y="tip", kind="kde")
plt.title('kde')
plt.show()



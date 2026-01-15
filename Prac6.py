import seaborn as sns
import scipy
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
mean = 50
sd = 1

# Create a normal distribution
n_data = norm(loc=mean, scale=sd)

# Generate a random sample of size 5
sample1 = n_data.rvs(size=5)
print("\nThe continuous data generated is: ",sample1)

# Compute PDF and CDF values for the sample
pdf_values = n_data.pdf(sample1)
cdf_values = n_data.cdf(sample1)

print("\nThe pdf values of generated data is: ", pdf_values )
print("\nThe cdf values of generated data is: ", cdf_values )

# n=no of trials
# p= probability of success
# pmf=Probability Mass Function
b_data = binom (n=10, p=0.5)
pfs = b_data.pmf(5)
sample2 = b_data.rvs(size=5)
print("\nThe discrete data generated is: ",sample2)
print("\nThe pmf of discrete data generated is: ",pfs)

# Plotting the sample distribution with KDE
sns.histplot(sample1, kde=True, color="c")

# Show the plot
plt.show()

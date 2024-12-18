import matplotlib.pyplot as plt
from scipy import stats
x = [0,1,2,3,4]
y = [2,3,5,4,6] 



slope, intercept, r, p, std_err = stats.linregress(x, y)
def reg(x):
  return slope * x + intercept
regmodel = list(map(reg, x))
plt.scatter(x, y)
plt.plot(x, regmodel)
plt.show()
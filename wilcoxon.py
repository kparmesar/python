#! python3 
# wilcoxon.py - Calculate Wilcoxon signed rank test for 
# nonparametric paired samples
import scipy
from scipy import stats
pre = [90, 94, 82, 80, 92, 88, 82, 80, 88, 82, 78, 80, 88, 94, 80, 82, 90, 86]
post = [86, 94, 82, 82, 90, 92, 82, 88, 90, 94, 84, 86, 96, 98, 82, 88, 84, 94]
dif = [-4, 0, 0, 2, -2, 4, 0, 8, 2, 12, 6, 6, 8, 4, 2, 6, 4, 8]
p = scipy.stats.wilcoxon(pre, post, zero_method='wilcox', correction=False)
p2 = scipy.stats.wilcoxon(dif, zero_method='wilcox', correction=False)
print(p)
print(p2)
#! python3 
# wilcoxon.py - Calculate Wilcoxon signed rank test for 
# nonparametric paired samples
import scipy
from scipy import stats
pre = []
post = []
p = scipy.stats.wilcoxon(pre, post, zero_method='wilcox', correction=False)
print(p)

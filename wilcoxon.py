#! python3 
# wilcoxon.py - Conduct a Wilcoxon signed rank test for nonparametric paired samples
import scipy
from scipy import stats
pre = []
post = []
p = scipy.stats.wilcoxon(pre, post, zero_method='wilcox', correction=False)
print(p)

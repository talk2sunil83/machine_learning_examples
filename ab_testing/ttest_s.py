#%%
import numpy as np
from scipy import stats

#%%
N = 10

a = np.random.rand(N) + 2
b = np.random.rand(N)


var_a = a.var(ddof=1)  # for n-1
var_b = b.var(ddof=1)

s = np.sqrt((var_a + var_b) / 2)
t = (a.mean() - b.mean()) / (s * np.sqrt(2.0 / N))
df = 2 * N - 2
p = 1 - stats.t.cdf(t, df=df)

print(f"t : {t}\t p : {p}")
t2, p2 = stats.ttest_ind(a, b)
print(f"t2 : {t2}\t p2 : {p2}")

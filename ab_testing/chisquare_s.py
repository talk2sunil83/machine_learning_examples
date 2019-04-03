#%%
import numpy as np
from scipy import stats


#%%

data = np.array([[36,14],[30, 25]])
print(data.shape)

#%%
def row_sum(two_d_array):
    return np.sum(two_d_array, axis=1)
    # return  [sum(row) for row in two_d_array]
     

#%%
row_sum(data)

#%%
def col_sum(two_d_array):
    return np.sum(two_d_array, axis=0)
    # return sum(array_data)

#%%
col_sum(data)

#%%
def mat_sum(array_data):
    return np.sum(array_data)
#   return sum(array_data)

#%%
mat_sum(data)

#%%
def chi_square_test(two_d_array):
    rs = row_sum(two_d_array)
    cs = col_sum(two_d_array)
    s = mat_sum(two_d_array)
    two_d_array_shape = two_d_array.shape
    res = 0
    for i in range(two_d_array_shape[0]):
        current_rs = rs[i]
        for j in range(two_d_array_shape[1]):
            current_cs = cs[j]
            expected = current_rs * (current_cs/s)
            actual  = two_d_array[i,j]
            res += ((actual-expected)**2)/expected
    return res
#%%
chi_square_test(data)


#%%
stats.chi2_contingency(data, correction=False)

#%%
stats.fisher_exact(data)

#%% [markdown]
#This is H1
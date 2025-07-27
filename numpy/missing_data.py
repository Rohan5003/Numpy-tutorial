import numpy as np
 #--to check value is nan

a = np.array([1,2, np.nan, 4, np.nan])
print(np.isnan(a))

#---to replace missing values---
cleaned = np.nan_to_num(a, nan=-0)
print(cleaned)

#---to replace issing values completely
print(a[~np.isnan(a)])
import numpy as np

a = np.array([1,2,3])
b = np.array([3,4,5])

print(np.union1d(a,b))
print(np.intersect1d(a,b))
print(np.setdiff1d(a,b))
print(np.setxor1d(a,b))

# to apply set operation in multidimenional array use ravel or flatten

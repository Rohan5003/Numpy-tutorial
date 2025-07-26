import numpy as np
# a = np.array([10, 20, 30])
# b = np.where(a > 15, 1, 0)
# print(b)   # [0 1 1]
# c = np.array([5, 10, 15, 20, 25])
# filtered = c[c > 15]
# print(filtered)   # [20 25]

# d = np.array([1, 0, 3])
# print(np.any(d > 2))   # True
# print(np.all(d > 0))   # False

# e = np.array([10, 15, 20, 25])
# print(e[(e > 10) & (e < 25)])  # [15 20]

a = np.array([10, 15, 20, 25])

condition = a > 15          # [False, False,  True,  True]
negated = ~condition        # [ True,  True, False, False]

print(negated)
print(a[negated])           # [10 15]


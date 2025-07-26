import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(a + b)     # [5 7 9]
# print(a * b)     # [4 10 18]
# print(a ** 2)    # [1 4 9]

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])

# b = np.array([1, 0, 1])

# print(a + b)     output-  [[2 2 4]
#                    [5 5 7]]

# a = np.array([[1, 2], [3, 4]])

# print(np.sum(a))        # 10
# print(np.mean(a))       # 2.5
# print(np.max(a))        # 4
# print(np.min(a))        # 1
# print(np.std(a))        # standard deviation

# print(np.sum(a, axis=0))  # column-wise [4 6]
# print(np.sum(a, axis=1))  # row-wise    [3 7]

a = np.array([10, 15, 20, 25])
print(a[a > 15])  # [20 25]


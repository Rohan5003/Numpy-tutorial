import numpy as np

# b = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])

# print(b[1, :])   # Row 1 → [4 5 6]
# print(b[:, 2])   # Column 2 → [3 6 9]

# a = np.array([1, 2, 3, 4, 5])
# print(a[a > 2])  # Output: [3 4 5]

# a = np.array([10, 20, 30, 40, 50])
# print(a[[1, 3]])  # Output: [20 40]

a = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

# Extract:
# 1. Middle row
# 2. Last column
# 3. Elements greater than 45
# print(a[1,: ])
# print(a[ : ,2])
# print(a[a>45])

# modifiy row and column

# a[1, 1] = 555
# print(a)

# a[0] = [1, 2, 3]
# print(a)

# a[:, 2] = [100, 200, 300]
# print(a)

# a[a > 100] = 0
# print(a)

print(a[[0,2]])
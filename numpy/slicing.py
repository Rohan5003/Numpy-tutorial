import numpy as np

# a = np.array([10, 20, 30, 40, 50])
# print(a[0])     # Output: 10 (1st element)
# print(a[-1])    # Output: 50 (last element)

# b = np.array([[1, 2, 3],
#               [4, 5, 6]])
# print(b[0, 0])  # Output: 1  (1st row, 1st column)
# print(b[1, 2])  # Output: 6  (2nd row, 3rd column)

# c = np.array([
#     [[1, 2],
#      [3, 4]],

#     [[5, 6],
#      [7, 8]]
# ])
# print(c[1, 0, 1])  # Output: 6
# # Explanation: 2nd matrix, 1st row, 2nd column

a = np.array([10, 20, 30, 40, 50])
print(a[1:4])    # Output: [20 30 40]
print(a[:3])     # Output: [10 20 30]
print(a[::2])    # Output: [10 30 50]

b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(b[0:2, 1:])   # Output:
# [[2 3]
#  [5 6]]

print(b[:, 1])      # Output: [2 5 8] (All rows, 2nd column)
print(b[1, :])      # Output: [4 5 6] (2nd row, all columns)

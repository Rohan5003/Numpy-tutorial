import numpy as np

# a = np.array([[1, 2], [3, 4]])
# for x in np.nditer(a):
#     print(x, end=' ')

# b = np.array([[1, 2], [3, 4]])
# for x in np.nditer(b, op_flags=['readwrite']):
#     x[...] = x * 2 #x[...]  ==  x[:]  ==  the entire content

# print(b)

# c = np.array([[10, 20], [30, 40]])
# for idx, val in np.ndenumerate(c):
#     print(f"Index: {idx}, Value: {val}")

# def range_func(x):
#     return np.max(x) - np.min(x)

# d = np.array([[1, 2, 3],
#               [4, 5, 6]])

# result = np.apply_along_axis(range_func, axis=1, arr=d)
# print(result)

# a = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# for x in a:
#     print(x)

# a = np.array([
#     [1, 2],
#     [3, 4]
# ])

# for x in np.nditer(a, op_flags=['readwrite']):
#     x[...] = x**2
#     print(a)

# a = np.array([
#     [5, 6],
#     [7, 8]
# ])
# for idx, val in np.ndenumerate(a):
#     print(f"index : {idx}, value {val}")

# a = np.array([
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ])

# def sum_square(x):
#     return np.sum(x**2)
# result = np.apply_along_axis(sum_square, axis = 1, arr = a)
# print(result)

# import numpy as np

a = np.array([
    [[1, 2, 3],
     [4, 5, 6]],
    
    [[7, 8, 9],
     [10, 11, 12]]
])  # Shape: (2, 2, 3)

# Let's say we want to iterate along axis 0 instead of last axis (default)
# So we move axis 0 to the last position
b = np.moveaxis(a, 0, -1)  # shape becomes (2, 3, 2)

for x in np.nditer(b, flags=['external_loop']):
    print(x)
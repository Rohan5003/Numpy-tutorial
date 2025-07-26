import numpy as np
#Operations work only if arrays are broadcastable (same shape or compatible shapes).

# These are all element-wise.

# x = np.array([2, 4, 6])
# y = np.array([1, 2, 3])
# a = np.array([[1, 2, 3],
#               [4, 5, 6]])

# # print(x + y)
# # print(x * y)
# # print(np.power(x, y))
# # print(x // y)
# b = np.sum(a, axis=0 )
# b = np.sum(a, axis=1 )
# print(b)

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])

# print("Total Sum:", np.sum(a))
# print("Mean (overall):", np.mean(a))
# print("Column-wise Sum:", np.sum(a, axis=0))
# print("Row-wise Mean:", np.mean(a, axis=1))

# b = np.array([
#     [1, 3],
#     [5, 7]
# ])

# # Predict these outputs:
# print(np.std(b))            # ?
# print(np.var(b, axis=0))    # ?

# c = np.array([
#     [[1, 2], [3, 4]],
#     [[5, 6], [7, 8]]
# ])

# c = np.array([
#     [[1, 2], [3, 4]],
#     [[5, 6], [7, 8]]
# ])

# c = np.array([
#     [[1, 2], [3, 4]],
#     [[5, 6], [7, 8]]
# ])
# print("sum : ", np.sum(c, axis=0))

a = np.array([1, 4, 9, 16, -25])

print("Square root:", np.sqrt(np.abs(a)))
print("Exponential:", np.exp([1, 2, 3]))
print("Logarithm:", np.log([1, np.e, 10]))  # e ≈ 2.718
print("Power of 2:", np.power([2, 3], 2))




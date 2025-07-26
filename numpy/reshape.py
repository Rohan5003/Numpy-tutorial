import numpy as np

# a = np.array([1, 2, 3, 4, 5, 6])
# b = a.reshape((2, 3))  # 2 rows, 3 columns
# print(b)

# a = np.array([[1, 2], [3, 4]])

# ravel() and flatten() in detail — both are used to convert a multi-dimensional NumPy array into a 1D array, but there are some key differences.
# print(a.flatten())  # returns a *copy*
# print(a.ravel())    # returns a *view* (modifies original)
#Use flatten() when you want a completely new array, and ravel() when memory efficiency matters.

# a = np.array([[1, 2], [3, 4]])
# print(a.T)

#When you don't know how many rows/columns, use -1 to auto-calculate.
# a = np.array([1, 2, 3, 4, 5, 6])
# print(a.reshape(-1, 2))  # Automatically determine rows
# print(a.reshape(2,-1))

#expand_dims adds extra dimensions (for batch inputs in ML):
# a = np.array([1, 2, 3])
# b = np.expand_dims(a, axis=0)  # Shape becomes (1, 3)
# print(b)

#squeeze removes unnecessary dimensions:
# a = np.array([[[1, 2, 3]]])
# print(np.squeeze(a))  # Removes extra dimension → [1 2 3]

# c = np.expand_dims(a, axis=1)
# print(c)
# print(c.shape)

# a = np.array([[1, 2], [3, 4]])
# print("Original:\n", a)

# swapped = np.swapaxes(a, 0, 1)
# print("Swapped axes 0 and 1:\n", swapped)


# a = np.array([
#     [[1, 2], [3, 4]],
#     [[5, 6], [7, 8]]
# ])
# print("Shape:", a.shape)  # (2, 2, 2)

# swapped = np.swapaxes(a, 0, 2)
# print(swapped)
# print("New Shape:", swapped.shape)

# a = np.array([
#   [[1, 2], [3, 4]],
#   [[5, 6], [7, 8]]
# ])  # shape (2, 2, 2)

# # Rearranging axes from (0, 1, 2) to (1, 0, 2)
# b = np.transpose(a, (1, 0, 2))
# print(b)
# print(b.shape)  # (2, 2, 2)

# a = np.arange(24)
# print(a.reshape(2, 3, 4))

# a = np.arange(6)
# print(np.reshape(a, (2, 3)))

# a = np.array([1, 2, 3])
# b = np.resize(a, (2, 4))
# print(b)

a = np.array([1, 2, 3])
b = np.resize(a, (3, 3))
print(b)
print(b.shape)

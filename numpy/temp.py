import numpy as np
# a = np.array([
# #   [[1, 2], [3, 4]],
# #   [[5, 6], [7, 8]]
# # ])
# # # print(a.shape)  # (2, 2, 2)

# # # b = np.swapaxes(a, 0, 2)
# # # # print(b.shape)  # (2, 2, 2)
# # # print(b)

# # c = np.transpose(a,(1,0,2))
# # print(c)

# a = np.random.rand(2, 3, 4)

# # Transpose with full change
# b = np.transpose(a, (2, 0, 1))  # Now axes: (4, 2, 3)

# # Swapaxes only swaps 2 axes
# c = np.swapaxes(a, 0, 1)        # Still shape: (3, 2, 4)

# # print(np.array_equal(b, c))  # ❌ False
# print(b)
# print(c)

a = np.arange(1,11)

print(a)
b = a[a%2 == 0]
c = b*10
d = a[a<5]
# np.where(c%2 == 0, "even", "odd"
print(np.where(a<5, -1, a))

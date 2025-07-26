import numpy as np

# a = np.random.rand(3)
# b = np.random.rand(2, 3)

# print(a)
# print(b)

# a = np.random.rand(5)
# print(a)

# b = np.random.randn(3,4)
# print(b)

# c = np.random.randint(10,50, size=(4,4))
# print(c)

# x = [5, 10, 15, 20]
# d = np.random.choice(x, size = 6)
# print(d)

# np.random.seed(42)

# e = np.random.rand(3)
# print(e)

arr_1d = np.array([1, 2, 3, 4, 5])
print("Original 1D array:", arr_1d)
np.random.shuffle(arr_1d)
print("Shuffled 1D array:", arr_1d)
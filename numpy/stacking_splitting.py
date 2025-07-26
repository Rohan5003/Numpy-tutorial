import numpy as np

# a = np.array([[10, 20, 30, 40],
#               [50, 60, 70, 80]])

# # Shape: (2, 4) → 2 rows, 4 columns

# b = np.split(a, 2, axis=1)  # split into 2 vertical parts (along columns)

# for part in b:
#     print(part)


# c = np.array([[1, 2],
#               [3, 4],
#               [5, 6],
#               [7, 8],
#               [9, 10],
#               [11, 12]])

# # Shape: (6, 2)

# d = np.vsplit(c, 3)  # 3 parts, must split evenly by rows

# for x in d:
#     print(x)
# #✅ vsplit is shorthand for split(..., axis=0) — splits along rows.

# a = np.array([[100, 200],
#               [300, 400],
#               [500, 600],
#               [700, 800],
#               [900, 1000]])

# # Shape: (5, 2) — 5 rows, can’t be split equally into 3

# b = np.array_split(a, 3, axis = 0)

# for part in b:
#     print(part)

# a = np.arange(24).reshape(2, 3, 4)
# print("Original shape:", a.shape)
# print("Original array:\n", a)

# # Split along axis=2 → 4 columns per matrix → split into 2 parts (2 columns each)
# b = np.split(a, 2, axis=2)

# for i, part in enumerate(b):
#     print(f"\nPart {i+1}:\n", part)

a = np.arange(18).reshape(2, 3, 3)
print("Shape:", a.shape)

# axis=1 is vertical in 3D (i.e., splitting row groups)
b = np.array_split(a, 3, axis=1)

for i, part in enumerate(b):
    print(f"\nPart {i+1}:\n", part)






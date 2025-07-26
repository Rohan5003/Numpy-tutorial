import numpy as np

# A = np.array([[1, 2],
#               [3, 4]])

# B = np.array([[5, 6],
#               [7, 8]])

# print(np.dot(A, B))      # Method 1
# print(A @ B)             # Method 2 (shorthand)
# print(np.matmul(A, B))   # Method 3

# X = np.array([[2, 4, 1],
#               [0, 1, 0]])

# Y = np.array([[1, 0],
#               [3, 2],
#               [4, 5]])

# Z = np.dot(X, Y)
# print(Z)

# import numpy as np

# I = np.eye(3)  # 3×3 identity matrix
# print(I)

# import numpy as np

# A = np.array([[4, 7],
#               [2, 6]])

# A_inv = np.linalg.inv(A)
# print("Inverse:\n", A_inv)

# # Verify
# # print("A * A_inv:\n", np.dot(A, A_inv))
# result = np.dot(A, A_inv)
# print(np.round(result, decimals=5))

# A = np.array([[4, 6],
#               [3, 8]])

# det = np.linalg.det(A)
# print("Determinant:", det)

# B = np.array([[1, 2],
#               [2, 4]])

# print("Det:", np.linalg.det(B))



# A = np.array([[2, 4],
#               [1, 2]])

# rank = np.linalg.matrix_rank(A)
# print("Rank:", rank)

# B = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])

# print("Rank:", np.linalg.matrix_rank(B))

# A = np.array([[2, 0],
#               [0, 3]])

# eigenvalues, eigenvectors = np.linalg.eig(A)

# print("Eigenvalues:", eigenvalues)
# print("Eigenvectors:\n", eigenvectors)

A = np.array([[4, -2],
              [1, 1]])

eig_vals, eig_vecs = np.linalg.eig(A)

print("Eigenvalues:", eig_vals)
print("Eigenvectors:\n", eig_vecs)

v1 = eig_vecs[:, 0]
print(np.allclose(A @ v1, eig_vals[0] * v1))  # Should return True

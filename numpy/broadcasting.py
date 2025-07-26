import numpy as np
a = np.array([[1], [2], [3]])  # shape (3,1)
b = np.array([10, 20, 30])     # shape (3,) -> treated as (1,3)

result = a + b
print(result)
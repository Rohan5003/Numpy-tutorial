import numpy as np

# a = np.array([1,2,3,4,5])
# print(np.add.reduce(a))   # reduce array to single value
# print(np.multiply.reduce(a))

# b = np.array([5,6,7,8,9])
# print(np.add.accumulate(b))   adds successivley

# c = np.array([3,4,5,6,7])
# print(np.multiply.outer(a,c))

# def add_ten(x):
#     return x+10

# vec_add_ten = np.vectorize(add_ten)
# a = np.array([1,2,3])

# print(vec_add_ten(a))

#-------------in 2d----------------

a = np.array([[1,2,3],
              [4,5,6]])
# print(np.add.reduce(a, axis=0))  #axis=0 collapses row wise
# print(np.add.reduce(a, axis=1))  #axis=1 collapses column wise

#---------------in 3d----------------

b = np.array([
             [[1,2],
              [4,5]],

              [[7,9],
               [6,8]]
               ])
# print(np.add.reduce(b, axis = 2))
# print(np.add.accumulate(b, axis=2))
out = np.add.outer(b,a)  # elements of b gets added to a one by one
print(out)
print(out.shape)

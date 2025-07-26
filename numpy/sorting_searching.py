import numpy as np

# a = np.array([[3,1,7], [4,6,5]])
# print(np.sort(a, axis=1))  #default row wise sort
# print(np.sort(a, axis=0))      # column wise sort

# b = np.array([1,2,4,6,5])
# print(np.argsort(b))  #reutnrs indice that would sort the array

# c = np.array([23,45,34,12,12])
# print(np.where(c>25))  #reutrns indices where condition is true
# print(np.where(c%2 == 0, "even", "odd"))  # even is written first the odd if condition is true

# print(np.searchsorted(c , 25))  # returns index to insert elemnt in a sorted array to maintain order

# print(np.count_nonzero(a)) # counts number of non zero elements
# print(np.count_nonzero(a > 4)) # condition is used 
# print(np.unique(c))  # finds unique elements
# vals, counts = np.unique(c, return_counts=True)
# print (vals)
# print(counts)

# labels = np.array(['cat', 'dog', 'cat', 'fish', 'dog', 'dog'])
# vals, counts = np.unique(labels, return_counts = True) 
# print(vals)
# print(counts)

scores = np.array([87, 92, 45, 99, 78, 84])
sorted_indices = np.argsort(scores)[ :: -1]

top3scores = scores[sorted_indices[:3]]
top3indices = sorted_indices[:3]
print(f"top three scores are {top3scores}")







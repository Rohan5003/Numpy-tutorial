import numpy as np
#----normalisation
# data = np.array([10,20,30,40,50])
# normalised = (data - data.min())/(data.max() - data.min())
# print(f"normalised : {normalised}")


#------standarisation (z-score)----
# mean = data.mean()
# std = data.std()
# standarisation = (data - mean) / std
# print(f"standarisation : {standarisation}")

# a = np.array([[1,2],[3,4],[5,6]])
# mean = a.mean()
# std = a.std()
# standard = (a - mean)/std
# print(np.round(standard, 3))

#---scaling to custom range---
# scaled = 100*(data - data.min())/(data.max() - data.min())
# print(scaled)


#---as a fucntion---

def scale_range(data, low_limit, upper_limit):
    old_min = data.min()
    old_max = data.max()
    scaled = upper_limit + ((data - old_min) / (old_max - old_min)) * (upper_limit - low_limit)

    return scaled
a = np.array([20, 34, 55, 60, 70])
scaled_arr = scale_range(a, 10,50)
print(f"original data : {a}")
print(f"scaled data for custom range : {scaled_arr}")



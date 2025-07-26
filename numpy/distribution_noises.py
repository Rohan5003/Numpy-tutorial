import numpy as np
# np.random.seed(0)
# x=np.random.rand(5)   # unform distribution
# print(x)

# y = np.random.randn(5) #normal distribution , mean = 0, std = 1
# print(y)

# #mea = 50, std = 10
# a = np.random.normal(loc=50, scale=10,size=5)
# print(a)   #most values around 50

# b = np.random.randint(10,50, size=(2,3))
# print(b)    # random int of shape (2,3)

# c = np.random.choice([0,1], size=10, p=[0.7, 0.3]) #biased coin  0(haeds) has 70% chance and 1(tails) has 30% chance
# print(f"simulated scores {c}")

#-------------------noise------------------------

data = np.array([10,20,30,40,50])

# noise = np.random.normal(0,2, size=data.shape)  #gaussian noise
# noisy_data = noise + data
# print(noisy_data)

# noise = np.random.uniform(low=-0.2, high=0.2, size=data.shape)  #unform noise
# noisy_data2 = noise + data
# print(noisy_data2)

image = np.random.randint(0,255,(3,3)).astype(float)   #grayscale image
noise = np.random.normal(0,10,image.shape)
noisy_image3 = noise+image
print(noisy_image3)
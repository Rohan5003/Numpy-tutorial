import numpy as np
a = np.array([1,2,3])
b = a.copy()

b[0] = 100   #changing b doesnot affect array a(original array)
print(f"original array : {a}")
print(f"copy array : {b}")

c = a.view()
c[0] = 50
print(f"original array {a}")   # modifying data will change original data  shares data with original array
print(f"view : {c}")

# to check array is a view 
print(c.base is a)  # true for view
print(b.base is a)  # false for copy

#--------------2d/3d array---------------
d = np.array([[1,2],[3,4]])
e = d.view()
e[0,0] = 300
print(f"original : {d}")
print(f"view  : {e}")

f = np.array([1,2,3,4])
g = f[1:3]    #    this is a view
g[0] = 100
print(f"original : {f}")
print(f"view : {g}")
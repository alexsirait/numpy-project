import numpy as np

a = np.arange(10)**2
# display
print(a)

# get value
print("get element 1 = ", a[0])
print("get element 3 = ", a[2])
print("get last element = ", a[-1])

# slicing
print("emelent 1-6 = ", a[0:6])  # from start to end
print("emelent 6 - last element = ", a[5:]) 
print("emelent first - element 6 = ", a[:6]) 

# iteration
for i in a:
    print("value: ", i)
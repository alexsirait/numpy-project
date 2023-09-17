import numpy as np

a = np.array(([1,2,3],[4,5,6]))

print("matrix a dengan ukuran :", a.shape)
print(a)

# transpose matrix
print("transpose matrix dari a :")
print(np.transpose(a));
# print(a.transpose());
# print(a.T);

# flatten array, vector baris
print("flatten matrix a :")
print(np.ravel(a))
# print(a.ravel())

# reshape matrix
print("reshape matrix a :")
print(a.reshape(3,2))

# resize matrix
print("resize matrix a:")
a.resize(3,2)
print(a);
print("matrix a dengan ukuran", a.shape)
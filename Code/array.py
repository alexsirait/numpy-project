import numpy as np

# vektor
a = np.array([1,2,3,4,5])

# vector dengan range
b = np.arange(1,10,2)

# linspace
c = np.linspace(1,10,2)

# multydimention
d = np.array([(1,2,3), (4,5,6)])

# null
e = np.zeros((5,5)) # row, column

# one
e = np.ones((5,5)) # row, column

# matrix identity
f1 = np.identity(5)
f2 = np.eye(5)

# display
print(f2)
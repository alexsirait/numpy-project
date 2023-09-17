import numpy as np

# memberikan type data kepada array
a = np.array(([1,2,3], [4,5,6]), dtype=float);

# memberikan array dengan sebuah function

def kuadrad(x,y):
    return y**2

def jumlah(x,y):
    return x + y

b = np.fromfunction(kuadrad, (2,10), dtype=float);
c = np.fromfunction(jumlah, (8,8), dtype=int)

# membuat array matrix dengan menggunakan iterable

iterable = (x**2 for x in range(10))

d = np.fromiter(iterable, dtype=int);

# mutiple array

dTipe = [('nama', "S255"), ('tinggi', float)]

data = [
    ('alex', 150),
    ('bonar', 160),
    ('sirait', 170),
]

e = np.array(data, dtype=dTipe, copy=True);


# display
print(e)
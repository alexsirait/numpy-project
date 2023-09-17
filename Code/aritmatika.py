import numpy as np

# python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# penjumlahan
hasil = anp + bnp

# pengurangan
hasil = anp - bnp

# perkalian
hasil = anp * bnp

# pembagian
hasil = anp / bnp

# kuadrad
hasil = anp**2

# multydimention
c = np.array(([1,2,3], [4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))

hasil = c + d
hasil = c * d
# display
print(hasil)
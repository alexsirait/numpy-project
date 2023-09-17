import numpy as np

a = np.floor(np.random.randn(1,6)*10)

print(a)

print('nilai max dari a = ', a.max())
print('posisi max dari a = ', a.argmax())
print('-------')
print('nilai min dari a = ', a.min())
print('pisisi min dari a = ', a.argmin())
print('-----------')
print('mengurutkan nilai a = ')
print(np.sort(a))
print(np.argsort(a))
import numpy as np

dtipe = [('nama', 'S20'), ('tinggi', int)]
data = [
    ('alex', 170),
    ('sirait', 150),
    ('bobi', 160),
]

a = np.array(data, dtype=dtipe, copy=True)

# display
print(np.sort(a, order='nama'))
print(np.sort(a, order='tinggi'))
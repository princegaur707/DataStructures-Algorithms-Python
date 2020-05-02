import numpy as np
m = np.array([[1,2], [3,4], [5,6]], int)
na=np.rot90(m, k=1, axes=(0, 1))  # k: no. of rotations, axes:from 1st to 2nd
print(m)
print(na)
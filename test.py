import numpy as np 
mask=np.zeros(shape=(8,8),dtype=bool)
mask[0:4,0:4]=True
for r,row in enumerate(mask):
    print(r,row)
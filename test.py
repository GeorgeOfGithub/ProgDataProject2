
import io
import pandas as pd
import numpy as np

dataname="test.bin"
xn = 32
yn = 32
zn = 8192


data = None
dt = np.dtype([('a', 'f4'), ('b', 'f4'), ('c', 'f4')])
data = np.fromfile(dataname,np.float32)
df = np.zeros(shape=(xn,yn,zn))
for x in range(xn):
    for y in range(yn):
        for z in range(zn):
            df[x,y,z] = data[x+y+z]

#df = pd.DataFrame(df)

print(df)



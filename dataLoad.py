import struct
import pandas as pd
import numpy as np
# Author: Lucas Buhelt
# This function loads data from a .bin
#
# Input: bin file located in same location as python file, with file name extension
#
# Output: data as a 3d numpy array

def dataLoad(dataname,Nx,Ny,Nz):

    data = None

    try:
        data = np.fromfile(dataname,np.float32)
        if len(data) < Nx*Ny*Nz:
            print("\nThe size of the matrix is too large for the amount of data!\n")
            return
        df = np.zeros(shape=(Nx,Ny,Nz))
        n=0
        for x in range(Nx):
            for y in range(Ny):
                for z in range(Nz):
                    df[x,y,z] = data[n]
                    n=n+1

    except OSError:
        print("\n404 FILE NOT FOUND! TRY ANOTHER FILENAME\n")
    return df


import struct
import pandas as pd
import numpy as np
# Author: Lucas Buhelt
# This function loads data from a csv or text file
#
# Input: file located in same location as python file, with file name extension
#
# Output: data, with all erroneous line removed

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
        colnames=['Temperature', 'Growth rate', 'Bacteria'] 
        # data = pd.read_csv(dataname,delim_whitespace=True,names=colnames,header=None)
        # data,error_amount = scan(data)
        # print("File loaded succesfully with errors in " + str(error_amount) + " lines.")
        # print("These have been removed. Returning to main menu...")
    except OSError:
        print("\n404 FILE NOT FOUND! TRY ANOTHER FILENAME\n")
    return df

# def scan(data):
#     # This function goes through the dataframe and searches for lines with errors
#     # Printing the errors and removing the errors are 2 different things
#     before = len(data)

#     # 3 for-loops for the 3 different columns where errors are printed
#     for i in range(len(data)):
#         if(data.iloc[i,0]<10.0 or data.iloc[i,0]>60.0):
#          print("Error in line "  + str(i) +" :Temperature outside scope")

#     for i in range(len(data)):
#         if(data.iloc[i,1]<0):
#             print("Error in line "  + str(i) +" :Negative growth")

#     for i in range(len(data)):
#         if(data.iloc[i,2]<1 or data.iloc[i,2]>4):
#             print("Error in line "  + str(i) +" :Wrong bacteria type")

#     # Using the drop function from pandas, using a new drop function for each condition
#     # because we couldnt get it to work in one function with "and"
#     data = data.drop(data[data.iloc[:,0] > 60.0].index)
#     data = data.drop(data[data.iloc[:,0] < 10.0].index)
#     data = data.drop(data[data.iloc[:,1] < 0.0].index)
#     data = data.drop(data[data.iloc[:,2] < 1.0].index)
#     data = data.drop(data[data.iloc[:,2] > 4.0].index)

#     # Returns data and amount of error lines
#     return(data, before - len(data))        

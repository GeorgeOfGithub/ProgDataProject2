import numpy as np

def dataStatistics(data,statistic,Yref,Zref,DeltaX):
#dataStatistics function calculates one of three possible statistics, which
#are single Ny*Nz matrices calculated along the x-dimension
#
# Usage: result = dataStatistics(data,statistic,Yref,Zref,DeltaX)
#
# Inputs: data(Nz*Ny*Nx array containing wind speed values)
#         statistic(string specifying the statistic that should be calculated)
#         Yref,Zref(y- and z-coordinate for the cross-correlation, when statistic is Croos correlation)
#         DeltaX(separation in x-coordinate for the cross-correlation, , when statistic is Croos correlation)
# Output: result(2-dimensional array Ny*Nz containing the calculated statistic)
    
    statistic = statistic.upper()
    Nx=len(data[:,0,0])
    if statistic == "MEAN":
        sum1=0
        for x in range (Nx):
            sum1=sum1+data[x,:,:]
        result=sum1/Nx
    elif statistic == "VARIANCE":
        sum1=0
        sum2=0
        for x in range (Nx):
            sum1=sum1+data[x,:,:]
        M=sum1/Nx
        for x in range(Nx):
            sum2=sum2+(data[x,:,:]-M)*(data[x,:,:]-M)
        result=sum2/Nx
    elif statistic == "CROSS-CORRELATION":
        sum1=0
        for x in range(Nx-DeltaX):
            sum1=sum1+data[x,:,:]*data[x+DeltaX,Yref,Zref]
        result=sum1/(Nx-DeltaX)
    return result
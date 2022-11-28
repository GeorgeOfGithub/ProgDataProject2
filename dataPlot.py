import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#statistic={"Mean", "Variance", "Cross correlation"}

#from data I will receive from statistics I extract length of Ny and Nz

def dataPlot(result, statistic):
    statistic = statistic.lower()
    x = np.arange(result.shape[1])
    y = np.arange(result.shape[0])
    X, Y = np.meshgrid(x, y)
    
    CS=plt.contour(X, Y, result)
    
    ## Create a simple contour plot with labels using default colors.  The
    # inline argument to clabel will control whether the labels are draw
    # over the line segments of the contour, removing the lines beneath
    # the label 
      
    plt.clabel(CS, inline=1, fontsize=10)
    plt.xlabel("Ny")
    plt.ylabel("Nz")

    if statistic == 'mean':
        plt.title('Mean of wind speeds')
    elif statistic=="variance":
        plt.title('Variance of wind speeds') 
    elif statistic=="cross correlation":
        plt.title('Cross correlation of wind speeds')  
    else:
        print("Not valid option. Choose Mean, Variance or Cross correlation ")
    
    plt.show()
 
    




#print(dataPlot(data,statistic))


        
        
        
        
        

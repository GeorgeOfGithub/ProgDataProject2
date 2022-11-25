import numpy as np
import pandas as pd
import displayMenu
import dataLoad as dL
import dataStatistics as dS

pd.options.mode.chained_assignment = None

def menu():
    menuItems = np.array(["Load data from file","Display Statistics", "Plot data","Display data as table", "Quit"])
    filename = ""
    data = None
    while True:
        # Display menu options and ask user to choose a menu item
        print("MENU")
        choice = displayMenu.displayMenu(menuItems)
        # Menu item chosen
        # ------------------------------------------------------------------
        # 1. Load data from file
        if choice == 1:
            
            filename = input("Please enter name of file: ")
            Nx = input("Please enter Nx: ")
            Ny = input("Please enter Ny: ")
            Nz = input("Please enter Nz: ")
            if Nx.isdigit() and Ny.isdigit() and Nz.isdigit():
                Nx = int(Nx)
                Ny = int(Ny)
                Nz = int(Nz)
                data = dL.dataLoad(filename,Nx,Ny,Nz)
            else:
                print("Error: One or more of the inputs are not whole numbers!\n")
        # ------------------------------------------------------------------
        # 2. Display Statistics        
        elif choice == 2:
            if data is None:
                print("\nError: No file selected!\n")
            else:
                print("Statistics")
                statistics=np.array(["Mean",
                                     "Variance",
                                     "Cross-correlation"])
                description=np.array([
                    "Mean value for each point in the y-z plane",
                    "Variance of each point in the y-z plane",
                    "Cross correlation at lag Dx between each time series in the y-z plane",])
                selected=int(displayMenu.displayMenu(description))-1
                Yref=0
                Zref=0
                Dx=0
                if selected==2:
                    Yref = input("Please enter Yref: ")
                    Zref = input("Please enter Zref: ")
                    Dx = input("Please enter Dx: ")
                statistic=dS.dataStatistics(data,statistics[selected],Yref,Zref,Dx)
                print(statistic)
        # ------------------------------------------------------------------
        # 4. Plot data
        elif choice == 3:
            print("test")
            # if data is None:
            #     print("\nError: No file selected!\n")
            # else:
            #     dP.dataPlot(data)   
        # ------------------------------------------------------------------
        # 5. Display current file after filters   
        elif choice == 4:
            if data is None:
                print("\nError: No file selected!\n")
            else:
                print(data)
        # ------------------------------------------------------------------
        # 6. Quit
        elif choice == 5:
        # End
            break        

menu()
import numpy as np
import pandas as pd
import displayMenu
import dataLoad as dL

pd.options.mode.chained_assignment = None

def menu():
    menuItems = np.array(["Load data from file", "Filter data","Display Statistics", "Plot data","Display data as table", "Quit"])
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
            Nx = int(Nx)
            Ny = int(Ny)
            Nz = int(Nz)
            #Original_data = dL.dataLoad(filename).copy()
            data = dL.dataLoad(filename,Nx,Ny,Nz)
        # ------------------------------------------------------------------
        # 2. Filter data
        elif choice == 2:
            print("test")
            # if data is None:
            #     print("\nError: No file selected!\n")
            # else:
            #     data = dF.dataFilter(data,Original_data)
        # ------------------------------------------------------------------
        # 3. Display Statistics        
        elif choice == 3:
            print("test")
            # if data is None:
            #     print("\nError: No file selected!\n")
            # else:
            #     print("Statistics")
            #     statistics=np.array(["Mean Temperature",
            #                          "Mean Growth rate",
            #                          "Std Temperature",
            #                          "Std Growth rate",
            #                          "Rows",
            #                          "Mean Cold Growth rate",
            #                          "Mean Hot Growth rate"])
            #     description=np.array([
            #         "Mean (average) Temperature",
            #         "Mean (average) Growth rate",
            #         "Standard deviation of Temperature",
            #         "Standard deviation of Growth rate",
            #         "The total number of rows in the data",
            #         "Mean (average) Growth rate when Temperature is less than 20 degrees",
            #         "Mean (average) Growth rate when Temperature is greter than 50 degrees"])
            #     selected=int(displayMenu.displayMenu(description))-1
            #     statistic=dS.dataStatistics(data, statistics[selected])
            #     print(statistic)
        # ------------------------------------------------------------------
        # 4. Plot data
        elif choice == 4:
            print("test")
            # if data is None:
            #     print("\nError: No file selected!\n")
            # else:
            #     dP.dataPlot(data)   
        # ------------------------------------------------------------------
        # 5. Display current file after filters   
        elif choice == 5:
            if data is None:
                print("\nError: No file selected!\n")
            else:
                print(data)
        # ------------------------------------------------------------------
        # 6. Quit
        elif choice == 6:
        # End
            break        

menu()
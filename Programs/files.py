import os

def no_of_files():
    '''This function determines how many .csv files exist within the current folder'''
    
    current_directory = os.getcwd()# Get the current working directory
    
    all_files = os.listdir(current_directory) # List all files in the current directory
    
    csv_files = []  # Initialize an empty list to store CSV files
    
    for file in all_files: # Iterate over all files
        
        if file.endswith('.csv'):# Check if the file ends with .csv
            file = file.replace('.csv', '')
            csv_files.append(file)  # Add the file to the csv_files list
    
    if csv_files == []:
        print("There are no current task lists")
        return False
    else:
        print('The current tasks are:')
        for csv in csv_files:
            print(csv)
    return True      

import os
from files import no_of_files #Import the no_of_files function
def delete_list():
    '''This function allows the user to delete an entire task list'''
    if not no_of_files():
        return
    delfile = input("Please enter the name of the CSV file to delete: ") #Asks the user for the file they want to delete
    delfile = f'{delfile}.csv'
    if os.path.exists(delfile): # Check if the file exists
        if delfile.endswith('.csv'): # Confirm the file is a CSV
            os.remove(delfile)# Delete the file
            print(f"The file '{delfile}' has been deleted.")
        else:
            print(f"The file '{delfile}' is not a CSV file.")
    else:
        print(f"The file '{delfile}' does not exist.")

import csv
import os
from files import no_of_files

def view_list():
    '''This function allows the user to view the contents of a certain task
    list, given that task list exists'''
    if not no_of_files():
         return
    while True:
        filename = input('What task list would you like to view')
        filename = f'{filename}.csv'
        if os.path.exists(filename):
            break  # Exit the loop if the file exists
        else:
            print(f"The file '{filename}' does not exist. Please try again.")
    tasklist = open(filename, 'r')
    fileread = csv.DictReader(tasklist)
    for task in fileread:
            for key, value in task.items():
                print(f"{key}: {value}", end=", ")
            print()

            
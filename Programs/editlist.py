import csv
import os
from files import no_of_files

def edit_list():
    '''This function allows the user to edit/update the elements of a task within a given list'''
    if not no_of_files():
        return
    filename = input('Which task list would you like to edit? ')
    filename = f'{filename}.csv'

    if not os.path.exists(filename): # Check if the file exists
        print(f"The file '{filename}' does not exist.")
        return
  
    with open(filename, 'r', newline='') as csvfile:   # Read the current contents of the CSV file
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        colnames = reader.fieldnames

    print("Current tasks in the list:")# Display the current contents to the user
    for i, row in enumerate(rows):
        print(f"Task {i+1}: {row}")

    while True:
        task_num = input(f"Enter the task number you want to edit (1-{len(rows)}) or 'Quit' to Quit: ")# Ask the user which task they want to edit
        if task_num.lower() == 'quit':
            break
        
        if not task_num.isdigit() or not (1 <= int(task_num) <= len(rows)):
            print("Invalid task number. Please try again.")
            continue
        
        task_num = int(task_num) - 1 

        selected_task = rows[task_num] # Display the selected task's details
        print(f"Selected task: {selected_task}")

        field = input(f"Which field do you want to edit? {colnames}: ") # Ask the user which field they want to edit
        if field not in colnames:
            print("Invalid field. Please try again.")
            continue
      
        new_value = input(f"Enter the new value for '{field}': ")  # Ask the user for the new value

        rows[task_num][field] = new_value  # Update the selected task

        print(f"Updated task: {rows[task_num]}")# Display the updated task

        another_edit = input("Would you like to edit another task? (yes/no): ").strip().lower() # Ask if the user wants to edit another task
        if another_edit != 'yes':
            break

    with open(filename, 'w', newline='') as csvfile: # Write the updated contents back to the CSV file
        writer = csv.DictWriter(csvfile, fieldnames=colnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"The file '{filename}' has been updated.")
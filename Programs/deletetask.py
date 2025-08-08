import csv
import os
from files import no_of_files #Import the no_of_files function

def delete_task():
    '''This function allows the user to delete a certain task within a 
    task list'''
    if not no_of_files():
        return
    filename = input('Which task list would you like to remove a task from? ') #Asks user for file they wish to delete a task from
    filename = f'{filename}.csv'

    if not os.path.exists(filename):
        print(f"The file '{filename}' does not exist.")  # Check if the file exists
        return

    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)  # Read the current contents of the CSV file
        tasks = list(reader)

    print("Current tasks in the list:")
    for i, task in enumerate(tasks, start=1):  # Display the current tasks to the user
        print(f"{i}. {task}")

    while True:
        try:
            task_index = int(input(f"Enter the index of the task you want to remove (1-{len(tasks)}) or 'Quit' to Quit: ")) # Ask the user which task they want to remove
            if task_index.lower() == 'quit':
                print("Operation canceled.")
                return
            if not 1 <= task_index <= len(tasks):
                raise ValueError("Invalid task number.")
            break
        except ValueError as ve:
            print(ve)
    
    removed_task = tasks.pop(task_index - 1) # Remove the selected task from the list of tasks
    print(f"Task removed: {removed_task}")

    with open(filename, 'w', newline='') as csvfile:     # Write the updated list of tasks back to the CSV file
        writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

    print(f"The file '{filename}' has been updated.")

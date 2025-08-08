import csv

def make_list():
    '''This function is used to generate a completely new task list. When
    executed, the user is asked to name the list as well as add any tasks
    to it that they wish'''
    filename = input('What would you like to call this new list')
    filename = f'{filename}.csv'

    with open(filename, 'w', newline = '') as csvfile:
        colnames = ['Task name', 'Due Date', 'Priority (!, !!, !!!)', 'Category', 'Completed']
        writer = csv.DictWriter(csvfile, fieldnames=colnames)

        writer.writeheader()
        
        while True:
            # Ask the user to input task details
            task = {}
            print('Please enter the details of the task')
            for col in colnames:
                task[col] = input(f"{col}: ")
            
            writer.writerow(task) # Write the task to the CSV file

            add_another = input("Would you like to add another task to this list? (Yes/No): ").strip().lower()
            if add_another != 'yes':
                break
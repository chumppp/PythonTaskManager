import time
from file_functions import *

def main():
    '''This is the main function that must be run to use the task manager.
    It incorporates all other functions within it'''
    startup()
    while True:
        action = input("\nWhat would you like to do? ")#Prompts user for what they would like to do
        #Executes the appropriate function based on the users input
        if action.lower() == 'quit':
            print('Thank you for using this task manager')
            break
        elif action.lower() == 'help':
            for key, value in commands.items():
                print(f"{key}: {value}")
                time.sleep(1)
        elif action.lower() == 'make list':
            make_list()
        elif action.lower() == 'view list':
            view_list()
        elif action.lower() == 'edit list':
            edit_list()
        elif action.lower() == 'delete list':
            delete_list()
        elif action.lower() == 'delete task':
            delete_task()
        else:
            print('Please input a valid command')

main()
    

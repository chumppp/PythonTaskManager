import time
#Creates a dictionary with information about the commands the user can use
commands = {
        'Make list' : 'Makes a new file for tasks',
        'View list' : 'Allows you to view a current task list',
        'Edit list' : 'Edit an already existing task list',
        'Delete list' : 'Deletes an entire task list',
        'Delete task' : 'Deletes a task within a task list',
        'Help' : 'View the commands',
        'Quit' : 'Quit the program'
    }
def startup():
    '''This is the function which runs as soon as the main function is run. It introduces the
    program and informs the user on all the commands they can use within the task manager'''
    print('Thank you for using this task manager')
    time.sleep(1)
    print('Firstly, please make a password to keep your task lists secure')
    time.sleep(1)
    password1 = input('Please enter a password to secure your task lists:') #Asks user to create and confirm password
    password2 = input('Please confirm your password:')
    while password1 != password2:
        print('Please ensure the passwords match')
        password1 = input('Please enter a password to secure your task lists:')
        password2 = input('Please confirm your password:')
    time.sleep(1)
    print('Thank you')
    time.sleep(1)
    print('Here are the commands you can use in this task manager')
    time.sleep(1)
    for key, value in commands.items(): #Prints out the 'commands' dictionary for the user to refer to
        print(f"{key}: {value}")
        time.sleep(1)


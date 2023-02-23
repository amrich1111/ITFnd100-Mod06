# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Aimee Richardson 2/19/23,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        try:
            file = open(file_name, "r")
            for line in file:
                task, priority = line.split(",")
                row = {"Task": task.strip(), "Priority": priority.strip()}
                list_of_rows.append(row)
            file.close()
        except:
            pass
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want to add more data to:
        :return: (list) of dictionary rows
        """
        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        # TODO: Add Code Here!
        list_of_rows.append(row)

        return list_of_rows

    @staticmethod
    def count_number_of_tasks(task, list_of_rows):
        """ Counts number of occurrences of single task in ToDoList table

        :param task: (string) with name of task:
        :param list_of_rows: (list) with table of tasks and priorities:
        :return: (int) number of times task appears in table
        """
        # TODO: Add Code Here!
        # Loop over current to do list and count how many times a given task is in the list 
        task_count = 0
        for row in list_of_rows:
            if row["Task"].lower() == task.lower():
                task_count += 1
        return task_count

    @staticmethod
    def remove_data_from_list(task, task_count, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows, (bool) if task successfully removed
        """
        # TODO: Add Code Here!
        removed_bool = True
        if task_count > 1:  # If there are multiple tasks with the same Task name, execute function to ask user which task to delete
            IO.output_multiple_tasks_to_remove(list_of_rows)
            remove_choice = IO.input_index_to_remove()
            try:  # Try to remove inputted item from list, if index does not exist display message to user
                list_of_rows.pop(int(remove_choice) - 1)  # Using pop to remove item from list based on index
            except:
                removed_bool = False
        elif task_count == 1:  # If only 1 task has the inputted name, remove item
            task_index = ""
            for row in list_of_rows:
                if row["Task"].lower() == task.lower():
                    task_index = list_of_rows.index(row)
            list_of_rows.pop(task_index)
        else:  # If no task has the inputted name
            removed_bool = False
        return list_of_rows, removed_bool

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        # Open ToDoList.txt file and loop over current list data to add to file
        file_obj = open(file_name, 'w')
        for row in list_of_rows:
            file_obj.write(str(row["Task"]) + "," + str(row["Priority"] + "\n"))
        return list_of_rows


# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def output_multiple_tasks_to_remove(list_of_rows):
        """ If multiple tasks in list have same name, print them to the user

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        for row in list_of_rows:
            if row["Task"].lower() == task.lower():
                task_index=list_of_rows.index(row)
                print(str(task_index + 1) + ". " + row["Task"] + " | " + row["Priority"])
        print()  # Add an extra line for looks

    @staticmethod
    def output_was_task_removed(removed_bool):
        """  Outputs whether user inputted task was removed or if it was not found

        :return: (str) indicating whether task was removed
        """
        # TODO: Add Code Here!
        if removed_bool:
            return "Task removed!\n"
        else:
            return "Task Not Found!\n"

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        # TODO: Add Code Here!
        strTask = input("Task: ").strip().title()
        strPriority = input("Priority: ").strip().title()
        print()
        return strTask, strPriority


    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task name
        """
        # TODO: Add Code Here!
        choice_str = input("Enter the name of the task you would like to remove: ").strip()
        return choice_str

    @staticmethod
    def input_index_to_remove():
        """  Gets the number of the task to be removed from the list (if multiple tasks have same name)

        :return: (int) with task number
        """
        # TODO: Add Code Here!
        remove_choice = input("Multiple tasks found. Please enter the task number you would like to remove: ")
        return int(remove_choice)

# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name=file_name_str, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()    # Ask user which task to remove
        task_count = Processor.count_number_of_tasks(task=task, list_of_rows=table_lst)     # Count instances of task
        table_lst, removed_bool = Processor.remove_data_from_list(task=task, task_count=task_count, list_of_rows=table_lst)     # Unpacks list and boolean indicating if task was removed
        print(IO.output_was_task_removed(removed_bool))     # Print message to user if task was removed
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        table_lst = Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        print("Data Saved!\n")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop

# -------------------------------------------------#
# Title: Functions And Class
# Dev:   PKim
# Date:  May 6, 2019
# ChangeLog: (Who, When, What)
#   PKim, 5/6/19, Created file & completed code
# -------------------------------------------------#

# DATA # declare variables and constants

lstTable = []
todolist = None

# PROCESSING # perform tasks

class ListManager():
    '''This class contains methods to manage a To-Do list'''

    # Load data from a file
    @staticmethod
    def ReadData(todolist):
        global lstTable
        for row in todolist:
            dictRow = {}

            # Add row to a python dictionary; split key & definition by "," character, includes .strip() for "\n"
            (dictRow["Task"], dictRow["Priority"]) = row.strip().split(",")

            lstTable.append(dictRow)

        return lstTable

    # Display all To-Do items to user
    @staticmethod
    def DisplayList():
        global lstTable

        i = 1

        for row in lstTable:
            strRow = str(row).strip("{").strip("}").replace("'", "")
            print(str(i) + ": " + strRow)
            i += 1

    # Add a new item to the list/Table
    @staticmethod
    def AddItem(strTask, strPriority):
        global lstTable

        # Create new data row and append to table
        dictNewRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dictNewRow)

    # Remove a new item to the list/Table
    @staticmethod
    def RemoveItem(intRemove):
        global lstTable

        del lstTable[intRemove - 1]

    # Save tasks to the ToDo.txt
    @staticmethod
    def SaveFile():
        global lstTable
        # Open file with "w" for overwrite in case user removes 2 tasks already in file
        objFile = open("ToDo.txt", "w")
        for row in lstTable:
            strRow = str(row).strip("{").strip("}").replace("'", "").replace("Task: ", "").replace(" Priority: ", "")
            objFile.write(strRow + "\n")

# PRESENTATION (I/O) # get user input

# Call ReadData() to open file
todolist = open("ToDo.txt")
ListManager.ReadData(todolist)
for row in lstTable:
    strRow = str(row).strip("{").strip("}").replace("'", "")

# Display a menu of choices to the user
while True:

    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print() # adding a blank line

    # Call DisplayList() to display current list to user
    if strChoice.strip() == '1':
        print("The current content of the To-Do list is as follows: \n")
        print("---------------------------------")
        ListManager.DisplayList()
        print("---------------------------------")

    # Call AddItem() to add an additional item
    elif strChoice.strip() == '2':
        strTask = input("What is the task you need to do?: ")
        strPriority = input("What is the priority? (low, medium, high, critical): ")
        ListManager.AddItem(strTask, strPriority)
        print("You have added '", strTask, "' to your task list.")

    # Call RemoveItem() to remove an item from the list
    elif strChoice == '3':
        print("\nEnter which task number to remove: ")
        ListManager.DisplayList()
        intRemove = int(input("\nItem Number: "))
        ListManager.RemoveItem(intRemove)
        print("You have removed  task number", intRemove, " from the table.")

    # Call SaveFile() to save current data to ToDo.txt
    elif strChoice == '4':
        ListManager.SaveFile()
        print("Your data has been saved!")

    # Exit program by calling ExitProgram()
    elif strChoice == '5':
        break

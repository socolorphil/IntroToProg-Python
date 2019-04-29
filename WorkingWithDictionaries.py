# -------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   PKim
# Date:  April 28, 2019
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   PKim, 4/28/19, Added code to complete assignment 5
#   PKim, 4/29/19, Edited/completed code to complete assignment 5
# https://www.tutorialspoint.com/python/python_dictionary.htm
# -------------------------------------------------#

#dictRow = {}
''' For some reason, having the dictRow = {} here caused issues in appending to lstTable below '''
lstTable = []

# Step 1 - Load data from a file
# When the program starts, load each "row" of data
# in "ToDo.txt" into a python Dictionary.
# Add each dictionary "row" to a python list "table"

# Code template from https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary
with open("ToDo.txt") as file:
    for row in file:
       dictRow = {}

       # Add row to a python dictionary; split key & definition by "," character, includes .strip() for "\n"
       (dictRow["Task"], dictRow["Priority"]) = row.strip().split(",")

       '''
       # Started with this code but simplified to the above by replacing the values defined below:
       
       (task, priority) = row.strip().split(",")
       dictRow["Task"] = task
       dictRow["Priority"] = priority
       '''

       lstTable.append(dictRow)

print("The current content of the To-Do list is as follows: \n")
print("---------------------------------")
for row in lstTable:
    strRow = str(row).strip("{").strip("}").replace("'", "")
    print(strRow)
print("---------------------------------")

# Step 2 - Display a menu of choices to the user
while True:
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

    # Step 3 -Show the current items in the table
    if strChoice.strip() == '1':
        print("Your current task list is as follows: ")
        for row in lstTable:
            strRow = str(row).strip("{").strip("}").replace("'","")
            print(strRow)

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = input("What is the task you need to do?: ")
        strPriority = input("What is the priority? (low, medium, high, critical): ")

        # Create new data row and append to table
        dictNewRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dictNewRow)

        print("You have added '", strTask, "' to your task list.")

    # Step 5 - Remove an item from the list/Table
    elif strChoice == '3':

        i = 1

        for row in lstTable:
            strRow = str(row).strip("{").strip("}").replace("'","")
            print(str(i) + ":" + strRow)
            i += 1

        intRemove = int(input("\nEnter which task number to remove: "))

        del lstTable[intRemove-1]

        print("You have removed  task number", str(intRemove), " from the table.")

    # Step 6 - Save tasks to the ToDo.txt file
    elif strChoice == '4':
        # Open file with "w" for overwrite in case user removes 2 tasks already in file
        objFile = open("ToDo.txt", "w")
        for row in lstTable:
            strRow = str(row).strip("{").strip("}").replace("'","").replace("Task: ","").replace(" Priority: ","")
            objFile.write(strRow + "\n")

        print("Your data has been saved!")

    elif strChoice == '5':
        break  # and Exit the program
# -------------------------------------------------#
# Title: Pickling And Exception Handling
# Dev:   PKim
# Date:  May 13, 2019
# ChangeLog: (Who, When, What)
#   PKim, 5/13/19, Created file & completed code
# -------------------------------------------------#

import pickle # In order to use pickle methods, you must first import the pickle module

# DATA # declare variables and constants

FilePath = "pickling.dat" # File name for relative file path
dictData = {1:"X", 2:"Y", 3:"Z"} # A dictionary with example data

# PROCESSING # perform tasks

class PickleFunctions:
    """ This class contains methods to demonstrate pickling """

    @staticmethod
    def pickle_out(data, path):
        """ Writes binary data into a file from the example dictionary data"""

        objFile = open(path, "wb") # Open file using "wb" for "write binary" and assign to object
        pickle.dump(data, objFile) # Use pickle method to dump data into the file
        objFile.close() # Close file object

    @staticmethod
    def pickle_in(path):
        """ Reads binary data into the script and returns data to be displayed back to user """

        objFile = open(path, "rb") # Open file using "rb" for "read binary" and assign to object
        fullData = pickle.load(objFile) # Use pickle method to load data into variable, 'fullData'
        objFile.close() # Close file object
        return fullData # Return value in the method so that it can display back to user

# PRESENTATION (I/O) # get user input

try: # In error handling, script will attempt to successfully run the 'try' portion first

    PickleFunctions.pickle_out(dictData, FilePath) # Call .pickle_out() method

    print("The binary data file now contains the following: ")
    print(PickleFunctions.pickle_in(FilePath)) # Call .pickle_in() method and print returned value to user

except Exception as e:  # In the case of an error, the 'except' block is trigered
                        # and assigns the Exception error code to variable "e"
    print("Python reported the following error: " + str(e)) # Display what the specific error was to user
    print("Please check your work and try again.")
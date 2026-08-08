# 1. Devlop a python application that reads a log file.
# 2. extracts structured information using regular expressions (Regex).
#    and stores  the extracted data into a myswl database
# 3. the application should demonstrate the use of file handling, regular expression, exception, exception handling and logging


# 1 input : log file : app_log.txt

# user defined function(log file)

# Read log file using with open function (line by line)

# entire log data into buffer as a whole string 

# using readline function will reads data line by default this read line function converts entire file data into list of strings
# - where each line will be single element in the list.

# Read the list using for loop 

# Performing the validation/filter/check using regular expressions, using conditional statement, using methods

# mapping
# time --- Date time
# Mode -- Log_mode
# Message --> log_message 
# Each case capture the activity or transaction using condition statement, using methods


# Each phase we are going to use exception handling 

# intercat or connect to the MYSQL data base using 

# Establish the cusror

# execute the sql query : if exists just insert the data
# if not Creat the table and insert the required data using for loop


# Commit the data and close the connection 


# Output : Mysql Table with required data : Data, Log_mode and Lof_message



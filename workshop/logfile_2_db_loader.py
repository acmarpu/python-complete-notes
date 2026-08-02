# Requirement
"""Develop a Python application that reads a log file, 
extracts structured information using Regular Expressions (Regex), 
and stores the extracted data into a MySQL database. 
The application should demonstrate the use of file handling, 
regular expressions, exception handling, and logging.
"""

# Create a function to read the log file and extract the required data



#Input : Log file
#"C:\\Users\\VENKATESH BALAGIRI\\PMCH\\Python_Digital_Mastery_Adv\Workshop_1_adv\\application.log"
# User defined function( Log file)



# Read log file using with open function (line by line)

# Entire log data into buffer as a whole string


# Convert the entire log data into list using readlines() method




# for loop to read each line form the log_list



# Use regex to extract the required data from each line of the log file



# List of tuples to store the extracted data , Assumed the output list is defined

# handle the exceptions using try-except block and log the errors using logging module





# Create a function to connect to MySQL database and insert the extracted data into the database


# connect to MySQL database using pymysql.connector.connect() method




# Create a cursor object using connection.cursor() method


# Create a table SQL query : log_data_table



# Validate the table exists in the database, if not create the table using cursor.execute() method




# Insert the extracted data into the table using cursor.executemany() method


# handle the exceptions using try-except block and log the errors using logging module





























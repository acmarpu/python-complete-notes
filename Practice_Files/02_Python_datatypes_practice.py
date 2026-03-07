#------------------------------------------------------------
# Practic Question 1
#------------------------------------------------------------

# convert a list of servers IPs into a tuple amd explain why immutability is preferable

# input: list of servers IPs
from pickletools import string1


servers_list = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"]

# convert list to tuple
servers_tuple = tuple(servers_list)

# Expected output: Tuple of servers IPs: Tuple of servers IPs: ('192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4')
print("Tuple of servers IPs:", servers_tuple)

# explain why immutability is preferable
print("\nWhy immutability is preferable:")
print("- Tuples are immutable, so they cannot be changed after creation.")
print("- This prevents accidental modification of data.")
print("- Tuples are faster than lists for accessing elements.")
print("- They are useful for representing fixed collections of data like IP addresses.")

#------------------------------------------------------------
# Practic Question 2
#------------------------------------------------------------

# Convert CPU usage from string  "78.5" to float and compare with a threshold (e.g 80.0)

cpu_usage_str = "78.5"

# Expected Output: CPU usage as string: 78.5 <class 'str'>
print("\nCPU usage as string:", cpu_usage_str, type(cpu_usage_str))

# Convert string to float
cpu_usage_float = float(cpu_usage_str)
# Expected Output: CPU usage as float: 78.5 <class 'float'>
print("\nCPU usage as float:", cpu_usage_float, type(cpu_usage_float))


threshold = 80.0
# Compare CPU usage with threshold
is_above_threshold = cpu_usage_float > threshold

# Expected Output: Is CPU usage above threshold? False
print("\nIs CPU usage above threshold?", is_above_threshold)


#------------------------------------------------------------
# Practic Question 3
#------------------------------------------------------------

# Access the first 3 servers IPs from a lsit using slicing 

server_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]

# Access the first 3 servers IPs using slicing
first_three_ips = server_ips[:3]

# Expected Output: First 3 servers IPs: ['192.168.1.1', '192.168.1.2', '192.168.1.3']
print("\nFirst 3 servers IPs:", first_three_ips)
print("First 3 servers IPs:", type(first_three_ips))


#------------------------------------------------------------
# Practic Question 4
#------------------------------------------------------------

# From a log message string "ERROR: Pod crashed at 10:00, slice to get only "ERROR"

log_message = "2025-06-01 10:00:00 ERROR: Pod crashed"
# Slice the log message to get only "ERROR"
error_message = log_message[20:25]  # Extract substring from index 20 to 25 (inclusive)
print("\n sliced error message:", error_message)



#------------------------------------------------------------
# Practic Question 5
#------------------------------------------------------------
"""
Extract every alterante and reverse service name from a list of services.

    services = ["nginx", "redis", "mysql", "postgres", "mongodb", "kafka", "elasticsearch"]
"""

services = ["nginx", "redis", "mysql", "postgres", "mongodb", "kafka", "elasticsearch"]

alternate_reverse_services = services[::-2]

# Alternate and reverse service names: ['elasticsearch', 'mongodb', 'mysql', 'nginx']
print("\nAlternate and reverse service names:", alternate_reverse_services)

#------------------------------------------------------------
# Practic Question 6
#------------------------------------------------------------

# F string practice

Course_id = 1001
Course_name = "python"

print(f"my Course Id is {Course_id} and my course name is {Course_name}")


# Format method practice

print("my Course Id is {} and my course name is {}".format(Course_id, Course_name))



# % formatting practice

print("my Course Id is %d and my course name is %s" % (Course_id, Course_name))


#------------------------------------------------------------
# Practic Question 7
#------------------------------------------------------------

str1 = "python is very easy and Anyone can learn"

print("Upper case str1:", str1.upper())                  # Output:  Upper case str1: PYTHON IS VERY EASY AND ANYONE CAN LEARN

str2 = str1.upper()

print(str2)                                              # Output:  PYTHON IS VERY EASY AND ANYONE CAN LEARN.
print("Lower case str1:", str2.lower())                  # Output:  Lower case str1: python is very easy and anyone can learn
   
str3 = str1.title()
print("Title Method str1:", str3.title())               # Output: Title Method str1: Python Is Very Easy And Anyone Can Learn


str4 = str1.capitalize()
print("Capitalize Method str1:", str4.capitalize())     # Output: Capitalize Method str1: Python is very easy and anyone can learn



#------------------------------------------------------------
# Practic Question 8
#------------------------------------------------------------

str1 = "  Python   "                 # Original string with spaces
print("Removed the spaces:", str1.strip())      # Output: Removed the spaces: Python


string = "code4python"
print("Original string:", string)               # Output: Original string: code4python
print("String after split:", string.split())     # Output: String after split: ['code4python']   
print("string after max split:", string.split("4"))  # Output: string after max split: ['code', 'python']
print("string after max split:", string.split("4"))  # Output: string after max split: ['code', 'python']


# Join method practice
str1 = ["Python", "is", "awesome"]
print("Joined string:", " ".join(str1))  # Output: Joined string: Python is awesome
print("str1 after join method:", '|'.join(str1))  # Output: str1 after join method: Python|is|awesome
str2 = ''.join(reversed(str1))
print("Reversed and joined string:", str2)  # Output: Reversed and joined string: awesomeisPython
str3 = ','.join(str1)
print("Joined with comma:", str3)  # Output: Joined with comma: Python,is,awesome




str1 = "python is easy"
print("Starts with 'python':", str1.startswith("python"))                # Output: True
print("Starts with 'is':", str1.startswith("is"))                    # Output:False




s = "python"
print("find b in s value:", s.find("b"))         # Not found
print("find t in s value:", s.find("t"))         # Found at index 2


# Check if a file name with .log

file_name = ["error.log", "access.log", "config.txt", "data.csv", "config.yml"]

for file in file_name:
    if file.endswith(".log"):
        print(f"{file} ends with .log")
    else:
        print(f"{file} does not end with .log")


# Output:
# error.log ends with .log
# access.log ends with .log         
# config.txt does not end with .log
# data.csv does not end with .log
# config.yml does not end with .log

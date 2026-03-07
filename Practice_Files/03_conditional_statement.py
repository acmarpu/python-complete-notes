'''
# Conditional statements in python 
#------------------------------------------------------------
# Practic Question 1
#------------------------------------------------------------

number = 10
if number > 0:
    print(f"{number} is positive.")

elif number < 0:
    print(f"{number} is negative.")

else:
    print(f"{number} is zero.") 

print("#" * 80)

# if with list and tuple and string
# string
course = "Python for devops"
if "devops" in course:
    print("This course is about devops.")
else:
    print("This course is not about devops.")


#------------------------------------------------------------
# Practic Question 2
#------------------------------------------------------------

# list
course_list = ["Python", "Devops", "Cloud", "AI", "ML"]
if "AI" in course_list:
    print("This course is about AI.")

else:
    print("This course is not about AI.")

#------------------------------------------------------------
# Practic Question 3
#------------------------------------------------------------

# tuple
course_tuple = ("Python", "Devops", "Cloud", "AI", "ML")
if "Cloud" in course_tuple:
    print("This course is about Cloud.")
else:
    print("This course is not about Cloud.")    

print("#" * 80)

# Single line if statement

age = 18
if age >=18: print("You are eligible to vote.")

print("#" * 80)

# Single line if-else statement
age = 17
print("You are eligible to vote.") if age >= 18 else print("You are not eligible to vote.")
# if the condation is true execute the first statement otherwise execute the second statement

#------------------------------------------------------------
# Practic Question 4
#------------------------------------------------------------

i = int(input("Enter a number: "))
j = int(input("Enter another number: "))

if i > j:
    print(f"{i} is greater than {j}.")
else:
    print(f"{j} is greater than {i}.")

# expected output: 20 is greater than 10.

#------------------------------------------------------------
# Practic Question 5
#------------------------------------------------------------

username = "admin"
password = "securepasssword"

if username == "admin":
    if password == "securepasssword":
        print("Login successful.")
    
    else:
        print("Incorrect password.")


#------------------------------------------------------------
# Practic Question 6
#------------------------------------------------------------

# idetity operator

username = "admin"
password = "securepasssword"

if username is "admin":                 # this is identity operator
    if password is "securepasssword":   # this is identity operator
        print("Login successful.")
    
    else:
        print("Incorrect password.")

else:                                   # this condition check the username is not "admin"            
    print("Invalid username.")


#------------------------------------------------------------
# Practic Question 7
#------------------------------------------------------------

# conditional statement with dictionary

user_roles = {
    "alice": "admin",
    "bob": "editor",
    "charlie": "viewer"
}


username = "bob"
if username in user_roles:
    role = user_roles[username]
    if role == "admin":
        print(f"{username} has admin privileges.")
    
    elif role == "editor":
        print(f"{username} has editor privileges.")
    
    elif role == "viewer":
        print(f"{username} has viewer privileges.")
    
    else:
        print(f"{username} has an unknown role.")

#------------------------------------------------------------
# Practic Question 8
#------------------------------------------------------------


# Boolean logic with and, or and not

age = 25
membership = "premium"

if age >= 18 and membership == "premium":
    print("You have access to premium content.")

else:
    print("You do not have access to premium content.") 


#------------------------------------------------------------
# Practic Question 9
#------------------------------------------------------------
# WAP that takes a server's CPU usage  (0-100) as input 
# and prints status : 90-100=Critical, 80-89=High, 70-79=Warning, 60-69=Moderate
# below 60=Normal

# Input
CPU_usage = int(input("Enter CPU usage (0-100): ")) # Example CPU usage percentage

# Drive Factor
# multiple conditions 

# condition 1: 90-100=Critical
if CPU_usage >= 90 and CPU_usage <= 100:
    status = "Critical"

# condition 2: 80-89=High

elif CPU_usage >= 80 and CPU_usage < 89:
    status = "High"    

# condition 3: 70-79=Warning

elif CPU_usage >= 70 and CPU_usage < 79:
    status = "Warning"

# condition 4: 60-69=Moderate

elif CPU_usage >= 60 and CPU_usage < 69:
    status = "Moderate"

# condition 5: below 60=Normal

elif CPU_usage >= 60 and CPU_usage < 69:
    status = "Normal"

else:
    status = "All Good"
    
# CPU usage input message :  Enter CPU usage (0-100): 60
# expected output   CPU usage: 60% - status: Moderate

print(f"CPU usage: {CPU_usage}% - status: {status}")


#------------------------------------------------------------
# Practic Question 10
#------------------------------------------------------------

i = 3

if i % 2 == 0:
    print(i, "is even")
else:
    print(i, "is odd number")


#------------------------------------------------------------
# Practic Question 11
#------------------------------------------------------------
# WAP that takes the number running containers as input and prints whether it is odd or even

# input
number_containers = int(input("Enter the number of running containers:"))

# Driving Factor
# Check if the number of container is odd or even using module operator

# condition: even

if number_containers % 2 == 0:
    container_status = "even"

# condation: odd

else: 
    container_status = "odd"

#Output
# print container status message: even or odd

print(f"the number of running containers ({number_containers}) is {container_status}")




#------------------------------------------------------------
# Practic Question 12
#------------------------------------------------------------
# WAP that takes a deployment status code (200, 400, 500)
# whether deployment was successful, faild or needs investigation 

# input 
status_code = int(input("Enter deployment status code 200, 400, 500 :"))

# Driving factor

# multiple conditions
# condition 1: 200: successful
if status_code == 200:
    deployment_status = "successful"

# condition 2: 400: failed
elif status_code == 400:
    deployment_status = "failed"

# condition 3: 500: needs server error
elif status_code == 500:
    deployment_status = "server error"


# condition 4: other codes : need investigation
else:
    deployment_status = "unknown status"

# output
print(f"deployment status code {status_code} indicates that the deployment was {deployment_status}.")

'''

#------------------------------------------------------------
# Practic Question 13
#------------------------------------------------------------
# WAP that takes a file extension and prints "log file", "config file", or "other file"

# Input 
# file extension

file_extension = ".cfg"

# Driver factor 
# analyze file extension using multiple condition

# condition 1 : .log : log file
if file_extension.endswith(".log"):
    file_type = "log file"

# condition 2 : .cfg or .ini: config file
elif file_extension.endswith(".cfg") or file_extension.endswith(".ini"):
    file_type = "config file"

# condition 3 : extensions: other file
else:
    file_type = "other file"

# output
# print file type message based on extension 

print(f"file extension '{file_extension} is classified as: {file_type}")







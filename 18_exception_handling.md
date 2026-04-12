----------------------------------------------------------------------------------------------
### Exception Handling
----------------------------------------------------------------------------------------------
* Try-Except blocks
* Error Handling best practices 

| **Exception Type**   | **Description**                              | **Example (DevOps Context)**   | 
|----------------------|----------------------------------------------|--------------------------------|
| Try-Except Block     | Used to catch and handle exceptions without  |  try:                          |
|                      | crashing the program                         |  with open(*/etc/config yaml*) |
|                      |                                              |                                 |
| Using the Else Block | Runs only if no exception occurs in the try  |  try:                          |
|                      | block.                                       |  response = 200 # mock HTTP status|
|                      |                                              |  if responce ! = 200            |
|                      |                                              |  raise Exception("Deployment failed") |  
|                      |                                              |  except Exception as e          |
|                      |                                              |  print("Error", e)              |
|                      |                                              |  else                           |
|                      |                                              |  print("Deployment Successful") |
|                      |                                              |                                 |
| Using the Finally    | Always runs(whether exception occurs or not).|  try:                           |  
  Block |                | Useful for cleanup tasks                     |  f = open("deployment log", 'W') |
|                      |                                              |  f write("Deploymet started.")   |
|                      |                                              |  finally.                        |
|                      |                                              |  f.close() # ensure file is closed|   
|                      |                                              |  print("Log file closed")         |
|                      |                                              |                                 |
|Raising  Exception    | Used to raise a built-in or custom error when|  def check_disk_space(space)      |
|                      | a condition fails.                           |    if space < 20                  |
|                      |                                              |  raise Exception("Low disk space! |
|                      |                                              |  cleanup required.")              |
|                      |                                              |  check_disk_space(10)             |
|                      |                                              |                                 |
|Custom Exception      | Define user-defined exceptions for specific  |  class ServiceDownError(Exception)|
|                      | error handling                               |  pass                             |
|                      |                                              |  service_status = "DOWN"          |
|                      |                                              |  if service_status == 'DOWN'      |
|                      |                                              |     raise ServiceDownError("Nginc |
|                      |                                              |     service is not running")      |      

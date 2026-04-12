----------------------------------------------------------------------------------------------
### Exception Handling
----------------------------------------------------------------------------------------------
* Try-Except blocks
* Error Handling best practices 

| **Exception Type**   | **Description**                              | **Example (DevOps Context)**   | 
|----------------------|----------------------------------------------|--------------------------------|
| Try-Except Block     | Used to catch and handle exceptions without  |  try:                          |
|                      | crashing the program                         |  with open(*/etc/config yaml*) |
| Using the Else Block | Runs only if no exception occurs in the try  |  try:                          |
|                      | block.                                       |  response = 200 # mock HTTP status|
|                      |                                              |  if responce ! = 200            |
|                      |                                              |  raise Exception("Deployment failed") |  
|                      |                                              |  except Exception as e          |
|                      |                                              |  print("Error", e)              |
|                      |                                              |  else                           |
|                      |                                              |  print("Deployment Successful") |
| Using the Finally    |                                              |                                 |
| Block                | Always runs(whether exception occurs or not).|  try:                           |  
|                      | Useful for cleanup tasks                     |  f = open("deployment log", 'W') |
|                      |                                              |  f write("Deploymet started.")   |
|                      |                                              |  finally.                        |
|                      |                                              |  f.close() # ensure file is closed|   
|                      |                                              |  print("Log file closed")         |
|Raising  Exception    | Used to raise a built-in or custom error when|  def check_disk_space(space)      |
|                      | a condition fails.                           |    if space < 20                  |
|                      |                                              |  raise Exception("Low disk space! |
|                      |                                              |  cleanup required.")              |
|                      |                                              |  check_disk_space(10)             |
|Custom Exception      | Define user-defined exceptions for specific  |  class ServiceDownError(Exception)|
|                      | error handling                               |  pass                             |
|                      |                                              |  service_status = "DOWN"          |
|                      |                                              |  if service_status == 'DOWN'      |
|                      |                                              |     raise ServiceDownError("Nginc |
|                      |                                              |     service is not running")      |      




| **Exception Type**   | **Description**                              | **Example (DevOps Context)**                                                                 |
|----------------------|----------------------------------------------|---------------------------------------------------------------------------------------------|
| **Try-Except Block** | Used to catch and handle exceptions without crashing the program | ```python\ntry:\n    with open("/etc/config.yaml") as f:\n        config = f.read()\nexcept Exception as e:\n    print("Error:", e)\n``` |
| **Using the Else Block** | Runs only if no exception occurs in the try block | ```python\ntry:\n    response = 200  # mock HTTP status\n    if response != 200:\n        raise Exception("Deployment failed")\nexcept Exception as e:\n    print("Error:", e)\nelse:\n    print("Deployment Successful")\n``` |
| **Using the Finally Block** | Always runs (whether exception occurs or not). Useful for cleanup tasks | ```python\ntry:\n    f = open("deployment.log", 'w')\n    f.write("Deployment started.")\nfinally:\n    f.close()  # ensure file is closed\n    print("Log file closed")\n``` |
| **Raising Exception** | Used to raise a built-in or custom error when a condition fails | ```python\ndef check_disk_space(space):\n    if space < 20:\n        raise Exception("Low disk space! Cleanup required.")\n\ncheck_disk_space(10)\n``` |
| **Custom Exception** | Define user-defined exceptions for specific error handling | ```python\nclass ServiceDownError(Exception):\n    pass\n\nservice_status = "DOWN"\nif service_status == "DOWN":\n    raise ServiceDownError("Nginx service is not running")\n``` |
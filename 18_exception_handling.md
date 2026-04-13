----------------------------------------------------------------------------------------------
### Exception Handling
----------------------------------------------------------------------------------------------
* Try-Except blocks
* Error Handling best practices 

* program errors
- compile-time error :
- run time error

* Exception Handling & Finally Keyword

- SyntaxError:
```
   a = 10
   if(a < 20)
       print("yes")
   # Here Syntaxerror is :
```

- TypeError
```
   a = 10
   b = "10"
   print(a + b)
   # here error is string can not add with int
```
- NameError
```
  print(value)
  # Error: 'value' is not defined
```

- IndexError
```
   nums = [1, 2, 3]
   print(nums[5])
   # Error: List index out of range
```

- KeyError
```
   data = {"name": "Ashoka"}
   print(data["age"])
   # Error: Key 'age' not found in dictionary

```
- ValueError
```
  num = int("abc")
  # Error: Invalid literal for int()

```
- AttributeError
```
  x = 10
  x.append(5)
  # Error: 'int' object has no attribute 'append'
```
- IOError
```
   f = open("nonexistent.txt", "r")
   # Error: File not found
```
- ZeroDivisionError
```
   print(10 / 0)
   # Error: Division by zero
```
- ImportError
```
   import non_existing_module
   # Error: No module named 'non_existing_module'
```


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
|  Block               | seful for cleanup tasks                      |  f = open("deployment log", 'W') |
|                      |                                              |  f write("Deploymet started.")   |
|                      |                                              |  finally.                        |
|                      |                                              |  f.close() # ensure file is closed|   
|                      |                                              | print("Log file closed")         |
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


* Basic Exception Handling in Python
```
   try:
       a = "ashoka"
       b = 10
       print(a + c)
   except TypeError:
       print("Type Error")
   except NameError:
       print("Name Error")
   else:
        print("hai)

```
   l = [1,2,3,4]
   print ("Provide the index of element to be printed")
   i = int(input())
   print(l[i])
   
```


----------------------------------------------------------------------------------------------
### Functions in Python
----------------------------------------------------------------------------------------------
* A **function** is a block of reusable code that performs a **specific task**.
* Functions help in organizing code into **small, manageable parts**.
* A function **runs only when it is called**.
* Functions improve **code readability, reusability, and maintainability**.


#### 📌 Types of Functions

##### 1. Built-in (Predefined) Functions
   * `print()`
   * `input()`
   * `type()`
   * `id()`

##### 2. User-defined Functions
   * Functions created by the programmer using the `def` keyword.

##### 🧱 Function Structure
```
   def f1(parameters):            # Function header 
       '''docstring'''            # Description of the function         
       statement                  # logic statement what action need to be perform
       return statement           # return statement 

   # Note : f1 name: function name,  parameters: [optional] input values to the function

```

* Creating small function
```
   def f1():
     '''this is my first function''
     print("hello")
   
   # Function will not execute until it is called 

```

```
   def f1():
     '''this is my first function''
     print("hello")

   f1()       # Calling the function  #Output: hello

```

```
   def f1():
      for i in range(5):
         print("hello", end=" ")
   
   f1()

```
----------------------------------------------------------------------------------------------
#### global vs nonlocal
----------------------------------------------------------------------------------------------
if we define global scope value a = 50, again if we define same value a = 50, so is local value change?
 
```
   a =100                        # Global scope
   def samplefunction():
      a = 200                    # Local scope
   samplefunction()
   print(a)                      # Optput: 100

```

* if you want to chenage global value with in function then use global keyward
```
   a =100                        # Global scope
   def samplefunction():
      a = 200
      def samplefunction1():
         global a
         a = 300                    
      samplefunction1()
   samplefunction1()
   print(a)                      # Optput: 

```




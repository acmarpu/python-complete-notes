
----------------------------------------------------------------------------------------------
### 🔢 2. Numeric type   (immutable)
----------------------------------------------------------------------------------------------

* In Python, the numeric types refer to the data types that represent numbers, which include 
   * int(0,100) 
   * float(10.0)
   * bool(true or false)
   * Complex Numbers(1a)

```      
   a = 10
   print(a)                       # Output 10 
   print(type(a))                 # Output <class 'int'> 

```

```
   a = 1.4
   print(a)                        # Output  1.4 
   print(type(a))                  # Output  <class 'float'>

```     

* **Converts the integer 10 into a floating-point number → 10.0.**
```      
   a = 10
   print(a)                         # Output 10
   print(type(a))                   # Output  <class 'int'>
      

   b = float(a)
   print(b)                          # Output 10.0
   print(type(b))                    # Output <class 'float'>

```

**Enter runtime** - when you enter a value at runtime using input() function the default datatype is *string*
``` 
   a = input("enter num1:")
   print(type(a))                    # Output   <class 'str'>

   x = int(a)                        # here we converting str to int
   print(type(x))                    # Output   <class 'int'>

```

* **Taking inputs separately and then converting to int**
```   
   a = input("enter number1:")       # Enter number 10
   print(a)                          # Output 10
   print(type(a))                    # Output <class 'str'>

   x = int(a)                        # converting str to int
   print(x)                          # Output 10
   print(type(x))                    # Output   <class 'int'>

   b = input("enter number2:")       # Enter number 20
   print(b)                          # Output 20
   print(type(b))                    # <class 'str'>

   y = int(b)                        # converting str to int
   print(type(y))
      
   c = x+y 
   print(c)                           # Output   sun c is 30
   print(type(c))                     # Output  <class 'int'> 

   print("sum c is", c)               # Output sum c is 30         

```   

**Simplified Approach**
```
   a = int(input("enter num1:"))       # Enter number 10
   b = int(input("enter num2:"))       # Enter number 20
   c = a + b
   print(c)                             # Output 30

   print("sum is:", c)                  # Output: sum is 30
   print(type(c))                       # Output <class 'int'>
 
```

**Taking float inputs directly and adding them**
```   
   a = float(input("Enter num1:"))
   b = float(input("enter num2:")) 
   c = a + b
   print("sum is:", c)                  # Example Output: sum is 45.7

```


**bool = true or false**
```   
   a = 10
   b = 20
   c = a > b
   print(c)                             # Output  False
   print(type(c))                       # Output  <class 'bool'>

```

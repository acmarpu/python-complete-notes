
----------------------------------------------------------------------------------------------
### 🔢 2. Numeric type   (immutable)
----------------------------------------------------------------------------------------------

* In Python, the numeric types refer to the data types that represent numbers, which include 
   * int(0,100) 
   * float(10.0)
   * bool(true or false)
   * Complex Numbers(1a)

```      
   numaric = 10
   print("numaric value:", numaric)       #Output: numaric value: 10
   print("numaric type:", type(numaric))  #Output: numaric type: <class 'int'>

```

```
  my_float = 3.14 
  print("Float value:", my_float)        #Output: Float value: 3.14      
  print("Float type:", type(my_float))   #Output: Float type: <class 'float'>

```     

```      
  # Converting integer (numaric) to float

   numaric = 10
   print("numaric value:", numaric)      #Output: numaric value: 10   
   print("numaric type:", type(numaric)) #Output: numaric type: <class 'int'>

   my_float = float(numaric)            
   print("Float value:", my_float)        #Output: Float value: 10.0
   print("Float type:", type(my_float))   #Output: Float type: <class 'float'>

```

**Enter runtime** - when you enter a value at runtime using input() function the default datatype is *string*

``` 
   numaric = int(input("Enter a numaric value: "))    #Output: Enter a numaric value: 10
   print("numaric value:", numaric)                   #Output: numaric value: 10
   print("numaric type:", type(numaric))              #Output: numaric type: <class 'int'>

```


``` 

# Enter the runtime value as a string and convert it to numaric value


   a = input("Enter a numaric value: ")
   print("Input value:", a)
   print("Input type:", type(a))


   # Converting a string input value to x integer value
   x = int(a)
   print("Converted value:", x)
   print("Converted type:", type(x))

   b = input("Enter a float value: ")
   print("Input value:", b)
   print("Input type:", type(b))
   

   # converting b string input value to y numaric value
   y = int(b)
   print("Converted value:", y)
   print("Converted type:", type(y))
   

   # Adding x and y
   c = x + y
   print("Sum of x and y:", c)
   print("Type of sum:", type(c))        

```   


```
  # Simple approach to add two numaric values
   
   a = int(input("Enter first numaric value: "))
   b = int(input("Enter second numaric value: "))

   c = a + b
   print("Sum of a and b:", c)
   print("Type of sum:", type(c))
 
```


```  
   # Adding two float values

   a = float(input("Enter num1:"))
   b = float(input("enter num2:")) 
   c = a + b
   print("sum is:", c)                  # Example Output: sum is 45.7

```



```  
   #  bool = true or false
   a = 10
   b = 20
   c = a > b
   print(c)                             # Output  False
   print(type(c))                       # Output  <class 'bool'>

```


----------------------------------------------------------------------------------------------
✅ End of Numaric Data Types 
----------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------
### 🔀 Control Flow Statement
----------------------------------------------------------------------------------------------
* In Python, **control flow statements** are used to decide the order in which statements are executed in a program.  
* Control flow statements help maintain the flow of program execution.  
* Conditional statements in Python are used to execute certain blocks of code based on whether a condition is true or false. These statements allow your program to make decisions and change its behavior accordingly.  
* Control flow refers to the order in which individual statements, instructions, or function calls are executed or evaluated.  

* Conditional statements
```
      if 
      if else
      nested if
      elif
```

* iteretive statement
```   
      for
      whle

```

* transfer statements
```   
      break
      continue
      pass
```

      
----------------------------------------------------------------------------------------------
### 1.❓Conditional Statements
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
#### 🔀 if & if-else
----------------------------------------------------------------------------------------------
* Based on the condition. it decides whether the block of code will allows for execution or not.
* The `if` keyword is used to test specific conditions.  
  - If the condition evaluates to **True**, the control enters the `if` block.  
  - If the condition evaluates to **False**, the control skips the `if` block and continues with the rest of the code.  

* The `if-else` block is used when you want to execute one block of code if the condition is **True**, and a different block of code if the condition is **False**.  

* The `if` statement evaluates a condition:  
  - If the condition is **True**, the code block inside `if` is executed.  
  - If the condition is **False**, it will skip to the `else` block (if present

```

   if condation:
      statements
   else:
      statement

``` 

```

   i = 10
   if i == 100:
       print("this is correct")        # This won't be printed because i is not 100
   else:
       print("this is not correct")    # This will be printed because i is 10, not 100

``` 

**🐞 Debug Mode**
* Debug mode is used to trace how the control flow moves through your program step by step.
* You can set a breakpoint (🔴) in your code — this is a marker that tells the debugger to pause execution at that specific line.
* When the program pauses, you can inspect variables, check conditions, and understand logic flow.
* To start debugging:
* Set a breakpoint (🔴) on the line you want to stop.
* Select Debug option in your IDE (e.g., VS Code → Run > Start Debugging).
* Keyboard Shortcut:
* Fn + F8: Step out of the current function and return to the caller (i.e., go back one level in the call stack).

```

   i = int(input("Enter a number: "))   # Get user input as an integer
   if i % 2 == 0:                       # Check if the number is divisible by 2
       print(i, "is even")
   else:
       print(i, "is odd")

```

``` 

   i = int(input("Enter first number: "))     # 10
   j = int(input("Enter second number: "))    # 20
   if i > j:
       print(i, "is bigger")
   else:
       print(j, "is bigger")                  # 20 is bigge

```
----------------------------------------------------------------------------------------------
#### 🪜 Nested if
----------------------------------------------------------------------------------------------
* Nested `if` is used to test **multiple conditions**.  
* If the outer `if` condition is `True`, then the inner `if` condition(s) will be tested.  
* If any condition fails, Python skips that inner block.  
* In simple terms: **`if` inside another `if`** is called a **nested if statement**.

```
      i = int(input("enter first number:"))  # 10
      j = int(input("enter second number:")) # 20
      k = int(input("enter third number:"))  # 30

      if i > j and i > k:
          print(i,"is big")
      else:
           if j > k:
            print(j,"is big")
           else:
              print(k,"is big")               # Output 30 is big

```

```
      name   = input("enter the name:")             # ashoka       
      age    = int(input("enter the age number:"))  # Convert input to integer 19
      gender = input("enter the gender (m/f):")     # m      

      if age >= 18:
          if gender == "m":
            print("hello Mr.", name, "welcome")
          else:
             print("hello Mrs.", name, "welcome")
      else:
         print("you are not eligbile")              # Output hello Mr. ashoka welcome

```

```
      
      var = int(input("Enter the expression value:"))
      if var < 150:
          print("expression value is less than 150")

          if var < 200:
              print("expression value is less than 200")

              if var < 300:
                   print("expression value is less than 300")
      else:
           print("could not fine the Expression value")

```
----------------------------------------------------------------------------------------------
#### 🔂 elif
----------------------------------------------------------------------------------------------
* If one of the conditions is true, the remaining conditions will not be tested.  
* The `elif` statement allows you to check multiple conditions. As soon as one condition is true, its block of code executes, and the rest are skipped.


* Using nested if statements (first example) makes the code longer and harder to read.
```
     i = int(input("enter the number"))
     if i == 1:
         print("one")
     else:
         if i == 2:
             print("two")
         else:
             if i == 3:
                 print("three)
             else:
                 if i == 4:
                     print("four")
                 else:
                     print("inval if number")

```

* The elif ladder checks conditions one by one — once a condition is True, the rest are skipped.

```
     i = int(input("Enter a number: "))   # Define i before using it

     if i == 1:
        print("one")
     elif i == 2:
        print("two")
     elif i == 3:
        print("three)
     elif i == 4:
        print("four")
     else:
        print("invalif number")

```

```
     marks = int(input("Enter the Marks:"))
     if marks >= 95:
         print("Grade A")
     elif marks >= 90:
         print("Grade B")
     elif marks >= 85:
         print("Grade C")
     elif marks >= 80:
         print("Grade D")
     else:
      print("not achived")
``` 

```
      var = 100
      or
      var = int(input("Enter the Expression value:")) #we can enter the runtime value
      if var < 150:
           print("Expression value is less than 150")
      elif var < 200:
          print("Expression value is less than 200")
      elif var < 300:
          print("Expression value is less than 300")
      else:
          print("invalid expression value")

```

----------------------------------------------------------------------------------------------
### 2.🔁 Iterative Statements (Loops) / Repetitive Statements
----------------------------------------------------------------------------------------------
* Iterative statements (also known as **loops**) are used to execute a block of code repeatedly **as long as a specific condition is true**.
* Once the condition becomes false, the loop terminates, and the control moves to the next part of the program.
* Loops help in reducing code repetition and improving efficiency.

📘 **Common Loop Types in Python:**
1. `for` loop → used to iterate over a sequence (like list, tuple, string, range, etc.)
2. `while` loop → used to repeat a block of code as long as a condition is `True`
3. `Nested` loops → loop inside another loop

----------------------------------------------------------------------------------------------
#### for loop
----------------------------------------------------------------------------------------------
* A **for loop** is used to iterate through elements of a collection **in the order they appear**.  
* It is commonly used to loop over a **sequence** — such as a **list**, **tuple**, **set**, **dictionary**, **array**, or **string**.


📘 **Key Points**
* **`for`** → keyword used to create a loop  
* **`element`** → temporary variable that holds each item of the sequence during iteration  
* **`iterator` / `sequence`** → the collection or range you want to loop through  


```    
       for element in iterator :
                block of code
```

* Normally, to display all elements of a list, we might print them **one by one**:
```
       l = [10,20,30,40,50]
       print(l[0])
       print(l[1])
       print(l[2])
       print(l[3])
       print(l[4])

```

* Instead of printing each element manually, we can use a for loop to print them all easily:

```
       l = [10,20,30,40,50,60]   
       for i in l:
         print(i)
```

**Explanation:**
* i → a temporary variable that holds each element of the list on every iteration
* l → the list (iterator) we are looping through
* The loop automatically moves through all items one by one  

```
         
      [10,20,30,40,50,60]     # list    iterator

      for i in l:             # Loop
      print(i)                # Print each element 
         
```

```
      l = [10,20,30,40,50,60]   
      for i in l:
          print(i, end="")      # Output 10 20 30 40 50 60  
```

* Checking with string
```
      for i in "ashoka":
          print(i)
          #Output
                  a
                  s
                  h
                  o
                  k
                  a

```


*Checking with range*
```
      for i in range(5):
          print (i, end="")   #Output 01234
```

```
      for i in [10,"ashoka",23.4,True,None]:
          print(i,type(i))
```

```
      for i in range(1,10,2):
          print(i,end="")

```

```
      for i in range(1,11):
      print(i, end="")
      if i == 5
         break                 # Completley stop when i = 5
                               # Output 12345
```      

```
      for i in range(1,11):
      if i == 5
         break  
      print(i, end="")
                                # Completley stop when i = 5
                                # Output 1234

```     

```
      for i in range(1,11):
      if i == 5 
         continue
      print(i, end="")          # OutPut  1 2 3 4 6 7 8 9 10

```   

```
      t = int(input("enter the table number:"))
      for i in range(1,21):
      print(t,"X",i,"=", t*i)

```
----------------------------------------------------------------------------------------------
#### Nested for loop
----------------------------------------------------------------------------------------------
* A **nested `for` loop** means a loop inside another loop.
* For every **iteration of the outer loop**, the **inner loop** executes completely before the outer loop moves to its next iteration.

```
      for outer_variable in outer_sequence:
         # Outer loop statements
         for inner_variable in inner_sequence:
            # Inner loop statements
```

```

      for n in [1,2,3]
         print(n)
         for c in ['a', 'b']: 
             print(c)

         #Output
               1
               a
               b
               2
               a
               b
               3
               a
               b             

```


----------------------------------------------------------------------------------------------
#### while loop
---------------------------------------------------------------------------------------------- 
* The **`while` loop** is used to execute a block of statements **repeatedly** as long as the given condition is **True**.  
* Once the condition becomes **False**, the control jumps **out of the loop**.
 
* *infinite loop* = If the loop condition **never becomes False**, the loop will continue running forever — this is called an **infinite loop**.

```
      while condition:
         statement

```

```
      i = 1
      while i < 6:
          print(i)
          i += 1   # Remember to increment i, otherwise the loop will continue forever.

```

```
      i = 1
      while i <= 10:
          print(i)
          i = i + 1
```


----------------------------------------------------------------------------------------------
#### 3. transfer statement
----------------------------------------------------------------------------------------------
* Transfer statements are used to **change the normal flow of execution** inside loops.

* The `break` statement is used to **stop the loop** when a specific condition is met.
* Once the condition is true, the loop **terminates immediately**, and control moves out of the loop.


```
     for i in range(1, 10):
         print(i, end=" ")
         if i == 5:
            break
```
```
     for i in range(1, 10):
         if i == 5 or i == 8:
             continue
         print(i, end=" ")
```

```
     for i in range(1, 101):
         if i % 2 != 0:     # Skip odd numbers
              continue
         print(i, end=" ")
```

* The pass statement is a null operation — it does nothing.

```
      for i in range(1, 6):
          if i == 3:
             pass  # Placeholder for future code
          print(i)

```

----------------------------------------------------------------------------------------------
✅ End of Python Control Flow Statement
----------------------------------------------------------------------------------------------
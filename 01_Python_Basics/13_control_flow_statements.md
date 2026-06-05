----------------------------------------------------------------------------------------------
### 🔀 Control Flow Statements
----------------------------------------------------------------------------------------------
* In Python, **Control flow Statements** are used to decide the order in which statements are executed in a program.  
* Control flow statements help maintain the flow of program execution.  
* Conditional statements in Python are used to execute certain blocks of code based on whether a condition is true or false. These statements allow your program to make decisions and change its behavior accordingly.  
* Control flow refers to the order in which individual statements, instructions, or function calls are executed or evaluated.  
* Based on the condition. it decides whether the block of code will allows for execution or not.
* if the condition is true. the block of code is allowed for execution 

✅ All loops are control flow statements,
but ❌ not all control flow statements are loops.

* Conditional statements:
```
   if 
   if else
   nested if
   elif

```

* iteretive statement:
```   
   for
   whle

```

* transfer statements:
```   
   break
   continue
   pass

```
 



----------------------------------------------------------------------------------------------
### 3. Transfer Statement
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
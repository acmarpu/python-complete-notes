----------------------------------------------------------------------------------------------
### 🔀 Control Flow Statements
----------------------------------------------------------------------------------------------
* In Python, **Control flow Statements** are used to decide the order in which statements are executed in a program.  
* Control flow statements help maintain the flow of program execution.  
* Conditional statements in Python are used to execute certain blocks of code based on whether a condition is true or false. These statements allow your program to make decisions and change its behavior accordingly.  
* Control flow refers to the order in which individual statements, instructions, or function calls are executed or evaluated.  

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
### 2.🔁 Iterative Statements / Repetitive Statements  (Loops) 
----------------------------------------------------------------------------------------------
* Iterative statements (also known as **loops**) are used to execute a block of code repeatedly **as long as a specific condition is true**.
* Once the condition becomes false, the loop terminates, and the control moves to the next part of the program.
* Loops help in reducing code repetition and improving efficiency.

📘 **Common Loop Types in Python:**
1. `for` loop → used to iterate over a sequence (like list, tuple, string, range, etc.)
2. `while` loop → used to repeat a block of code as long as a condition is `True`
3. `Nested` loops → loop inside another loop


#### for loop

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

**Explanation:**
* i → a temporary variable that holds each element of the list on every iteration
* l → the list (iterator) we are looping through
* The loop automatically moves through all items one by one  

```

```
   l = [10,20,30,40,50,60]   
   for i in l:
       print(i, end=" ")      # Output 10 20 30 40 50 60  
```


*Checking with string*
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

    # Output 
    10 <class 'int'>
    ashoka <class 'str'>
    23.4 <class 'float'>
    True <class 'bool'>
    None <class 'NoneType'

```

```
   for i in range(1,10,2):
        print(i,end=" ")     #Output 1 3 5 7 9 

```

```
   for i in range(1,11):
       print(i, end="")
       if i == 5:
               break                 # Completley stop when i = 5
                                     # Output 1 2 3 4 5
```      

```
   for i in range(1,11):
    if i == 5:
       break                   # Completley stop when i = 5
    print(i, end="")           # Output 1 2 3 4
                     
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
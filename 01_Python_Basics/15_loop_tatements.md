
----------------------------------------------------------------------------------------------
### 2.🔁 Loops (Iterative Statements / Repetitive Statements) 
----------------------------------------------------------------------------------------------
* Iterative statements (also known as **loops**) are used to execute a block of code repeatedly **as long as a specific condition is true**.
* Once the condition becomes false, the loop terminates, and the control moves to the next part of the program.
* Loops help in reducing code repetition and improving efficiency.

📘 **Common Loop Types in Python:**
1. `for loop'      → used to iterate over a sequence (like list, tuple, string, range, etc.)
2. `while loop'    → used to repeat a block of code as long as a condition is 'True' (integers, float, numbers)
3. `Nested loops'  → loop inside another loop


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
    for variable in sequence :
            block of code
```
* **for** is the keyword used to indicate the start if a for loop
* **in** is another keyword used to separate the variable from the sequence it's iterating over.
* **sequence** is the collection of values you want to iterate over. the could be a list, tuple, string, or iterable object.
* **variable** is a name you choose to represent each value in the sequence as you iterate through it. this name can be anything you like, but it should be meaningful to your code 

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

* **range**
* range(start, stop, step)
  - generates the list:
* start(optional): the first number in the sequence.
  - if omitted, it defaults to 0.
* stop: The last number in the sequence, This number is not included in the swquence itself
* step(optional): The amount by which each number in the sequence increases. if omitted, if defaults to 1


* Checking with range*
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

* **Break & Continue**
* Break : Exit the current loop immediately
* Continue: Skip the current iteration

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
* Conditions can be based on **integers, floats, or other numeric values** (and even boolean expressions).  
* integer(0,100), float(10.0), bool(true or false)

 
* *infinite loop* = If the loop condition **never becomes False**, the loop will continue running forever — this is called an **infinite loop**.


* Always an expression → never just a statement.
   - Expressions can involve:
   - Comparisons (==, <, >=, etc.)
   - Logical operators (and, or, not)
   - Membership (in, not in)
   - Identity (is, is not)
   - Or even direct values (True, False, numbers, strings).

* whenever condition statement true execute statement1 and statement2
* if false then execute statement2

```
      while (expression):
         statement1

      statement2

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

```
# while loop example : multiplication table

# input from user
num = int(input("enter a number to print its multiplication table: "))

# initialize counter

i = 1
print(f"Multiplication Table of {num}:")

# while loop from 1 to 10
while i <= 10:
    product = num * i
    print(f"{num} X {i} = {product}")
    i += 1  # increment counter
    
```

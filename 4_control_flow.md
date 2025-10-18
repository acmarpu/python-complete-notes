# this document is inprogress 


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


#### for loop** 
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


```
       for variablename in sequence:
      statements
      for variablename in sequence:
         statements
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


* Checking with range
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


#### while//////
 
   use to execute the no of statements as long as the condition is true, 
   once the condition is false then the control will jump into out of the loop.
 
   *infinite* = no stop

    while condition:
       statement

   i = 1
    while i < 6:
      print(i)
      i += 1 # remember to increment i, or else the loop will continue forever.

   i = 1
    while i <= 10:
        print(i)
         i = i+1
----------------------------------------------------------------------------------------------
#### 3. transfer statement
----------------------------------------------------------------------------------------------

   *break* is used to stope the iteratiosn based on the condition
   *continue* is used to skip the current iteration and it will continue with the next iteration
   *pass*

   for i in range(1,10):
        print(i,end= " ")
        if i == 5:
            break
---------------------------------------------------------
*this will skip only 5 and 8*
   for i in range(1,10):
       if i == 5 or i == 8:
            continue
        print(i, end=" ")

   for i in range(1,101):
       if i%2 != 0: # if i%2 == 0:
            continue
        print(i,end= " ")

----------------------------------------------------------------------------------------------------------

*nested for loop* a for loop which is having one more loop within is is called nested for loop











1. write a program to find the sum of first n mumbers using for loop and while loop?
   # n = int(input("Enter number:"))
   # s = 0
   # for i in range(1,n+1):
   #     s += i
   # print("the sum of first",n,"numbers:",s)

   n is the input type
   s is the result storage


2. take a number form user input print that number table?
   # n = int(input("Enter the number:"))
   # for i in range(1,11):
   #     print(n,"X",i,"=",n*i)


------------------------------------

String :=

1. what is string
   string is group of charrecters or sequence of charrecters

2. diffrent ways to create a string
   '', "", ''' ''', immutable

3. string indexing and string slicing
   string always starts with 0 index 
   slicing its part of the string
   # 0 1 2 3 4 5 6 7 8 # positive index
   # h y d e r a b a d
   # -9-8-7-6-5-4-3-2-1 # negitive index

   # s = "hyderabad"
   # print(s)
   # print(s[3])
   # print(s[-3])
   # print(s[1:6]) # slicing is print the 1 to 5 words in hyderabad
   # print(s[-7:-1]) # negitive slicing

4. String concatenation and string multiplication
   concatenation is it just process of adding 2 or more string into single string (+)
   multiplication is if you want to display the string number of repeted times  (*)
   # s1 = "durga"
   # s2 = "soft"
   # print(s1+s2)
   # print(s1+" "+s2)
   # print(s1*3)
   # print((s1+" "+s2+" ")*3)

5. String split and max split
   split just divied the string based on the separator
   max split how many times
   # s1 = "python is very easy and it is opp and it is interpreted"
   # print(s1)
   # s2 = s1.split(" ")
   # print(s2)
   # s2 = s1.split(" ",3)
   # s2 = s1.split("is")
   # print(s2)

6. string capitalize
   is used to return a new string where as capital letter 
   # s1 = "python is very easy and it is opp and it is interpreted"
   # print(s1)
   # s2 = s1.capitalize()
   # print(s2)
   # print(s1.capitalize())

7. String Titel
   only starting capitalize word
   # s1 = "python is very easy and it is opp and it is interpreted"
   # print(s1)
   # s2 = s1.title()
   # print(s2)

8. String count 
   it is used to return the number of ocurrences of substring form given string
   # s1 = "python is very easy and it is opp and it is interpreted"
   # print(s1)
   # print(s1.count('is'))
   # s2 = s1.count("a")
   # print(s2)

9. string replace
  # s1 = "python is very easy and it is opp and it is interpreted"
  # print(s1.replace("easy","hard"))
  # s2 = s1.replace("easy", "hard")
  # print(s2)

10. upper and lower
   # s1 = "python is very easy and it is opp and it is interpreted"
   # print(s1.upper())
   # s2 = s1.upper()
   # print(s2.lower())

11. string swapcase (caps change to small)
   # s = "DuRgAsOfT"
   # print(s)
   # print(s.swapcase())

12. string reverse
13. string immutable
14. string sort
   # s = "python is very easy"
   # s1 = s.split()
   # print(s1)
   # s1.sort()
   # print(s1)
   # s1.sort(reverse=True)
   # print(s1)

print even index and odd index position characters
# s = "durgasoft"
# print("Even index position characters:",s[0::2])
# print("odd index position characters:",s[1::2])

   
15 join function for the string

   # s = "durgasoft"
   # s1 = ':'.join(s)
   # print(s1)
   # s2 = ''.join(reversed(s1))
   # print(s2)
   # print("".join(reversed("SAI")))

   # l = ["sai", "raj","ram"]
   # s = ','.join(l)
   # print(s)


16. strip() 
   - it return a copyof the string with both leading and trailing characters removed
      leading = left side of the character
      trailing = right side of the character
       
17. lstrip()
   - return a copy of the string with leading characters removed

18. rstrip()     
   - Return a copy of the string with trailing characters removed
   
   # s = "  durga  "
   # print(s.strip("  "))
   # print(s.rstrip("  "))
   # print(s.lstrip("  "))
   # s1 = (s.strip("  "))
   # print(s1)

19. len(): it return length of the string
    # print(len(s))

20. Find() used to find substring from given string returns -1 if there is no substring
    # print(s.find("b"))
   
21. Max() highest alphabetical character in a string
22. min() lowest alphabeticalcharacter in astring
23. index() index of substring
    # print(s.index("b"))

24. rindex() highest index of substring
    # print(s.rindex(b))

25. partition() splits the string at the first occurrence of the separator and return a tuple
    # s = "python is very easy and it is opp and it is interpreted is"
    # print(s.split(" "))
    # print(s.partition(s))

26. startswith() return true if a string starts with the given prefix otherwise returns false

27. endwith() return true if a string ends with the given suffix otherwise returns False

28. isdigit() returns "True" if all characters in the string are digits,
    otherwise, it returns "False"

29. isalpha() return "True" if all characters in the string are alphabets Otherwise, it returns "False"

30. isalnum() returns true if all the characters

 Ex reveresed words
 # s = "python is very easy"
 # s1 = s.split(" ")
 # print(s1)
 # for i in s1:
 #     print(i[::-1],end=" ")

--------------------------------------------------------------------------------------------------
List : is order collection of elements
      heterogeneous elements (diffrent types of data types)

1. what is list
2. nested list (one or more list)
  # l = [ 10,20,[30],40,1.0 ]
  # print(l[2])
  # print(type(l))
3. creating a list

4. access elements from a list
5. list slicing (perticulear part of the string)
   # l = [10,20,[30],40,1.0]
   # print(l)
   # l[1] =33 # 1 is index and 33 is element
   # print(l)
   # l.insert(1,33) # 1 is index and 33 is value
   # print(l)

6. changing or adding elements to list
   # l = [10,20,[30],40,1.0]
   # print(l)
   # l.append(33) # last of the list and one element to the list
   # print(l)
   # l.extend([34,"sai",56]) # multipile elements to the list
   # print(l)

7. append and extend methods in list
8. inser method in list
9. list concatenation and multiplication
   # l1 = ["sai","manoj","jaideep"]
   # l2 = ["att","ms","tcs"]
   # l3 = l1+l2
   # print(l3)
   # print(l1*2)
10. delete or remove elements form a list
11. remove(), pop(), clear(), del
   # l = [10,20,30,40,60]
   # print(l)
   # l.remove(20) # elements
   # print(l)
   # l.pop(2) # index
   # print(l)
   # l.clear()
   # print(l)
   # del l
   # print(l)

12. list sort

   # l = [2,10,4,8,6,7,8]
   # print(l)
   # l.sort()
   # print(l)
   # l.sort(reverse=True)
   # print(l)
b b   
13. list copy
   shallow copy is normal copy

   deep copy
   # l = [2,10,4,8,6,7,8]
   # print(l)
   # l1 = l.copy()
   # print(l1)
   # l.append(33)
   # l1.remove(10)
   # print(l1)
   # print(l)
   
14. list count
  # l = [2,10,4,8,6,7,8,5,5,5,5]
  # print(l.count(5))
  
15. list index

16. creating list from user input values

   # creating list from user input value
   # l = []
   # v1 = int(input("Enter a integer value:"))
   # v2 = float(input("Enter a float value:"))
   # v3 = input("enter a string value:")
   # l.append(v1)
   # l.append(v2)
   # l.append(v3)
   # print(l)

17. creating list using range function
   # l = []
   # n = int(input("Enter the length of list:"))
   # for i in range(n):
   #     x = int(input("enter the element:"))
   #     l.append(x)
   # print(l)


   # l = []
   # n = int(input("Enter the length of list:"))
   # for i in range(n):
   #     x = input("enter the element:")
   #     l.append(x)
   # print(l)

# Creating list using range function
   # print(list(range(2,10,2)))

13--------------------------------------------------------------------------------------------------

Tuple:

1. what is tuple : is order collection of elements same as list
2. creating tuple : ()
3. creating tuple with one element : with ,
4. accessing elements from tuple
5. tuple slicing
6. tuple immutable
7. tuple concatenation and multiplication
   adding one or more tuples in to single concatenation
8. deleting a tuple
9. tuple methods --- count and index
10. tuple membershiptest
11. len(),max(),min(),sum()
12. converting a string into tuple
13. converting a list into tuple
14. converting a tuple into string
15. tuple packing and unpacking

---------------------------------------
Set:

1. what is set : unorder collection of unic elements and ignore duplicate elements
2. creating set 
   # s = set()
   # print(s)
   # print(type(s))

   # s = {10,20,30,"sai",34.5}
   # print(s)
   # s.add(99)
   # print(s)
   
3. creating an empty set
4. how to change set (add and update)
5. remove elements from set(discard and remove), clear(), del
6. set operation -- union (|)
                    intersection (&)
                    difference(-)
                    symmetric difference(^)
   # its return unique values
   # a = {1,2,3,4,5}
   # b = {4,5,6,7,8}
   # print(a|b)
   # print(a.union(b))

   # intersection
   # print(a&b)
   # print(a.intersection(b))

   # difference
   # print(a-b)
   # print(a.difference(b))

   # symmetric difference
   # common values will not print
   # print(a^b)
   # print(a.symmetric_difference(b))

7. membership test
8. len
9. max and min
10. sum

---------------------------------------

Dictionary:
-----------

1. what is dictionary : is a collection of items, 
                        each item can be pair {key:value}
                        keys are immutable, values are mutable
                        keys must be unique, no duplicate key
                        value not unique, duplicate values also possible
                        key can be any type
2. creating dictonary
3. accessing value from dictionary
4. change or add values
5. delete or remove values
6. copy
7. items
8. keys
9. values
10. membership test
11. len
12. pop
13. popitem

   bytes: is used to represent byte numers just like an array the only allowed values for bytes is0 to256
          bytes is immutable, we cannot chang

# this document is inprogress 



*****************************************************************************************
# **Control Flow Statement**
*****************************************************************************************
* In Python, conditional statements are used to execute certain blocks of code based on whether a condition is true or false. These statements allow your program to make decisions and change its behavior accordingly.
* Python control flow. Control flow is the order in which individual statements, instructions, or function calls are executed or evaluated.
* Control FLow Statement are used to mantin flow of program execution
 
   Conditional statements
      if 
      if else
      nested if
      elif
   
   iteretive statement
      for
      whle
   
   transfer statements
      break
      continue
      pass

      
*****************************************************************************************
**1. Conditional statements**
*****************************************************************************************
    *if  
    *if else 
    *nested if 
    *elif 
    
      
**if & if else**
* *if* is key word test the specific condition
* if else --The if-else statement allows you to execute one block of code if the condition is true and another block of code if the condition is false
* The if statement evaluates a condition. If the condition is True, the code block within the if gets executed. If the condition is False, it will skip to the else block (if present).

* #Examples

      i = 10
      if i == 100:
         print("this is correct")  # This won't be printed because i is not 100
      else:
         print("this is not correct")  # This will be printed because i is 10, not 100

      i = 10
      if i == 100:
         pass   # nothing is there 
      else:
         print("this is not correct")  # This will be printed because i is 10, not 100
 
      i = int(input("Enter a number: "))  # Get user input as an integer
      if i % 2 == 0:  # Check if the number is divisible by 2
         print(i, "is even")
      else:
         print(i, "is odd")


      i = int(input("enter first number:"))
      j = int(input("enter second number:"))  
      if i > j:
          print(i,"is big")
      else
           print(j,"is big")  
-----------------------------------------------------------------
**nested if**
  * is test multipile conditions and one of the condition fail its jump into another if ) 
  * (if inside if) You can have if statements inside if statements, this is called nested if statements.

   #Examples
      i = int(input("enter first number:"))
      j = int(input("enter second number:"))
      k = int(input("enter third number:"))

      if i > j and i > k: #30 10 20
          print(i,"is big")
      else
           if j > k:
            print(j,"is big")
        else:
           print(k,"is big")
-----------------------------------------------------------------
   #Examples
      name = input("enter the name:")
      age = int(input("enter the age:"))
      gender = input("enter your geder (M/F):")

      if age>= 18:
      if gender == "M":
           print("Hello Mr.", name, "Welcome")
      else:
           print("Hello Mrs", name, "Welcome")

      else:
          print("You are not eligbile")

   #Examples
      var = 100
      or
      var = int(input("Enter the Expression value:")) #we can enter the runtime value 
      if var < 150:
          print("Expression value is less than 150")

          if var < 200:
              print("Expression value is less than 200")

              if var < 300:
                   print("Expression value is less than 300")
      else:
           print("could not fine the Expression value")
  
-----------------------------------------------------------------
**elif**
  * one of the confition is true other condition will not be test here

 
   #Examples
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

   #Examples
      i = int(input("enter the number:"))
      if i == 1:
          print("one")
      elif i == 2:
          print("two")
      elif i == 3:
          print("three")
      elif i == 4:
          print("four")
      else:
          print("invalid number")



==========================================================================================================================================
**2. Iterative statements** or **loop Statement** or **Repetitive Statements**
==========================================================================================================================================
2 key words 
   1. for loop
      a) for loop statement
         for loop is used to itetate the iterator or range
         iterators -  list, set, tuple, dict, arry, string etc
          
      b) for repetitive statement
         while loop is repetitive statement or loop statement
         it will repet the certine block of code
         
      c) for iterative statement

   2. While loop

**for loop** 
   * use to iterate the elements of collections what the order they appear
   * A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

   a) for loop statement
         for loop is used to itetate the iterator or range
         iterators -  list, set, tuple, dict, arry, string etc

    
    for element in iterator :
              block of code

   for - keyward  [to create for loop]       element - Temporary variable [ to store a value of iterator for every iteration]

    for variablename in sequence:
        statements
        for variablename in sequence:
            statements

  #Examples
      
      list = [10,20,30,40,50,60]
      for element in list:
         print(element)

         ![alt text](image.png)
         
   #Examples
      
      list = [10,20,30,40,50,60]
      for i in list:
         print(i)

   #Examples

      l = [10,20,30,40,50]
      print(l[0])
      print(l[1])
      print(l[3])
      print(l[4])

   #Examples
       for i in range(50)
           print (att)
----------------------------------------------------
Another Way:-
      
   i is the loop variable
   L list collections
   here one by one value assigned to "i" 

   #Examples
      l = [10,20,30,40,50]
      for i in l:
          print(i) # Line by Line
    
      for i in l:
          print(i, end= " ") #single line
    
      for i in [10,20,30,40,50]:
         print(i)
    
      for i in "att":
         print(i)
        
       for i in range(10):
            print(i,end= " ")

      for i in range(10):
      for i in range(1,10,2):
          print(i,end="")

   #Examples
      for i in range(1,11):
      if i == 5 or i == 8:
         continue
      print(i, end="")
   
   #Examples
      for i in range(1,11):
      if i == 5 or i == 8:
         break  # Completley stop 
      print(i, end="")
-------------------------------------------------------------------------
   #Examples
      t = int(input("enter the table number:"))
      for i in range(1,21):
      print(t,"X",i,"=", t*i)
--------------------------------------------------------------------------

 **while** 
   use to execute the no of statements as long as the condition is true, 
   once the condition is false then the control will jump into out of the loop.
 
   *infinite* = no stop

    while condition:
       statement

   i = 1
    while i < 6:
      print(i)
      i += 1 # remember to increment i, or else the loop will continue forever.
--------------------------------------------------------------------------
   i = 1
    while i <= 10:
        print(i)
         i = i+1
===========================================================================================================================================
**3. transfer statement**
===========================================================================================================================================

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

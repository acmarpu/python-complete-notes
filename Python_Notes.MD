
# **Python**

==========================================================================================
Python was designed and developed by Guido van Rossum in the year 1989, and the first version was released in the year 1991.


**1.** Python is a programming language used for app development

**2.** Python is a general-purpose programming language, high-level programming language [Human understanble], case-sensitive programming language

**3.** Python is simple and easy to learn, meaning it’s a straight forward language

**4.** Python is completely cross-platform or platform-independent
* &nbsp;Python is cross-platform, meaning you can write Python code on one operating system (e.g., Windows) and run it on another (e.g., macOS or Linux) without modifications, as long as Python is installed on that system.

**5.** Python is completely free and open-source

**6.** Python is an interpreted language 

**Compiler-based languages(e.g., C, C++, Java):** 
* &nbsp; The source code is compiled into machine code (binary) before execution.
* &nbsp; In this language, compilation errors prevent the code from compiling.

**Interpreter-based languages** (e.g., Python): 
* &nbsp; The code is executed line by line, with each line being translated into machine code and executed on the fly.
* &nbsp; In this languages, all the debugging occurs at run-time.


**7.** Python is a dynamically typed language, not a statically typed language

**Statically typed languages** (e.g., C, Java) require the programmer to specify the data type of variables at the time of declaration.
* &nbsp; **Ex:** int a = 100
* &nbsp; The data type (int) must be declared explicitly

**Dynamically typed languages** (e.g., Python)* allow the data type to be inferred based on the assigned value. You don't need to declare the type explicitly, making the code simpler and more flexible
* &nbsp;dynamically: no need to spcify any data type at the time of decleration 
* &nbsp;**Ex:** variable name = value 
* &nbsp;var = 100  # Here, 'var' is dynamically typed as an integer.

==========================================================================================
**Features of python:**
==========================================================================================

**Easy to Learn:** Python has a simple and easy-to-understand syntax, making it a great choice for beginners.

**Expressive Language:** Python code is readable and concise, allowing developers to write fewer lines of code for complex tasks.

**Interpreted Language:** Python code is executed line by line by an interpreter, which makes debugging easier.

**Free and Open Source:** Python is free to use, and its source code is available for modification and redistribution under the Python Software Foundation License.

**Cross-Platform/Platform Independent:** Python code can be run on any operating system without modification, making it highly portable.

**Object-Oriented Language:** Python supports object-oriented programming (OOP), which enables code reuse, modularity, and encapsulation for better security and maintainability.

**Huge Standard Libraries:** Python comes with a comprehensive standard library that provides many modules and functions for various tasks, such as file I/O, web development, data manipulation, etc.

**GUI Support:** Python supports graphical user interface (GUI) development with frameworks like Tkinter, PyQt, and Kivy.

**Portable:** Python programs can be easily migrated from one platform to another (e.g., from Windows to Linux or Mac) without changes.

**Extensible:** Python allows developers to integrate other languages like C/C++ for performance-critical parts, and it supports the use of external libraries and modules.


==========================================================================================
**Application Areas of Python:**
==========================================================================================

**Standalone or Desktop Applications**
* CUI (Command User Interface)
* GUI (Graphical User Interface)

**Web Applications**
* Frameworks like Django enable Python for web development.

**Network-Based Applications**
* Python is used for building networked applications and protocols.

**Data Analysis Applications**
* Python, with libraries like Pandas, NumPy, and Matplotlib, is widely used in data analysis.

**Business Applications**
* Python is used for building business applications, including ERP systems and CRM software.

**AWS (Amazon Web Services)**
* Python can be used with AWS SDK (Boto3) for cloud services automation.

**DevOps**
* Python is often employed in automation scripts, monitoring, and server management tasks in DevOps.

**MATLAB-like Applications**
* Python can be used for numerical computing, similar to MATLAB, with libraries like SciPy and SymPy.

**Artificial Intelligence (AI)**
* Python is widely used for AI and Machine Learning, with frameworks like TensorFlow, Keras, and PyTorch.

**Testing**
* Python is popular in software testing and automation with frameworks like unittest, pytest, and Selenium.

**Python File Extension:**
* The default extension for Python files is .py (e.g., test.py).


==========================================================================================
**Different Ways to Write and Execute Python Code:**
==========================================================================================

**Interactive Mode**
* You can run Python code interactively in the Python shell (REPL).

**Script Mode**
* You can write Python code in a file (e.g., test.py) and execute it via the command prompt:

**Using Python IDLE**
* Python's Integrated Development and Learning Environment (IDLE) is a simple environment to write and run Python code.

**Using PyCharm Editor**
* PyCharm is a popular Python IDE for professional developers.
* You can download PyCharm Community Edition here.
* download PyCharm Community Edition : https://www.jetbrains.com/pycharm/download/?section=windows


==========================================================================================

# Python fundamentals

==========================================================================================

**1. Comments** 
* &nbsp;Python are identified with a hash symbol(#), and extend to the end of the line# 
* &nbsp;short cut key is ctrl+/ : description about the code we can use # also

**2. Keywords or Reserved Words**
* &nbsp;There are fewer restrictions on their usage. For example, you will get a “SyntaxError” if you try assigning a keyword to a variable
* &nbsp;Python keywords are special reserved words that have specific meanings and purposes and can’t be used for anything but those specific purposes. 
* &nbsp;These keywords are always available—you’ll never have to import them into your code.
* &nbsp;Python keywords are different from Python’s built-in functions and types.
   
   * &nbsp;import keyword
   * &nbsp;print(keyword.kwlist)

* 'if' is keyword, we can not use as variable

**3. Identifiers**
* &nbsp;Any name is called identifiers (variable name or function name or any other name)
* &nbsp;Python Identifier is the name we give to identify a variable, function, class, module or other object. 
* &nbsp;That means whenever we want to give an entity a name, that's called identifier.
   
   * &nbsp;**a.** lowercase or uppercase
   * &nbsp;**b.** case-sensitive
   * &nbsp;**c.** allow digits(0-9)
   * &nbsp;**d.** should not start with digit. wrong : 9acmarpu9  crroct : acmarpu9
   * &nbsp;**e.** should not be two parts (if two parts use _) (emp id) (emp_id)
   * &nbsp;**f.** allow underscore (_)
   * &nbsp;**g.** if any identifier starts with underscore(_) then it is private
   * &nbsp;**h.** no keywords or reserved words can be used as identifier

**4. Variables**
* &nbsp;Variables as Containers: A variable is used to store data values. It holds information that can be used and manipulated throughout a program.
* &nbsp;Variables as Identifiers: A variable is also known as an identifier because it uniquely identifies the value or object it is storing. An identifier is simply a name given to a memory location where data is stored.
* &nbsp;Named Memory Location: In Python, when you assign a value to a variable, Python internally stores the value in a memory location, and the variable name points to that location. The name you assign to a variable acts as a reference to the data.
* &nbsp;No Need to Specify Data Type: Unlike many other programming languages, Python is dynamically typed, meaning you don't need to specify the type of data a variable will hold.

**5. Multiple Assignment**
* &nbsp;is process of assigning a single value to multiple variables
* &nbsp;is process of assigning a multiple values to multiple variables
   
      a =b =c =10
      print(a)
      print(b)
      print(c)
      print(type(a))

* &nbsp;Single line print

      a =b =c =10
      print(a,b,c, sep=",") # sep = separate with ,

* &nbsp; the process of assigning multiple values ot multiple variables

      a,b,c = 10,20,30
      print(a)
      print(b)
      print(c)
      print(a,b,c)
      print(a, end=",")
      print(b, end=",")
      print(c)


**6. Python Indentation**
* Python uses indentation (whitespace before a statement) to define the structure of the code, such as loops, conditionals, functions, and classes. Instead of using curly braces {} (like in many other languages such as C or Java), Python relies on consistent indentation to group statements within a block of code. 
* Indentation Rules:
   * 4 spaces: The Python style guide (PEP 8) recommends using 4 spaces for each level of indentation.
   * Consistency: You can technically use a different number of spaces (like 1 or 2), but mixing different indentation styles (e.g., 4 spaces and tabs) will cause errors.
   * Tab vs Space: Although spaces are preferred, you can use tabs. However, using spaces is the common practice. Python 3 will raise a TabError if you mix tabs and spaces within the same block.

      i = 10
      if i ==10:
    *indent by four spaces = 1 level*
         print("true")
      
      else:
    *indent by four spaces = 1 level*
         print("false")
   


===========================================================================================
# Data types in python
===========================================================================================
* Python Data Types are used to define the type of a variable.
* Data types define the type of value a variable holds, and they also determine what operations can be performed on that value.
* In Python, data types are used to represent different types of values (e.g., numbers, strings, etc.) that are stored in variables.
* Python Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. 

**Mutable:** Data types whose values can be changed after they are created.

**Immutable:** Data types whose values cannot be changed after they are created.


1. **None**(NoneType) -- a = 'none'
2. **Numeric type**(*int(Integers)*) -- float.bool,Complex Numbers(1a) -- holds numeric values
3. **string**(Text Type)      
4. **list**(Sequence Types)
5. **tuple**(Sequence Types)  -- holds collection of items
6. **range**(Sequence Types)  -- holds collection of items
7. **set**(Set Types)         --hold collection of unique items
8. **dist**(Mapping Type)     -- holds data in key-value pair form
9. **bytes**(Binary Types)
10. **bytearray**(Binary Types) 
11. **forzenset**(Set Types)



**1. none**
* nothing is there in the variable
      
      a = 'none'
      print('none')
      print(a)
      print(type(a))

**2.Numeric type**
* Numeric -- init(0,100),float(10.0),bool(true or false),Complex Numbers(1a)
      
      a = 10
      print(a)
      print(type(a))

      a = 10.9
      print(a)
      print(type(a))

* int to flot convert*
      
      a = 10
      print(a)
      print(type(a))


      b= float(a)
      print(b)
      print(type(b))




**Enter runtime** - when you enter a value at runtime using input() function the default datatype is *string*

* #Lab

      a = input("enter num1:")
      print(type(a))
      x = int(a)
      print(type(x))

* #Lab

      a = input("enter number1:")
      print(a)
      print(type(a))
      x = int(a)  #here we converting str to int
      print(x)
      print(type(x))
      b = input("enter number2:")
      print(b)
      print(type(b))
      y = int(b)  #here we converting str to int
      print(type(y))
      c = x+y
      print("sum c is", c)
    
**-------another way------**
* #Lab

      a = int(input("Enter num1:"))
      b = int(input("enter num2:"))
      c = a + b
      print("sum is:", c)

* #Lab

      a = float(input("Enter num1:"))
      b = float(input("enter num2:"))
      c = a + b
      print("sum is:", c)

* bool = true or false
      
      a = 10
      b = 20
      c = a > b
      print(c)

**Sequence Datatypes or data structure**

**3. String()**
   *In Python, strings are used for representing textual data.
   *A string is a sequence of characters enclosed in either single quotes ('') or double quotes (" "). 
   *The Python language provides various built-in methods and functionalities to work with strings efficiently
   *str is a group of characters or sequence of characters
   *string is immutable (can not change or modify directly)

   #We can not replace, we will use replace to change the value
   #Lab
      s = "hello att" 
      print(s)
      s1 = s.replace("hello", "hai") #replace to change the value
      print(s1)

      #print(dir(str))
   
**4. List[]**
   *List is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ]
   *Lists are used to store multiple items in a single variable.
   *list will allow the diffrent datatype elements
   *list will allow the duplicate elements
   *list is mutable, we can modify the list

   #Lab
      l = [10,20,30,3.4,"att",True]
      print(l)
      print(type(l))
      l.append(33) #append is adding
      print(l)

      l = [10,20,30,3.4,"att",True]
      print(l)
      print(type(l))
      l[1] = 33 #modifies the element at index 1
      print(l)
   #Output
      [10, 20, 30, 3.4, 'att', True]
      <class 'list'>
      [10, 33, 30, 3.4, 'att', True]

**5. Tuple()**
   *The tuple is another data type which is a sequence of data similar to a list. But it is immutable. That means data in a tuple is write-protected.
   *tuple is ordered collection of elements
   *tuple can be create using () or ()bracket or opetional
   *tuple will allow the diffrent datatype elements
   *tuple will allow the duplicate elements

   #Lab
      t = ("raj",)
      print(t)
      print(type(t))

**6. Set{}**
   *set is un-ordered collection of unique elements
   *set can be create by using {}
   *to create an empty set than we use set() function
   *set will allow the diffrent datatype elements
   *set is mutable, we can change the set

   #Lab
      s = set()
      print(s)
      print(type(s))
   
   #Lab
      a = {10,20,30,40,50,60}
      print(a)
      print(type(a))

**7. Dictionary dict {}**
   *dict is an ordered collection of items. It stores elements in key/value pairs.
   *each item can be a pair of key and value 
   *we can create by usinf {}
   *in dict keys are immutable, and must be unique
   *in dict values are mutable and no need to be unique
   *in dict keys and values can be of any type(key rule should satisfy)
   *structures that allow you to store key-value pairs. Dictionary can be created using the dict() constructor or curly braces' {}'. 
    Once you have created a dictionary, you can add, remove, or update elements using the methods dict.

   #Lab
      capital_city = {'TS': 'Hyd', 'AP':'AMV','TN':'CH'}
      print(capital_city)
      print(capital_city['TS'])
      print(capital_city['AP'])
   
   #Lab
      d = {1:'sai',2:'att'}
      print(d)
      print(type(d))
      d[2] = 'ramesh' # Changing the values 
      print(d)

   #Lab
      person = {}
      # Get user input for key-value pairs
      name = input("Enter person's name: ")
      age = int(input("Enter person's age: "))
      city = input("Enter person's city: ")

      # Add or removing the key-value pairs to the dictionary
      person['name'] = name
      person['age'] = age
      person['city'] = city

      print("Dictionary after adding runtime values:", person)
      print(type(person))

**8. range**
   * range is used to generate the range of values
   * by default the range starts from 0
   * range is immutable, we can not modify

   #Lab
      r = range(10)
      print(r)
      print(type(r))
      print(list(r))
      print(type(r))
   # 2 = starting value, 10 = stop valu,e 2 = steping 

**9. bytes**
   *the bytes data type represents sequences of bytes, which are immutable sequences of integers, each representing a byte value from 0 to 255

   #Lab
      b = bytes([65, 66, 67])  # ASCII values for 'A', 'B', 'C'
      print(b)  # Output: b'ABC'

**10. bytearray**
   *In Python, bytearray is a mutable sequence of integers in the range 0 <= x <= 255. It is similar to bytes, but unlike bytes, bytearray objects can be modified after creation.

   #Lab
      ba = bytearray([65, 66, 67])  # ASCII values for 'A', 'B', 'C'
      print(ba)  # Output: bytearray(b'ABC')

**11. frozenset**
   *frozenset is an immutable version of a set, which means once it is created, its elements cannot be changed or modified.

   #Lab
      frozen_set = frozenset([1, 2, 3, 4, 5])
      print(frozen_set)  # Output: frozenset({1, 2, 3, 4, 5})


DS      Create     mutable    immutable   ordered    duplicate
str    '' or ""      no          yes          yes      yes
list     []          yes         no           yes      yes
tuple    ()          no         yes           yes      yes
set      {}          yes         no           no       no
dict     {}        keys:no     keys:yes       yes     kesy:no
                   value:yes   values:no            value:yes
range range()      no            yes         yes     no


================================================================================================================
***Operators**:
================================================================================================================
* Operator is a symbol which is used to perform the required operations.
* Operators are used to perform operations on variables and values.

**1. Arithmetic**
   + -- add
   - -- sub
   * -- mul
   / -- div
   % -- mod
   // -- floor div
   ** -- power

   print(3+2)

**2. Relational**
  <  -- lessthan
  >  -- greaterthan
  <= -- lessthan or equlto
  >= -- greaterthan or equalto
  == -- equlto
  != -- not equalto

   print(3 > 4)
   False

**3. Assignment**
  =  -- assignment
  += -- add and assign
  -= -- sub and assign
  *= -- mul and assigan
  /= -- div and assigan
  %= -- mod and assigan
  //= -- floot div and assign
  **= -- power and assigan
      a = 5
      print(a)
      a += 2
      a = a+2
      a -= 2
      print(a)

**4. logical**
   * and, or , not
   * and: return True if both the conditions are true else false
   
   #Lab
      print (20 < 3 and 1 < 4)

   * or: return True if any one of the condition is True or both the conditions are true else False
   #Lab
      print (20 < 3 or 1< 4)

   
   * not: return True if the condition is False
        return False if the condition is True
   #Lab
      print(not(20 < 3))


**5. Membership**
   * These are used to check whether the value are present in the sequence or not
   * in : return True if the value is present in the sequence else False
   * not in : return True if the value is not present in the sequence else False

   #Lab
      l = [10,20,30]
      print(10 not in l)
      print(10 in l)
   #Lab
      print("x" in 'hyd')

**6. identity**
   * These are used to check whether the variables are having the same identity or not
   * is: return True if the variables are having same identity else False
   * is not: return True if the variable are not having same identity else False

   #Lab
      i = 10
      j = 20
      print(i is j)

      print(id(i))
      print(id(j))

   * id(): it is a built-in function
         it is used to find the memory address of the variable 
         it will return a unique interger

**7. Bitwise**
   Bitwise operators will work on only integers for bit by bit calcualtion

   bitwise AND(&)
   bitwise OR(|)
   bitwise XOR(^)
   bitwise NOT(~)
   bitwise left shift (<<)
   bitwise right shift (>>)
   

==========================================================================================================================================
**1. Control Flow Statement**
==========================================================================================================================================
  * Python control flow. Control flow is the order in which individual statements, instructions, or function calls are executed or evaluated.
  * Control FLow Statement are used to mantin flow of program execution
 
**1. Conditional statements**
    *if  
    *if else 
    *nested if 
    *elif 
    
      
**if & if else**
  * is key word test the specific condition
  *if else --The if-else statement allows you to execute one block of code if the condition is true and another block of code if the condition is false

   #Lab

      i = 10
      if i == 100:
          print("this is correct") #Python Indentation
      else:
          print("this is not correct") #Python Indentation
     
   #Lab

      i = int(input("enter a number:"))
      if i % 2 == 0:
           print(i,"is even")
      else:
           print(i,"is odd")
-----------------------------------------------------------------
**nested if**
  * is test multipile conditions and one of the condition fail its jump into another if ) 
  * (if inside if) You can have if statements inside if statements, this is called nested if statements.

   #Lab
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
   #Lab
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

   #Lab
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

 
   #Lab
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

   #Lab
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

  #Lab
      
      list = [10,20,30,40,50,60]
      for element in list:
         print(element)

         ![alt text](image.png)
         
   #Lab
      
      list = [10,20,30,40,50,60]
      for i in list:
         print(i)

   #Lab

      l = [10,20,30,40,50]
      print(l[0])
      print(l[1])
      print(l[3])
      print(l[4])

   #Lab
       for i in range(50)
           print (att)
----------------------------------------------------
Another Way:-
      
   i is the loop variable
   L list collections
   here one by one value assigned to "i" 

   #Lab
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

   #Lab
      for i in range(1,11):
      if i == 5 or i == 8:
         continue
      print(i, end="")
   
   #Lab
      for i in range(1,11):
      if i == 5 or i == 8:
         break  # Completley stop 
      print(i, end="")
-------------------------------------------------------------------------
   #Lab
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
          bytes is immutable, we cannot change






   
      

   



























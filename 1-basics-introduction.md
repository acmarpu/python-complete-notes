----------------------------------------------------------------------------------------------
👉 Python Basics
----------------------------------------------------------------------------------------------
Python was designed and developed by Guido van Rossum in the year 1989, and the first version was released in the year 1991.

**1.** Python is a programming language used for app development

**2.** Python is a general-purpose, high-level, Case-Sensitive and Easy to Learn Programming Language

  *a) General-Purpose:*
   * This means that Python is designed to be used for a wide variety of programming tasks, not just one specific domain.
   You can use Python for:
   * Web development
   * Data analysis
   * Machine learning
   * Automation
   * Scripting, and more.

  *b) High-level:*
   * Python is considered a high-level language because it is abstracted from the machine's hardware.(Python does not require you to deal with computer hardware directly (like CPU instructions or memory).)
   * This makes Python easier to read, write, and understand, compared to low-level languages (like Assembly or C), which are closer to machine code. 
   * In other words, Python lets you focus more on solving problems rather than managing memory or other low-level tasks.

  *c) Case-Sensitive:*
   * Python treats uppercase and lowercase characters as different.
   * For example, *Variable* and *variable* would be considered two different identifiers. 
   * This is important to remember when writing Python code, as the language will not automatically correct case mismatches.
 
  *d) Easy to Learn:*
   * Python has a simple and easy learn and easy-to-understand syntax, making it a great choice for beginners.
   * meaning it’s a straight forward language


**3.** Python is completely cross-platform or platform-independent
   * Python is cross-platform, meaning you can write Python code on one operating system (e.g., Windows) and run it on another (e.g., macOS or Linux) without modifications, as long as Python is installed on that system.

**4.** Python is completely free and open-source
**5.** Python is an interpreted language
  *a) Interpreter-based languages(e.g., Python):* 
   * The code is executed line by line, with each line being translated into machine code and executed on the fly.
   * In this languages, all the debugging occurs at run-time.which makes debugging easier.

  *b) Compiler-based languages(e.g., C, C++, Java):* 
   * The source code is compiled into machine code (binary) before execution.
   * In this language, compilation errors prevent the code from compiling.

**6.** Python is a dynamically typed language, not a statically typed language

  *a) Statically typed languages (e.g., C, Java)* require the programmer to specify the data type of variables at the time of 

```
      int a = 100
      The data type (int) must be declared explicitly

```

  *b) Dynamically typed languages (e.g., Python)* allow the data type to be inferred based on the assigned value. You don't need to declare the type explicitly, making the code simpler and more flexible
   * dynamically: no need to spcify any data type at the time of decleration 

* **Ex:** variable name = value 

 ```
      var = 100 # Here, 'var' is dynamically typed as an integer.
      print(var)
      print(type(var))

```

----------------------------------------------------------------------------------------------
### 🧩 1. Features of Python:
----------------------------------------------------------------------------------------------

**Expressive Language:** 
  * Python code is readable and concise, allowing developers to write fewer lines of code for complex tasks.

**Free and Open Source:** 
  * Python is free to use, and its source code is available for modification and redistribution under the Python Software Foundation License.

**Cross-Platform/Platform Independent:** 
  * Python code can be run on any operating system without modification, making it highly portable.

**Object-Oriented Language:** 
  * Python supports object-oriented programming (OOP), which enables code reuse, modularity, and encapsulation for better security and maintainability.

**Huge Standard Libraries:** 
  * Python comes with a comprehensive standard library that provides many modules and functions for various tasks, such as file I/O, web development, data manipulation, etc.

**GUI Support:** 
  * Python supports graphical user interface (GUI) development with frameworks like Tkinter, PyQt, and Kivy.

**Portable:** 
  * Python programs can be easily migrated from one platform to another (e.g., from Windows to Linux or Mac) without changes.

**Extensible:** 
  * Python allows developers to integrate other languages like C/C++ for performance-critical parts, and it supports the use of external libraries and modules.

----------------------------------------------------------------------------------------------
### ⚡ 2. Application Areas of Python:
----------------------------------------------------------------------------------------------

**Standalone or Desktop Applications**
  * CUI (Command User Interface) run directly on a user's computer
  * GUI (Graphical User Interface) interact with the user via text in the terminal or command line

**Web Applications**
  * Frameworks like Django and Flask enable Python for web development.

**Network-Based Applications**
  * Python is used for building networked applications and protocols.

**Data Analysis Applications**
  * Python, with libraries like Pandas, NumPy, and Matplotlib, is widely used in data analysis.These libraries allow you to work with large datasets, perform calculations, and generate charts.

**Business Applications**
  * Python is used for building business applications, including ERP (Enterprise Resource Planning) systems and CRM software.

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


----------------------------------------------------------------------------------------------
### 💻 3. Different Ways to Write and Execute Python Code:
----------------------------------------------------------------------------------------------

**Interactive Mode**
  * You can run Python code interactively in the Python shell (REPL(Read-Eval-Print Loop)).

**Script Mode**
  * You can write Python code in a file (e.g., test.py) and execute it via the command prompt:

**Using Python IDLE**
  * Python's Integrated Development and Learning Environment (IDLE(Integrated Development and Learning Environment)) is a simple environment to write and run Python code.

**Using PyCharm Editor**
  * PyCharm is a popular Python IDE for professional developers.
  * You can download PyCharm Community Edition here.
  * download PyCharm Community Edition : https://www.jetbrains.com/pycharm/download/?section=windows


----------------------------------------------------------------------------------------------
### 📜 4. Python Fundamentals
----------------------------------------------------------------------------------------------

**a. Comments** 
* &nbsp;Python are identified with a hash symbol(#), and extend to the end of the line# 
* &nbsp;short cut key is ctrl+/ : description about the code we can use # also

**b. Keywords or Reserved Words**
* &nbsp;There are fewer restrictions on their usage. For example, you will get a “SyntaxError” if you try assigning a keyword to a variable
* &nbsp;Python keywords are special reserved words that have specific meanings and purposes and can’t be used for anything but those specific purposes. 
* &nbsp;These keywords are always available—you’ll never have to import them into your code.
* &nbsp;Python keywords are different from Python’s built-in functions and types.

``` 
      import keyword
      print(keyword.kwlist)

```
* 'if' is keyword, we can not use as variable

**b. Identifiers**
* &nbsp;Any name is called identifiers (variable name or function name or any other name)
* &nbsp;Python Identifier is the name we give to identify a variable, function, class, module or other object. 
* &nbsp;That means whenever we want to give an entity a name, that's called identifier.
   
    _a)_ lowercase or uppercase.

    _b)_ case-sensitive.

    _c)_ allow digits(0-9).

    _d)_ should not start with digit. wrong : 9acmarpu9  crroct : acmarpu9.

    _e)_ should not be two parts (if two parts use _) (emp id) (emp_id).

    _f)_ allow underscore (_).

    _g)_ if any identifier starts with underscore(_) then it is private.
 
    _h)_ no keywords or reserved words can be used as identifier.

----------------------------------------------------------------------------------------------
### 📜 c. Variables
----------------------------------------------------------------------------------------------
*Statically Typed vs Dynamically Typed:*
   * In some languages (like Java, C, C++), variables are *statically typed*, meaning you must declare the data type before using it.
   * In Python, variables are *dynamically typed* — you don’t need to declare the type explicitly. Python infers the type automatically at runtime.

*Variables as Containers:*
   * Variables act like containers that store values. You can reuse and manipulate these values throughout the program.

*Variables as Identifiers:*
   * A variable is also called an *identifier* because it uniquely identifies the value or object stored in memory.

*Named Memory Location:* 
   * When you assign a value to a variable, Python stores that value in a memory location, and the variable name points to that location.  
  Example: `x = 10` → here `x` is the *name* (identifier) pointing to the value `10`.

*Dynamic Typing in Python:* 
   * Python doesn’t require specifying the data type during declaration. The type is decided automatically based on the assigned value.
  
```
      x = 10        # int
      x = "hello"   # str
      x = 3.14      # float
```

**d. Multiple Assignment**
  * is process of assigning a single value to multiple variables
  * is process of assigning a multiple values to multiple variables

```  
      a =b =c =10
      print(a)
      print(b)
      print(c)
      print(type(a))

```

* Single line print

```
      a =b =c =10                       # multiple variables assigned the same value
      print(a,b,c, sep=",")             # sep -> separates output with commas
      print(a,b,c, sep=",", end=".")    # end -> ends output with a period instead of newline
      print(type(a))                    # prints the type of variable 'a'

      
      # 10,10,10. <class 'int'>         # Output  
```

* the process of assigning multiple values ot multiple variables

```
      a,b,c = 10,20,30     # assigning multiple values to multiple variables
      print(a)             # prints value of a
      print(b)             # prints value of b
      print(c)             # prints value of c

      print(a,b,c)
      # 10 20 30           # Output   

      print(a, end=",")
      # 10,                # Output  

      print(b, end=",")
      # 20,                # Output  

      print(c)
      # 30,                # Output  

      # Each variable (a, b, c) is printed one after the other on the same line.
      # 10,20,30,          # Output  

```

**e. Indentation**
  * Python uses indentation (whitespace before a statement) to define the structure of the code — for example, in loops, conditionals, functions, and classes.
  * Unlike many other languages such as C, C++, or Java, which use curly braces {} to group statements, Python relies only on indentation.

*Indentation Rules:*
  * 4 spaces → According to PEP 8 (Python Enhancement Proposal 8), the recommended style is 4 spaces per indentation level.
  * Consistency → You may technically use other spacing (e.g., 2 spaces), but mixing spaces and tabs or using inconsistent indentation will cause errors.
  * Tabs vs Spaces → Spaces are preferred. While tabs can be used, Python 3 raises a TabError if you mix tabs and spaces in the same block.

```
# In Java

      i = 10
      if (i=10)
      {
      s.o.p("true"); # System.out.print
      }
      else
      {
      s.o.p("false");
      }
```

```
# In Python


      i = 10
      if i ==10:
          print("true") # *indent by four spaces = 1 level*

      else:
          print("false") # *indent by four spaces = 1 level*

```


----------------------------------------------------------------------------------------------
#### 🧱 1. Structured Programming
----------------------------------------------------------------------------------------------
* **Definition:**
* Structured programming is a logical, step-by-step programming style that emphasizes sequence, selection, and iteration.

✅ Key Idea: Divide a program into smaller logical blocks (functions) that control the flow of execution using loops and conditionals.
It improves readability and reduces the use of goto.


----------------------------------------------------------------------------------------------
#### ⚙️ 2. Function-Oriented Programming (FOP)
----------------------------------------------------------------------------------------------
* **Definition:**
In function-oriented programming, the program is divided into functions, and data is passed between functions.

✅ Key Idea:
* Functions are the main building blocks.
* Focuses on actions (functions) that operate on data.
* Data and functions are separate.

----------------------------------------------------------------------------------------------
#### 🧩 3. Object-Oriented Programming (OOP)
----------------------------------------------------------------------------------------------
* **Definition:**
* OOP organizes code around objects, which combine data (attributes) and functions (methods) into a single unit.
✅ Key Idea:
* Everything is treated as an object.
* Objects represent real-world entities.
* Focus on what to model rather than how to do it.



----------------------------------------------------------------------------------------------
✅ End of Python Basics
----------------------------------------------------------------------------------------------
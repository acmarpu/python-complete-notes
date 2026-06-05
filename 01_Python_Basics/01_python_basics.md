----------------------------------------------------------------------------------------------
👉 Python Basics
----------------------------------------------------------------------------------------------
Python was designed and developed by Guido van Rossum in the year 1989, and the first version was released in the year 1991.

* Python is a versatile programming language commonly used for application development across web, desktop, and mobile platforms. Although Python itself does not directly create physical infrastructure such as servers, networks, or cloud machines, it plays a crucial role in DevOps and cloud computing. Through libraries and tools like Ansible, SaltStack, boto3 (AWS), and Google Cloud SDK, Python enables engineers to automate, configure, and manage infrastructure efficiently using code

----------------------------------------------------------------------------------------------
### why Python for Automation
----------------------------------------------------------------------------------------------

**1.** Introduction to Python

* Python is a **General-purpose**, **High-level**, **Case-sensitive**, and **Easy-to-Learn** programming language.  
It is known for its **Simple** and **Readability**, making it highly **Beginner-friendly**.

  **a)** *General-Purpose Language*
    * Python is a general-purpose programming language, meaning it is designed to be used for a wide variety of tasks, not restricted to a single domain.

    * You can use Python for:

    * 🤖 AI and Data Automation — using pandas, numpy, openai, etc.
    * 📊 Data Analysis and Visualization — with matplotlib, seaborn, pandas
    * 🧩 Machine Learning & Deep Learning — with scikit-learn, tensorflow, pytorch
    * ☁️ Cloud and DevOps Automation — using boto3, azure, gcloud SDKs
    * ⚙️ Scripting & Process Automation — repetitive or scheduled tasks
    * 🖥️ OS and Network Automation — via os, subprocess, paramiko
    * 📑 Document Automation — Excel, Word, and PDF using openpyxl, python-docx, PyPDF2
    * 📁 File and Folder Operations — rename, move, delete, or backup files

  **b)** *High-level:*
   * Python is considered a high-level language because it is abstracted from the machine's hardware.(Python does not require you to deal with computer hardware directly (like CPU instructions or memory).)
   * This makes Python easier to read, write, and understand, compared to low-level languages (like Assembly or C), which are closer to machine code. 
   * In other words, Python lets you focus more on solving problems rather than managing memory or other low-level tasks.

  **c)** *Case-Sensitive:*
   * Python treats uppercase and lowercase characters as different.
   * For example, *Variable* and *variable* would be considered two different identifiers. 
   * This is important to remember when writing Python code, as the language will not automatically correct case mismatches.
 
  **d)** *Easy to Learn:*
   * Python has a simple and easy learn and easy-to-understand syntax, making it a great choice for beginners.
   * meaning it’s a straight forward language


**2.** Python is completely cross-platform or platform-independent
   * Python is cross-platform, meaning you can write Python code on one operating system (e.g., Windows) and run it on another (e.g., macOS or Linux) without modifications, as long as Python is installed on that system.

**3.** Python is completely free and open-source

**4.** Python is an **Interpreted** language.

  *a) Interpreter-based languages(e.g., Python):* 
   * The code is executed line by line, with each line being translated into machine code and executed on the fly.
   * In this languages, all the debugging occurs at run-time.which makes debugging easier.

  *b) Compiler-based languages(e.g., C, C++, Java):* 
   * The source code is compiled into machine code (binary) before execution.
   * In this language, compilation errors prevent the code from compiling.

**5.** Python is a dynamically typed language, not a statically typed language

  *a) Statically typed languages (e.g., C, Java)* require the programmer to specify the data type of variables at the time of 

 c or c++: 
```
    int a = 100
    The data type (int) must be declared explicitly

```
```
    int main() {
      printf("hello, python");
      return 0;
    }

```

  *b) Dynamically typed languages (e.g., Python)* allow the data type to be inferred based on the assigned value. You don't need to declare the type explicitly, making the code simpler and more flexible
   * dynamically: no need to spcify any data type at the time of decleration 

 ```

    print("hello, python", "very, simple")
    # you’re passing two separate arguments

    print("hello, python", "very, simple", sep=" | ")
    # By default, arguments are joined with a space ().


    # variable name = value
   
    var = 100             # Here, 'var' is dynamically typed as an integer.
    print(var)
    print(type(var))

```

----------------------------------------------------------------------------------------------
### 🧩 Features of Python:
----------------------------------------------------------------------------------------------

- **Expressive & Readable** → Concise syntax, beginner-friendly, easy to learn.  
- **Free & Open Source** → Available under the Python Software Foundation License.  
- **Cross-Platform & Portable** → Runs on Windows, Linux, macOS without modification.  
- **Object-Oriented & Extensible** → Supports OOP concepts and integration with C/C++.  
- **Rich Standard Library** → Built-in modules for file I/O, web, data, and more.  
- **GUI Support** → Frameworks like Tkinter, PyQt, and Kivy for desktop apps.

----------------------------------------------------------------------------------------------
### 💻 Different Ways to Write and Execute Python Code:
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

**Install Python extension VS Code**
  * Open VS Code → go to Extensions (left sidebar).
  * Search for Python and install the official extension


----------------------------------------------------------------------------------------------
### ⚡ Application Areas of Python:
----------------------------------------------------------------------------------------------

- **Desktop Apps (CUI/GUI)** → Command-line or graphical applications.  
- **Web Development** → Django, Flask.  
- **Networking & Cloud** → Protocols, AWS (Boto3), Azure, GCP automation.  
- **Data Science & Analysis** → Pandas, NumPy, Matplotlib.  
- **Business Apps** → ERP, CRM systems.  
- **DevOps & Automation** → Scripts for monitoring, server management.  
- **Scientific Computing** → SciPy, SymPy (MATLAB-like).  
- **AI/ML** → TensorFlow, Keras, PyTorch.  
- **Testing** → unittest, pytest, Selenium.  
- **File Extension** → Python files use `.py` (e.g., `test.py`).
- **Indexing**
  * Indexing means accessing individual elements from a sequence (like string, list, tuple) using their position number (index).
  * Indexing starts from 0 (zero-based indexing).
  * Negative indexing starts from the end (-1 is last element).
  * Works with strings, lists, tuples, etc.
  * Indexing gives only one element at a time.

```
    s = "python"
    print(s[0])      # Output: p
    print(s[5])      # Output: n
    print(s[-1])     # Output: n
    print(s[-2])     # Output: o

```

- **Slicing**
  * Slicing is used to extract a part (subsequence) from a sequence like a string, list, or tuple.
  * start → index where slice begins (inclusive)
  * stop → index where slice ends (exclusive)
  * step → optional, defines jump or direction (default = 1)

```
    s = "python"
    print(s[0:4])     # Output: pyth
    print(s[2:])      # Output: thon
    print(s[:3])      # Output: pyt
    print(s[::2])     # Output: pto
    print(s[::-1])    # Output: nohtyp (reverse string)

```


----------------------------------------------------------------------------------------------
#### 🧱 1. Structured Programming
----------------------------------------------------------------------------------------------
* **Definition:**
* Structured programming is a logical, step-by-step programming style that emphasizes sequence, selection, and iteration.

✅ Key Idea: 
* Divide a program into smaller logical blocks (functions) that control the flow of execution using loops and conditionals.
* It improves readability and reduces the use of goto.


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
----------------------------------------------------------------------------------------------
### 📜 Python Keywords
----------------------------------------------------------------------------------------------

**A. Comments** 
* Python are identified with a hash symbol(#), and extend to the end of the line# 
* short cut key is ctrl+/ : description about the code we can use # also

**B. Keywords or Reserved Words**
* There are fewer restrictions on their usage. For example, you will get a “SyntaxError” if you try assigning a keyword to a variable
* Python keywords are special reserved words that have specific meanings and purposes and can’t be used for anything but those specific purposes. 
* These keywords are always available—you’ll never have to import them into your code.
* Python keywords are different from Python’s built-in functions and types.

#list of python keyword module

``` 
   import keyword
   print(keyword.kwlist)   
   
   # Output

   ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

   'if' is keyword, we can not use as variable

   print(len(keyword.kwlist))
   # Output 35

```

    

----------------------------------------------------------------------------------------------
### 📜 Variables
----------------------------------------------------------------------------------------------
*Statically Typed vs Dynamically Typed:*
   * In some languages (like Java, C, C++), variables are *statically typed*, meaning you must declare the data type before using it.
   * In Python, variables are *dynamically typed* — you don’t need to declare the type explicitly. Python infers the type automatically at runtime.

*Variables as Containers:*
   * Variables act like containers that store values. You can reuse and manipulate these values throughout the program.

*Variables as Identifiers:*
   * A variable is also called an *identifier* because it uniquely identifies the value or object stored in memory.

**Identifiers**
* Any name is called identifiers (variable name or function name or any other name)
* Python Identifier is the name we give to identify a variable, function, class, module or other object. 
* That means whenever we want to give an entity a name, that's called identifier.
   
    _a)_ lowercase or uppercase.

    _b)_ case-sensitive.

    _c)_ allow digits(0-9).

    _d)_ should not start with digit. wrong : 9acmarpu9  crroct : acmarpu9.

    _e)_ should not be two parts (if two parts use _) (emp id) (emp_id).

    _f)_ allow underscore (_).

    _g)_ if any identifier starts with underscore(_) then it is private.
 
    _h)_ no keywords or reserved words can be used as identifier.

*Named Memory Location:* 
   * When you assign a value to a variable, Python stores that value in a memory location, and the variable name points to that location.  
  Example: `x = 10` → here `x` is the *name* (identifier) pointing to the value `10`.

```
   x = 10 
   x is the variable  
   = is the operator 
   10 nature of the datatype

```
*Dynamic Typing in Python:* 
   * Python doesn’t require specifying the data type during declaration. The type is decided automatically based on the assigned value.
  
```
   x = 10        # int
   x = "hello"   # str
   x = 3.14      # float

```

**Multiple Assignment**
  * is process of assigning a single value to multiple variables
  * is process of assigning a multiple values to multiple variables

```  
   a =b =c =10
   print(a)
   print(b)
   print(c)
   print(type(a))

```

```
    a1 = "Hello Python"
    a2 = "Simple & Readable"
    a3 = "****************"
 
    print(a1, a2, sep =a3)                  # Output Hello Python****************Simple & Readable
    print(a1, a3, a2, sep=" ")              # Output Hello Python **************** Simple & Readable
    print(a1, a2, sep =a3, end="!!!")       # Output Hello Python **************** Simple & Readable

```

* Single line print
```
   a =b =c =10                       # multiple variables assigned the same value
   print(a,b,c, sep=",")             # sep -> separates output with commas     # Output 10,10,10
   print(a,b,c, end=".")             # end -> commas at the end # Output 10 10 10,
   print(a,b,c, sep=",", end=".")    # end -> ends output with a period instead of newline
   print(type(a))                    # prints the type of variable 'a'

```

* the process of assigning multiple values ot multiple variables

```
   a,b,c = 10,20,30     # assigning multiple values to multiple variables
   print(a)             # prints value of a
   print(b)             # prints value of b
   print(c)             # prints value of c

   print(a,b,c)         # Output   10 20 30 
             

   print(a, end=",")    # Output  10

   print(b, end=",")    # Output  20

   print(c)             # Output  30

   # Each variable (a, b, c) is printed one after the other on the same line.
   # 10,20,30,          # Output  

```

**Indentation**
  * Python uses indentation (whitespace before a statement) to define the structure of the code — for example, in loops, conditionals, functions, and classes.
  * Unlike many other languages such as C, C++, or Java, which use curly braces {} to group statements, Python relies only on indentation.

*Indentation Rules:*
  * 4 spaces → According to PEP 8 (Python Enhancement Proposal 8), the recommended style is 4 spaces per indentation level.
  * Consistency → You may technically use other spacing (e.g., 2 spaces), but mixing spaces and tabs or using inconsistent indentation will cause errors.
  * Tabs vs Spaces → Spaces are preferred. While tabs can be used, Python 3 raises a TabError if you mix tabs and spaces in the same block.

#In Java
```
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

#In Python
```

    i = 10
    if i ==10:
        print("true") # *indent by four spaces = 1 level*

    else:
        print("false") # *indent by four spaces = 1 level*

```

----------------------------------------------------------------------------------------------
### 📜 Scope
----------------------------------------------------------------------------------------------
* Global and local
* Scope defines where a variable can be accessed in your program.

1. Global Scope
* Variables declared outside of functions.
* Accessible throughout the program.

```
    x = 10  # global variable

    def show():
        print(x)  # can access global variable

    show()
        print(x)  # works here too

```

2. Local Scope
* Variables declared inside a function.
* Accessible only within that function

```
    def demo():
        y = 5  # local variable
        print(y)

    demo()
    # print(y)  # ❌ Error: y not defined outside

```

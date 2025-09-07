
----------------------------------------------------------------------------------------------
### 👉 Data types in Python
----------------------------------------------------------------------------------------------

* Python Data Types are used to define the type of a variable.
* They represent the kind of value a variable holds (e.g., numbers, strings, etc.), and they determine what operations can be performed on that value.
* Python data types are the classification of data items. They represent the kind of value stored in a variable and determine the operations that can be performed on that value.

#### 🔹 Mutable vs Immutable Types

- **Mutable:** Data types whose values **can be changed** after creation.  
- **Immutable:** Data types whose values **cannot be changed** after creation.  


* 📘 **_Basic Data Types_**

| **Data Type**   | **Category**   | **Example**          | **Definition** |
|-----------------|----------------|----------------------|----------------|
| **None**        | NoneType       | `a = None`           | Represents the absence of a value or null. |
| **Numeric**     | int (Integer)  | `a = 10`             | Holds whole numbers (e.g., 0, 100, -5). |
|                 | float (Float)  | `a = 10.5`           | Numbers with decimal or fractional part. |
|                 | bool (Boolean) | `x = True`           | Represents truth values: `True` or `False`. |
|                 | complex        | `a = 2 + 3j`         | Numbers with real and imaginary parts. |


* **_Sequence & Collection Types_**
* Meaning: you can access elements using indexing, slicing, or keys.

| **Data Type** | **Category**      | **Example**                           | **Definition** |
|---------------|------------------|---------------------------------------|----------------|
| **str**       | Text Type         | `a = 'x'` or `"x"` or `"""Hello"""`   | Holds textual data (sequence of characters). **mutable** (can be changed). |
| **list**      | Sequence Type     | `a = [1, 2.5, "Hello", [1, 2, 3], True]` | Stores multiple items, **mutable** (can be changed). |
| **tuple**     | Sequence Type     | `a = (1, 2.5, "Hello")`               | Stores multiple items, **immutable** (cannot be changed). |
| **range**     | Sequence Type     | `for i in range(5): print(i)`         | Generates a sequence of numbers, often used in loops. |
| **set**       | Set Type          | `a = {1, 2, 3, 4, 5}`                 | Unordered collection of unique items (duplicates removed). |
| **frozenset** | Set Type          | `fs = frozenset([1, 2, 3])`           | Same as set, but **immutable**. |
| **dict**      | Mapping Type      | `a = {"key1": "value1", "key2": "value2"}` | Stores data in **key-value pairs**. |
| **bytes**     | Binary Type       | `b = b'Hello'`                        | Immutable sequence of bytes. |
| **bytearray** | Binary Type       | `ba = bytearray(b'Hello')`            | Mutable sequence of bytes. |



----------------------------------------------------------------------------------------------
### 📊 Data Types Comparison Table
----------------------------------------------------------------------------------------------


| **Data Type** | **create**  | **Mutable**       | **immutable**     | **Ordered** | **duplicate**     |
|---------------|-------------|-------------------|-------------------|-------------|-------------------|
| **str**       |'' or ""     |    No             |    Yes            |     Yes     |  Yes              |
| **list**      | []          |    Yes            |    No             |     Yes     |  Yes              |
| **tuple**     | ()          |    No             |    Yes            |     Yes     |  Yes              |
| **set**       | {}          |    Yes            |    No             |     No      |  No               |
| **dict**      | {}          | key:no values:yes |key:no values:yes  |     Yes     | key:no values:yes |
| **range**     | range()     |    No             |    Yes            |     Yes     |  No               |



----------------------------------------------------------------------------------------------
### 🔹 1. none
----------------------------------------------------------------------------------------------

* nothing is there in the variable

 ```     
      a = 'none'
      print('none')
      print(a)
      print(type(a))

      # none                 # Output 
      # <class 'str'>        # Output 
```

----------------------------------------------------------------------------------------------
### 🔢 2. Numeric type   immutable.
----------------------------------------------------------------------------------------------

* In Python, the numeric types refer to the data types that represent numbers, which include -- int(0,100), float(10.0), bool(true or false), Complex Numbers(1a)

```      
      a = 10
      print(a)
      print(type(a))
  
      # 10                    # Output 
      # <class 'int'>         # Output 

```

```
      a = 1.4
      print(a)
      print(type(a))

      # 10                     # Output 
      # <class 'float'>        # Output 
```     

* **Converts the integer 10 into a floating-point number → 10.0.**

```      
      a = 10
      print(a)
      print(type(a))

      # 10                      # Output 
      # <class 'int'>           # Output 

      

      b = float(a)
      print(b)
      print(type(b))

      # 10.0                     # Output 
      # <class 'int'>            # Output 

```

**Enter runtime** - when you enter a value at runtime using input() function the default datatype is *string*


``` 
      a = input("enter num1:")
      print(type(a))             # Output   <class 'str'>
      x = int(a)                 # here we converting str to int
      print(type(x))             # Output   <class 'int'>

```

```   
      # Taking inputs separately and then converting to int

      a = input("enter number1:")
      print(a)
      print(type(a))

      x = int(a)                 # converting str to int
      print(x)
      print(type(x))             # Output   <class 'int'>

      b = input("enter number2:")
      print(b)
      print(type(b))

      y = int(b)                # converting str to int
      print(type(y))
      
      c = x+y                   
      # print(type(c))          # Output   sun c is 30
      print("sum c is", c)      # Output  <class 'int'>

```   

**Simplified Approach**


```
      a = int(input("enter num1:"))  
      b = int(input("enter num2:"))
      c = a + b
      print("sum is:", c)        # Output: sum is 30

```

```   
      # Taking float inputs directly and adding them

      a = float(input("Enter num1:"))
      b = float(input("enter num2:")) 
      c = a + b
      print("sum is:", c)        # Example Output: sum is 45.7

```



```   
      # bool = true or false

      a = 10
      b = 20
      c = a > b
      print(c)                  # Output  False
      print(type(c))            # Output  <class 'bool'>

```


----------------------------------------------------------------------------------------------
### 🔡 3. String ("immutable","python")
----------------------------------------------------------------------------------------------

* In Python, strings are an essential data type used to represent textual data.
* Definition: A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' / """ """).
 - Example: 'hello', "python", """world"""
* String Methods: Python provides many built-in methods to manipulate strings.
 - Examples: .replace(), .split(), .lower(), .upper(), .strip(), etc.
* String Immutability: Strings are immutable, meaning once created, they cannot be modified.
 - Operations like concatenation or .replace() return a new string instead of changing the original one.


```  
* With single quotes (' ') → may need escape \'.

    
      s = 'hello ashoka''s'
      print(s)                 # Output: hello ashoka
      print(type(s))           # Output <class 'str'>

      s = 'hello ashoka\'s'
      print(s)                 # Output: hello ashoka's
      print(type(s))           # Output: <class 'str'>

```

* With double quotes (" ")

```
      s = "hello ashoka" 
      print(s)                 # Output: hello ashoka
      print(type(s))           # Output: <class 'str'>

```

```
      s = "Hello"
      print(s[0])              # Output: H (first character)
      print(s[-1])             # Output: o  (last character, negative index)
      print(s[0:5])            # Output: Hello (substring from index 0 to 4)

```

```
      # In Python, you can repeat strings using the multiplication (*) operator.

      s = "Hello"
      repeated = s * 3
      print(repeated)           # Output: HelloHelloHello

```

```
      s = "  Hello, World  "
      print(s.upper())           # Output: HELLO, WORLD
      t = s[7:]. upper()         # Output: WORLD

      print(s.lower())           # Output: hello, world
      
      print(s.strip())           # Output: Hello, World! used to remove any leading and trailing whitespace characters from a string

      print(s.replace("World", "Python"))            # Output:   Hello, Python!

      print(s.split())                               # Output: ['Hello,', 'World!']

      print(s.find("World"))                         # Output: 8 (index of the first occurrence of "World")

```

* Replacing 'hello' with 'hai' (note this does not change s, since strings are immutable)*

```      
      s.replace("hello", "hai")
      print(s)                                    # Output: hello ashoka (s is unchanged)
```


*The replace method returns a new string, we can assign the result to a variable*
*we can not reuse "s" value*


```

      print(s.replace("hello","hai")) 

```

*We can assign the modified string to a new variable*

```      
      s1 = s.replace("hello", "hai")
      print(s1)                                  # Output: hai ashoka

```

**To get a list of all available functions for string operations, you can use the dir() function:**
* This will return a list of all the methods and attributes associated with the string class.

```
      print(dir(str))
      __add_                                     #also called descriptors
```


```    
       * description    
      help(str)

```


----------------------------------------------------------------------------------------------
### 📋 4. List ["mutable"]
----------------------------------------------------------------------------------------------

* A **list** in Python is an **ordered, mutable collection** that can hold different data types:integers, floats, strings, and even other lists.  
* Lists are enclosed in **square brackets [ ]** and elements are separated by commas.
* Since lists are **mutable**, their elements can be changed after creation.


📌 **Key Features of Python Lists:**
  - **Ordered:** Items in a list have a defined order, and that order will not change unless modified.  
  - **Mutable:** Lists can be changed after creation — you can add, update, or remove elements.  
  - **Heterogeneous:** A single list can store elements of different data types (e.g., integers, strings, booleans, even other lists).  
  - **Duplicates Allowed:** Lists can contain duplicate values; the same element can appear multiple times.  


* Creating a list with various types of elements*

```      
      l = [10,20,30,3.4,"python",True]
      print(l)                           # Output: [10,20,30,3.4,"python",True]
      print(type(l))                     # Output: <class 'list'>

```

* Lists are mutable, which means we can change their elements. We can modify an element by accessing it using its index, or add elements using methods like append().

```      
      l = [10,20,30,3.4,"ashoka",True]
      l.append(33)                       # Adds 33 to the end of the list
      print(l)                           # Output: [10,20,30,3.4,"ashoka",True,33]

```

```
      *Modifying an element at a specific index*

      l[1] = 33                          # Changes the element at index 1 (20 → 33)
      print(l)                           # Output: [10, 33, 30, 3.4, "ashoka",True,33]

```

📌 **Key Methods for Working with Lists:**

* **append(value)** — Adds an element to the end of the list.
```
      l = [10,20,30,3.4,"ashoka",True]
      l.append(33)                       # Adds 33 to the end of the list
      
```

* **insert(index, value)** — Inserts an element at a specific index in the list.

```
      my_list = [10, 20, 30]
      my_list.insert(1, 15)              # Inserts 15 at index 1
      print(my_list)                     # Output: [10, 15, 20, 30]

```

* **remove(value)** — Removes the first occurrence of the specified value.

```
      my_list = [10, 20, 30, 40, 20]
      my_list.remove(20)                 # Removes the first occurrence of 20
      print(my_list)                     # Output: [10, 30, 40, 20]
      
```

* **pop(index)** — Removes the element at the specified index and returns it.

```
      my_list = [10, 20, 30, 40, 50]
      popped_item = my_list.pop(2)        # Removes the element at index 2 (30)
      print(my_list)                      # Output: [10, 20, 40, 50]
      print("Popped Item:", popped_item)  # Output: Popped Item: 30

      # That returned value is stored in the variable popped_item

```

* **extend(iterable)** — Extends the list by appending all elements from another iterable (e.g., another list).

```
      my_list = [1, 2, 3]                 # Original list
      other_list = ["python","java"]       # Another list to extend my_list with
      my_list.extend(other_list)          # Using extend() to add elements of other_list to my_list
      print(my_list)                      # Output: [1, 2, 3, 'python', 'java']

```

* **index(value)** — Returns the index of the first occurrence of the specified value.

```
      my_list = [10, 20, 30, 40, 50]
      index_of_30 = my_list.index(30)
      print(index_of_30)                  # Output: 2 (The index of 30 is 2)

```

* **sort()** — Sorts the list in ascending order. 

```
      my_list = [4, 1, 3, 9, 2]
      my_list.sort()
      print(my_list)  # Output: [1, 2, 3, 4, 9]
```

----------------------------------------------------------------------------------------------
### 📦 5. Tuple (immutable)
----------------------------------------------------------------------------------------------

* A **tuple** is a built-in data structure in Python, very similar to a list. However, unlike lists, **tuples are immutable** — their elements cannot be changed after creation.
   
📌 **Key Points:**
*  *Immutable:* Once a tuple is created, its elements cannot be modified, added, or removed.
*  *Ordered:* Like lists, tuples maintain the order of elements.
*  *Different Data Types:* A tuple can store elements of various data types (e.g., integers, strings, floats, etc.).
*  *Duplicates Allowed:* Tuples can have multiple occurrences of the same element.
*  *Parentheses:* Tuples are usually created using () (parentheses), though they are optional in some cases (e.g., creating a single element tuple requires a trailing comma).


* If you want to create a **tuple with only one element**, you must add a **trailing comma**.  
* Without the comma, Python will treat it as a normal value inside parentheses, not a tuple.
   
```   
      t = ("ashoka")
      print(t)                         # Output: ('ashoka')
      print(type(t))                   # Output: <class 'str'>


      t = ("ashoka",)
      print(t)                         # Output: ('ashoka',)
      print(type(t))                   # Output: <class 'tuple'>

```


```
      t = ("ashoka",12,23.4,10)
      print(t)                         # Output: ('ashoka', 12, 23.4, 10)
      print(type(t))                   # Output: <class 'tuple'>
      t[1] = 33                        # ❌ Trying to change index 1 (value 12 to 33)
      print(t)                         # Output ('ashoka', 12, 23.4, 10)  elements cannot be modified

```

```
      nested_tuple = (1, 2, (3, 4), 5)
      print(nested_tuple[2])

```


----------------------------------------------------------------------------------------------
### 🧾 6 . Set {Mutable}
----------------------------------------------------------------------------------------------

* A **set** is an **unordered** collection of **unique elements**. 
* Duplicate values are automatically removed when creating a set.

📌 *Key Points:*
   * *Unordered:* The elements in a set do not have any specific order. When you print a set, its elements may not appear in the order they were added.
   * *Unique Elements:* Sets automatically remove duplicate elements, so each element is stored only once.
   * *Mutable:* Sets are mutable, meaning you can add or remove elements after creation.
   * *Different Data Types:* A set can hold elements of different data types (e.g., integers, strings, etc.).

*Creating Sets:*
* To create a non-empty set, you can use curly braces {}.
* To create an empty set, you need to use the set() function because {} creates an empty dictionary, not a set.
   

```   
      # Example: Empty set  

      s = set()
      print(s)                        # Output: set()
      print(type(s))                  # Output: <class 'set'>

```   

```
      s = {10, 20, 30, 40, 50, 60}
      print(s)                       # Output: {50, 20, 40, 10, 60, 30}
      print(type(s))                 # Output: <class 'set'>

```

```
      s = {10, 10, 20, 30, 40, 50, 60, 60}
      print(s)                       # Output: {50, 20, 40, 10, 60, 30} # Sets remove duplicates automatically
      print(type(s))                 # Output: <class 'set'>

```

* Adding elements to a set:

```   
      s = {10, 20, 30, 40, 50, 60}   
      s.add(70)                      # Adds 70 to the set
      print(s)                       # Output: {50, 20, 70, 40, 10, 60, 30}


```
* Removing elements from a set:

```      
      s = {10, 20, 30, 40, 50, 60}
      s.remove(20)                   # Removes 20 from the set
      print(s)                       # Output: {10, 30, 40, 50, 60, 70}

```

* **Set operations** like **union**, **intersection**, and **difference** are commonly used.  
**Union:** Returns a new set with **all unique elements** from both sets.    

```

      s = {10, 20, 30, 40, 50}
      s1 = {50, 60, 70, 80}
      print(s.union(s1))              # Union: {10, 20, 30, 40, 50, 60, 70, 80}

```

* intersection of two sets returns a new set that contains only the elements that are common to both sets.

```

      s = {10, 20, 30, 40, 50}
      s1 = {50, 60, 70, 80}
      print(s.intersection(s1))  # Intersection: {50}

```

* Difference: Returns a new set with elements in the first set but not in the second.

```
      print(s.difference(s1))   # Output: {10, 20, 30, 40}

```


----------------------------------------------------------------------------------------------
### 🔑 7. Dictionary {Mutable}
----------------------------------------------------------------------------------------------
* A **dictionary** is an **unordered collection of key-value pairs**.  
* It stores elements in **pairs**, where each key is associated with a value. - Each key-value pair is called an **item**: `{key: value}` 

📌 **Key Points:**

   * **Ordered Collection:** As of Python 3.7+, dictionaries maintain the order of insertion, meaning the order in which you add key-value pairs is preserved.
   * **Keys are Immutable:** The keys must be of immutable types (e.g., strings, numbers, tuples). You cannot use mutable types (like lists) as keys.
   * **Unique Keys:** Dictionary keys must be unique. If you try to insert a duplicate key, it will update the existing key with the new value.
   * **Mutable Values:** Values can be of any data type, and they do not need to be unique.
   * **Creation:** You can create a dictionary using curly braces {} or by using the dict() constructor.
   * *Creating a Dictionary:*
   * **Empty dictionary:** Use {} or dict().
   * **Non-empty dictionary:** Use curly braces {} with key-value pairs separated by a colon (:).
   
```
   * Empty dictionary 
      d = dict()

      or

      d = {}
      print(d)                                           # Output: {}
      print(type(d))                                     # Output: <class 'dict'>
      
```

```
      capital_city = {'TS':'Hyd', 'KA':'BANG','TN':'CH'}
      print(capital_city)                                 # Output: {'TS': 'Hyd', 'AP': 'AMV', 'TN': 'CH'}
      print(capital_city['TS'])                           # Output: Hyd
      print(capital_city['AP'])                           # Output: AMV

```   
  
* Duplicate Keys:

```
   

      capital_city = {'TS':'Hyd', 'TS':'BANG','TN':'CH'}
      print(capital_city)                                # Output: {'TS': 'BANG', 'TN': 'CH'}

```

* Modifying Dictionary Values:
```


      capital_city = {'TS':'Hyd', 'TG':'HYD','TN':'CH'}
      capital_city['TS'] = 'Hyderabad'
      print(capital_city)                               # Output: {'TS': 'Hyderabad', 'TG': 'HYD', 'TN': 'CH'}

```

* Changing values in a dictionary

```
   

      d = {1:'sai',2:'ashoka'}
      print(d)                                         # Output: {1: 'sai', 2: 'ashoka'}
      print(type(d))                                   # Output: <class 'dict'>
      d[2] = 'ramesh'                                  # Changing the value for key 2 
      print(d)                                         # Output: {1: 'sai', 2: 'ramesh'}

```
* Adding key-value pairs to a Dictionary at Runtime
* Get user input for key-value pairs*

``` 
      # Create an empty dictionary
      person = {}

      # Take input from user
      name = input("Enter person's name:")
      age = int(input("Enter person's age:"))
      city = input("Enter person's city:")



  *Add key-value pairs to the dictionary*
      
      person['name'] = name
      person['age'] = age
      person['city'] = city

      print("Dictionary after adding runtime values:", person)  # Output:  {'name': 'ashoka', 'age': '35', 'city': 'hyd'}
      print(type(person))                                       # Output:  <class 'dict'>

```

```
     # Start with an empty dictionary
     student_scores = {}


     # Adding scores for students
     student_scores['ashoka'] = 85
     student_scores['sunil'] = 92
     student_scores['bhaskar'] = 78

     print("Student Scores Dictionary:", student_scores)
     print(type(student_scores))                             # Output: <class 'dict'>


     student_scores['Alice'] = 90  # Update Alice's score
     print(student_scores)                                    # Output: {'ashoka': 90, 'sunil': 92, 'bhaskar': 78}

``` 

----------------------------------------------------------------------------------------------
### ✨ 8. range (immutable)
----------------------------------------------------------------------------------------------
* The `range()` function in Python is used to generate a sequence of numbers.  
* It's typically used in **for loops** to iterate over a specific range of values.
   
📌 **Key Points:**
  - **Start, Stop, Step:**
  - **Start:** The number where the range begins (**inclusive**).
  - **Stop:** The number where the range ends (**exclusive**).
  - **Step:** The interval between each number in the range.
  - If `step` is not specified, it defaults to `1`.
  - If `start` is not specified, it defaults to `0`.

**Immutability:**
- `range()` objects are **immutable**, meaning you cannot modify the values once it’s created.

**Use Cases:**
- The range() function is often used in loops (like for loops) to repeat actions a certain number of times.


```
      r = range(10)
      print(r)                # Output: range(0, 10)
      print(type(r))          # Output: <class 'range'>
      print(list(r))          # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      print(type(r))          # Output: <class 'range'>

```

- range(10) generates a sequence starting from 0 up to (but not including) 10.
- You can convert it to a list or tuple to see the actual values.
- `range()` itself does **not store all values in memory**. It generates numbers on demand (lazy evaluation), which is why printing it directly shows `range(0, 10)` instead of the numbers


```    
      r = range(2, 10, 2)  # start=2, stop=10, step=2
      print(tuple(r))      # Output: (2, 4, 6, 8)
      print(type(r))       # Output: <class 'range'>

```

- `range(2, 10, 2)` starts from `2`, goes up to (but not including) `10`, and increments by `2` each time.  
- We can convert the range to a tuple to see the sequence of numbers: `(2, 4, 6, 8)`.


```     
      for i in range(5):
      print(i)

      # Output:
      # 0
      # 1
      # 2
      # 3
      # 4

```


----------------------------------------------------------------------------------------------
### 🔍 9. bytes  immutable 
----------------------------------------------------------------------------------------------
   *the bytes data type represents sequences of bytes, which are immutable sequences of integers, each representing a byte value from 0 to 255

📌 **Key Points:**
- Immutable → once created, cannot be changed.  
- Each element in a `bytes` object is an integer (0–255).  
- Often used when dealing with raw binary or encoded data.

-  Creating bytes from a list of integers (ASCII codes)

```
      b = bytes([65, 66, 67])           # ASCII values for 'A', 'B', 'C'
      print(b)                          # Output: b'ABC'
      print(type(b))                    # Output: <class 'bytes'>

      print(b[0])                       # Output: 65  (the ASCII code for 'A')

      # Iterating over bytes
      for byte in b:
          print(byte)

```

----------------------------------------------------------------------------------------------
### 🧮 10. bytearray**
----------------------------------------------------------------------------------------------

- The **`bytearray`** type is a **mutable sequence of integers** in the range `0–255`.  
- Similar to `bytes`, but unlike `bytes`, a `bytearray` object **can be modified after creation**.  


📌 **Key Points:**
 - Mutable → you can change elements after creation.  
 - Each element represents a single byte (0–255).  
 - Useful when you need a modifiable sequence of binary data.  

 ```
      # Creating a bytearray
      ba = bytearray([65, 66, 67])   # ASCII values for 'A', 'B', 'C'
      print(ba)                      # Output: bytearray(b'ABC')
      print(type(ba))                # Output: <class 'bytearray'>

      # Modifying elements
      ba[0] = 90                     # Change ASCII 65 ('A') to 90 ('Z')
      print(ba)                      # Output: bytearray(b'ZBC')

      # Appending a new byte
      ba.append(68)                  # ASCII for 'D'
      print(ba)                      # Output: bytearray(b'ZBCD')


      # bytearray(b'ABC')
      # <class 'bytearray'>
      # bytearray(b'ZBC')
      # bytearray(b'ZBCD')


```

----------------------------------------------------------------------------------------------
### ❄️ 11. frozenset**
----------------------------------------------------------------------------------------------
* **frozenset** is an **immutable** version of a set, which means once it is created, its elements **cannot be changed, added, or removed**.
* Like sets, frozensets:
  - Store **unique elements** only (no duplicates).
  - Support **set operations** (union, intersection, difference, etc.).
* Difference: Unlike `set`, a `frozenset` is **hashable**, so it can be used as a **key in a dictionar

```
      frozen_set = frozenset([1, 2, 3, 4, 5])
      print(frozen_set)   # Output: frozenset({1, 2, 3, 4, 5})

      # frozen_set.add(6) ❌ Error: 'frozenset' object has no attribute 'add'

      # But we can still perform set operations
      s = {3, 4, 5, 6}
      print(frozen_set.union(s))        # frozenset({1, 2, 3, 4, 5, 6})
      print(frozen_set.intersection(s)) # frozenset({3, 4, 5})

```

----------------------------------------------------------------------------------------------
✅ End of Python Data Types 

👉 Next Topic: [3_operators.md](./3_operators.md)
----------------------------------------------------------------------------------------------
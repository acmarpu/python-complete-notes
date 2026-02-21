
----------------------------------------------------------------------------------------------
### 👉 Data types in Python
----------------------------------------------------------------------------------------------
* Python Data Types are used to define the type of a variable.
* They represent the kind of value a variable holds (e.g., numbers, strings, etc.).
* Data types determine the **operations** that can be performed on a value.
* Python is a **dynamically typed** language (no need to declare data types explicitly).

----------------------------------------------------------------------------------------------
### 🔹 Mutable vs Immutable Types
----------------------------------------------------------------------------------------------
- **Mutable:** Data types whose values **can be changed** after creation.  
- **Immutable:** Data types whose values **cannot be changed** after creation.  

----------------------------------------------------------------------------------------------
### 📘 **_Basic Data Types_**
----------------------------------------------------------------------------------------------

| **Data Type**   | **Category**   | **Example**     | **Definition** |
|-----------------|----------------|-----------------|----------------|
| **None**        | NoneType       |   a = None      | Represents the absence of a value or null. |


| **Data Type**   | **Category**   | **Example**     | **Definition** |
|-----------------|----------------|-----------------|----------------|
| **Numeric**     | int (Integer)  |   a = 10        | Holds whole numbers (e.g., 0, 100, -5). |
|                 | float (Float)  |   a = 10.5      | Numbers with decimal or fractional part. |
|                 | bool (Boolean) |   x = True      | Represents truth values: `True` or `False`. |
|                 | complex        |   a = 2 + 3j    | Numbers with real and imaginary parts. |


* **_Sequence & Collection Types_**
* Meaning: you can access elements using indexing, slicing, or keys.

| **Data Type** | **Category**      | **Example**                           | **Definition** |
|---------------|------------------|---------------------------------------|----------------|
| **str**       | Text Type         | `a = 'x'` or `"x"` or `"""Hello"""`   | Holds textual data (sequence of characters). **immutable** (cannot be changed). |
| **list**      | Sequence Type     | `a = [1, 2.5, "Hello", [1, 2, 3], True]` | Stores multiple items, **mutable** (can be changed). |
| **tuple**     | Sequence Type     | `a = (1, 2.5, "Hello")`               | Stores multiple items, **immutable** (cannot be changed). |
| **range**     | Sequence Type     | `for i in range(5): print(i)`         | Generates a sequence of numbers, often used in loops. |
| **set**       | Set Type          | `a = {1, 2, 3, 4, 5}`                 | Unordered collection of unique items (duplicates removed). **mutable** |
| **frozenset** | Set Type          | `fs = frozenset([1, 2, 3])`           | Same as set, but **immutable**. |
| **dict**      | Mapping Type      | `a = {"key1": "value1", "key2": "value2"}` | Stores data in **key-value pairs**. |
| **bytes**     | Binary Type       | `b = b'Hello'`                        | Immutable sequence of bytes. |
| **bytearray** | Binary Type       | `ba = bytearray(b'Hello')`            | Mutable sequence of bytes. |



----------------------------------------------------------------------------------------------
### 📊 Data Types Comparison Table
----------------------------------------------------------------------------------------------


| **Data Type** | **create**  | **Mutable**       | **immutable**     | **Ordered** | **duplicate**     |
|---------------|-------------|-------------------|-------------------|-------------|-------------------|
| **Numeric**   | 10 or 1.4   |    No             |    Yes            |     Yes     |  Yes              |
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
    print(a)                     # Output none
    print(type(a))               # Output <class 'str'> 

```

----------------------------------------------------------------------------------------------
### 🔢 2. Numeric type   (immutable)
----------------------------------------------------------------------------------------------

* In Python, the numeric types refer to the data types that represent numbers, which include 
   * int(0,100) 
   * float(10.0)
   * bool(true or false)
   * Complex Numbers(1a)



----------------------------------------------------------------------------------------------
### 🧵 3. String ("immutable")
----------------------------------------------------------------------------------------------
* In Python, strings are an essential data type used to represent textual data.
* Definition: A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' / """ """).
 - Example: 'hello', "python", """world"""
* String Methods: Python provides many built-in methods to manipulate strings.
 - Examples: .replace(), .split(), .lower(), .upper(), .strip(), etc.
* String Immutability: Strings are **immutable**, meaning once created, they cannot be modified.
 - Operations like concatenation or .replace() return a new string instead of changing the original one.

```
   s = "hello python" 
   print(s)                 # Output: hello python
   print(type(s))           # Output: <class 'str'>

```

----------------------------------------------------------------------------------------------
### 🧾 4. List ["mutable"]
----------------------------------------------------------------------------------------------

* A **list** in Python is an **ordered, mutable collection** that can hold different data types: 
   * integers, 
   * floats, 
   * strings, and even other lists.  
* Lists are enclosed in **square brackets [ ]** and elements are separated by commas.
* Since lists are **mutable**, their elements can be changed after creation.

📌 **Key Features of Python Lists:**
  * **Ordered:** Items in a list have a defined order, and that order will not change unless modified.  
  * **Mutable:** Lists can be changed after creation — you can add, update, or remove elements.  
  * **Heterogeneous:** A single list can store elements of different data types (e.g., integers, strings, booleans, even other lists).  
  * **Duplicates Allowed:** Lists can contain duplicate values; the same element can appear multiple times.  


* Creating a list with various types of elements*

```      
   l = [10,20,30,3.4,"python",True]

   print(l)                           # Output: [10,20,30,3.4,"python",True]

   print(type(l))                     # Output: <class 'list'>

```

* Lists are mutable, which means we can change their elements. We can modify an element by accessing it using its index, or add elements using methods like append().
* Lists in Python are ordered collections — elements are stored in a sequence (index 0, 1, 2, ...).
* The append() method adds an element to the end of the list.




----------------------------------------------------------------------------------------------
### 📦 5. Tuple (immutable)
----------------------------------------------------------------------------------------------

* A **tuple** is a built-in data structure in Python, very similar to a **list**. However, unlike lists, **tuples are immutable** — their elements cannot be changed after creation.
   
📌 **Key Points:**
  * **Immutable:** Once a tuple is created, its elements cannot be modified, added, or removed.
  * **Ordered:** Like lists, tuples maintain the order of elements.
  * **Different Data Types:** A tuple can store elements of various data types (e.g., integers, strings, floats, etc.).
  * **Duplicates Allowed:** Tuples can have multiple occurrences of the same element.
  * **Parentheses:** Tuples are usually created using () (parentheses), though they are optional in some cases (e.g., creating a single element tuple requires a trailing comma).


* If you want to create a **tuple with only one element**, you must add a **trailing comma**.  
* Without the comma, Python will treat it as a normal value inside parentheses, not a tuple.
   


```
      t = ("ashoka",12,23.4,10)

      print(t)                         # Output: ('ashoka', 12, 23.4, 10)

      print(type(t))                   # Output: <class 'tuple'>

      t[1] = 33                        # ❌ Trying to change index 1 (value 12 to 33)

      print(t)                         # Output ('ashoka', 12, 23.4, 10)  elements cannot be modified

```




----------------------------------------------------------------------------------------------
### 🧾 6 . Set {Mutable}
----------------------------------------------------------------------------------------------
* A **set** is an **unordered** collection of **unique elements**. 
* Duplicate values are automatically removed when creating a set.

📌 **Key Points:**

  * **Unordered:** The elements in a set do not have any specific order. When you print a set, its elements may not appear in the order they were added.
  * **Unique Elements:** Sets automatically remove duplicate elements, so each element is stored only once.
  * **Mutable:** Sets are mutable, meaning you can add or remove elements after creation.
  * **Different Data Types:** A set can hold elements of different data types (e.g., integers, strings, etc.).

*Creating Sets:*
* To create a non-empty set, you can use curly braces {}.
* To create an empty set, you need to use the set() function because {} creates an empty dictionary, not a set.
   
* Example: Empty set

```   
   s = set()

   print(s)                        # Output: set()

   print(type(s))                  # Output: <class 'set'>

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

* Empty dictionary  

```
   d = dict()

   # or

   d = {}

   print(d)                                           # Output: {}

   print(type(d))                                     # Output: <class 'dict'>
      
```


----------------------------------------------------------------------------------------------
### ✨ 8.range (immutable)
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
      
   print(list(r))          # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   
   print(type(r))          # Output: <class 'range'>

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
----------------------------------------------------------------------------------------------
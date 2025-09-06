
----------------------------------------------------------------------------------------------
### 👉 Data types in Python
----------------------------------------------------------------------------------------------

* Python Data Types are used to define the type of a variable.
* They represent the kind of value a variable holds (e.g., numbers, strings, etc.), and they determine what operations can be performed on that value.
* Python data types are the classification of data items. They represent the kind of value stored in a variable and determine the operations that can be performed on that value.

#### 🔹 Mutable vs Immutable Types

- **Mutable:** Data types whose values **can be changed** after creation.  
- **Immutable:** Data types whose values **cannot be changed** after creation.  


* **_Basic Data Types_**

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
| **str**       | Text Type         | `a = 'x'` or `"x"` or `"""Hello"""`   | Holds textual data (sequence of characters). |
| **list**      | Sequence Type     | `a = [1, 2.5, "Hello", [1, 2, 3], True]` | Stores multiple items, **mutable** (can be changed). |
| **tuple**     | Sequence Type     | `a = (1, 2.5, "Hello")`               | Stores multiple items, **immutable** (cannot be changed). |
| **range**     | Sequence Type     | `for i in range(5): print(i)`         | Generates a sequence of numbers, often used in loops. |
| **set**       | Set Type          | `a = {1, 2, 3, 4, 5}`                 | Unordered collection of unique items (duplicates removed). |
| **frozenset** | Set Type          | `fs = frozenset([1, 2, 3])`           | Same as set, but **immutable**. |
| **dict**      | Mapping Type      | `a = {"key1": "value1", "key2": "value2"}` | Stores data in **key-value pairs**. |
| **bytes**     | Binary Type       | `b = b'Hello'`                        | Immutable sequence of bytes. |
| **bytearray** | Binary Type       | `ba = bytearray(b'Hello')`            | Mutable sequence of bytes. |


==========================================================================================
### 1. none
===========================================================================================

* nothing is there in the variable

 ```     
      a = 'none'
      print('none')
      print(a)
      print(type(a))
```

==========================================================================================
### 2. Numeric type
===========================================================================================

* In Python, the numeric types refer to the data types that represent numbers, which include -- int(0,100), float(10.0), bool(true or false), Complex Numbers(1a)

```      
      a = 10
      print(a)
      print(type(a))

```

```
      a = 3.14
      print(a)
      print(type(a))
```     

* int to flot convert

```      
      a = 10
      print(a)
      print(type(a))


      b = float(a)
      print(b)
      print(type(b))
```

**Enter runtime** - when you enter a value at runtime using input() function the default datatype is *string*


```
      a = input("enter num1:")
      print(type(a))
      x = int(a)
      print(type(x))
```

```
      a = input("enter number1:")
      print(a)
      print(type(a))
      x = int(a)  #_here we converting str to int_
      print(x)
      print(type(x))

      b = input("enter number2:")
      print(b)
      print(type(b))
      y = int(b)  #_here we converting str to int_
      print(type(y))
      
      c = x+y
      print("sum c is", c)

```   

_A More Concise Way_


```
      a = int(input("Enter num1:"))
      b = int(input("enter num2:"))
      c = a + b
      print("sum is:", c)

```

```
      a = float(input("Enter num1:"))
      b = float(input("enter num2:")) 
      c = a + b
      print("sum is:", c)

```

* bool = true or false

```      
      a = 10
      b = 20
      c = a > b
      print(c)
      print(type(c))

```


==========================================================================================
### 3. String (immutable)
===========================================================================================

* In Python, strings are an essential part of the language used to represent textual data. 
* _String Definition_: A string is a sequence of characters enclosed in either single quotes (' ') or double quotes (" ").
   * Example: ('hello'), ("python"), ("""world""")
* _String Methods_: Python provides a variety of built-in methods to perform operations on strings. Some of these include methods like replace(), split(), lower(), upper(), and many more.
* _String Immutability_: Strings in Python are immutable, meaning once a string is created, it cannot be modified. Operations like replace() or string concatenation will create new strings rather than modifying the original string.

```  
   
* with '' 

    
      s = 'hello ashoka's'
      print(s)           # Output: hello ashoka
      print(type(s))     # Output: <class 'str'>

      s = 'hello ashoka\'s'
      print(s)           # add \ for print
      print(type(s))     # Output: <class 'str'>
```

* with ""

```
      s = "hello ashoka" 
      print(s)           # Output: hello ashoka
      print(type(s))     # Output: <class 'str'>
```

```
      s = "Hello"
      print(s[0])   # Output: H (first character)
      print(s[-1])  # Output: o (last character)
      print(s[0:5])   # Output: Hello (from index 0 to 4)
```

```
      s = "Hello"
      repeated = s * 3
      print(repeated)  # Output: HelloHelloHello

```

```
      s = "  Hello, World!  "
      print(s.upper())   # Output: HELLO, WORLD!
      print(s.lower())   # Output: hello, world!
      print(s.strip())   # Output: Hello, World! used to remove any leading and trailing whitespace characters from a string
      print(s.replace("World", "Python"))  # Output:   Hello, Python!  
      print(s.split())   # Output: ['Hello,', 'World!']
      print(s.find("World"))  # Output: 8 (index of the first occurrence of "World")

```

* Replacing 'hello' with 'hai' (note this does not change s, since strings are immutable)*

```      
      s.replace("hello", "hai")
      print(s)           # Output: hello ashoka (s is unchanged)
```

*The replace method returns a new string, we can assign the result to a variable*
*we can not reuse "s" value*
```

      print(s.replace("hello","hai")) 

```
*We can assign the modified string to a new variable*
```      
      s1 = s.replace("hello", "hai")
      print(s1)          # Output: hai ashoka
```
**To get a list of all available functions for string operations, you can use the dir() function:**
* This will return a list of all the methods and attributes associated with the string class.
```
      print(dir(str))
      __add_  #also called descriptors
```
      
```    
       * description    
      help(str)
```


==========================================================================================
### 4. List [mutable]
===========================================================================================

* A list in Python is an **ordered** collection that can hold a variety of different data types, including integers, floats, strings, and even other lists. 
* Lists are enclosed in square brackets [] and elements are separated by commas.


* Key Features of Python Lists:*
   * **Ordered:** The items in a list have a specific order, and that order is preserved.
   * **Mutable:** Lists can be modified after creation. You can change, add, or remove elements.
   * **Heterogeneous:** Lists can store elements of different data types (e.g., integers, strings, booleans, etc.).
   * **Allow duplicates:** Lists allow duplicate elements, meaning the same value can appear multiple times in a list.
   
* Creating a list with various types of elements*

```      
      l = [10,20,30,3.4,"python",True]
   *Printing the list and its type*
      print(l)            # Output: [10, 20, 30, 3.4, 'att', True]
      print(type(l))      # Output: <class 'list'>

```

* Lists are mutable, which means we can change their elements. We can modify an element by accessing it using its index, or add elements using methods like append().

```      
      l = [10,20,30,3.4,"ashoka",True]
      l.append(33)        # Adds 33 to the end of the list
      print(l)            # Output: [10, 20, 30, 3.4, 'att', True, 33]
```

```
      *Modifying an element at a specific index*

      l[1] = 33           # Changes the element at index 1 (value 20) to 33
      print(l)            # Output: [10, 33, 30, 3.4, 'att', True, 33]
```

**Key Methods for Working with Lists:**
* **append(value)** — Adds an element to the end of the list.
```
      l = [10,20,30,3.4,"ashoka",True]
      l.append(33)        # Adds 33 to the end of the list
```
* **insert(index, value)** — Inserts an element at a specific index in the list.
```
      my_list = [10, 20, 30]
      my_list.insert(1, 15)  # Inserts 15 at index 1
      print(my_list)  # Output: [10, 15, 20, 30]
```
* **remove(value)** — Removes the first occurrence of the specified value.
```
      my_list = [10, 20, 30, 40, 20]
      my_list.remove(20)  # Removes the first occurrence of 20
      print(my_list)  # Output: [10, 30, 40, 20]
```
* **pop(index)** — Removes the element at the specified index and returns it.
```
      my_list = [10, 20, 30, 40, 50]
      popped_item = my_list.pop(2)  # Removes the element at index 2 (30)
      print(my_list)  # Output: [10, 20, 40, 50]
      print("Popped Item:", popped_item)  # Output: Popped Item: 30

```
* **extend(iterable)** — Extends the list by appending all elements from another iterable (e.g., another list).
```
   # Original list
      my_list = [1, 2, 3]
   # Another list to extend my_list with
      other_list = [4, 5, 6]
   # Using extend() to add elements of other_list to my_list
      my_list.extend(other_list)
      print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
```

* **index(value)** — Returns the index of the first occurrence of the specified value.
```
      my_list = [10, 20, 30, 40, 50]
      index_of_30 = my_list.index(30)
      print(index_of_30)  # Output: 2 (The index of 30 is 2)
```
* **sort()** — Sorts the list in ascending order. 
```
      my_list = [4, 1, 3, 9, 2]
      my_list.sort()
      print(my_list)  # Output: [1, 2, 3, 4, 9]
```


==========================================================================================
### 5. Tuple(immutable)
===========================================================================================

* A tuple is a built-in data structure in Python that is very similar to a list. However, unlike lists, tuples are immutable, which means their elements cannot be changed after creation.
   
**Key Points:**
*  *Immutable:* Once a tuple is created, its elements cannot be modified, added, or removed.
*  *Ordered:* Like lists, tuples maintain the order of elements.
*  *Different Data Types:* A tuple can store elements of various data types (e.g., integers, strings, floats, etc.).
*  *Duplicates Allowed:* Tuples can have multiple occurrences of the same element.
*  *Parentheses:* Tuples are usually created using () (parentheses), though they are optional in some cases (e.g., creating a single element tuple requires a trailing comma).


* tuple required multipile values*
* The trailing comma is necessary to differentiate a tuple with one element from a regular value enclosed in parentheses.
   
```      
      t = ("raj",)
      print(t)      # Output: ('raj',)
      print(type(t)) # Output: <class 'tuple'>

```

* Without the trailing comma, this is just a string enclosed in parentheses.*
      
```      
      t = ("raj")  # This is a string, not a tuple
      print(t)  # Output: raj
      print(type(t))  # Output: <class 'str'>

```

```
      t = ("raj",12,23.4,10)
      print(t)
      print(type(t))
      t[1] = 33
      print(t)  # output t can not be changed

```

```
      nested_tuple = (1, 2, (3, 4), 5)
      print(nested_tuple[2])
```


==========================================================================================
### 6 . Set {}
===========================================================================================

* A set is an "unordered" collection of unique elements. This means that duplicate values are automatically removed when creating a set.

*Key Points:*
   * *Unordered:* The elements in a set do not have any specific order. When you print a set, its elements may not appear in the order they were added.
   * *Unique Elements:* Sets automatically remove duplicate elements, so each element is stored only once.
   * *Mutable:* Sets are mutable, meaning you can add or remove elements after creation.
   * *Different Data Types:* A set can hold elements of different data types (e.g., integers, strings, etc.).

*Creating Sets:*
* To create a non-empty set, you can use curly braces {}.
* To create an empty set, you need to use the set() function because {} creates an empty dictionary, not a set.
   

```      
      s = set()
      print(s)          # Output: set()
      print(type(s))    # Output: <class 'set'>

```   

```
      s = {10, 20, 30, 40, 50, 60}
      print(s)  # Output: {50, 20, 40, 10, 60, 30}
      print(type(s))  # Output: <class 'set'>
```

```
      s = {10, 10, 20, 30, 40, 50, 60, 60}
      print(s)  # Output: {50, 20, 40, 10, 60, 30}
      print(type(s))  # Output: <class 'set'>

```

* *Adding elements to a set:*
```   
      s = {10, 20, 30, 40, 50, 60}   
      s.add(70)  # Adds 70 to the set
      print(s)  # Output: {50, 20, 70, 40, 10, 60, 30}


```
* *Removing elements from a set:*

```      
      s = {10, 20, 30, 40, 50, 60}
      s.remove(20)  # Removes 20 from the set
      print(s)  # Output: {10, 30, 40, 50, 60, 70}
```

* *Set operations like union, intersection, and difference are also commonly used:*
      
```
The union of two sets returns a new set that contains all unique elements from both sets
      s = {10, 20, 30, 40, 50}
      s1 = {50, 60, 70, 80}
      print(s.union(s1))  # Union: {10, 20, 30, 40, 50, 60, 70, 80}
```

```
intersection of two sets returns a new set that contains only the elements that are common to both sets.
      s = {10, 20, 30, 40, 50}
      s1 = {50, 60, 70, 80}
      print(s.intersection(s1))  # Intersection: {50}

```




==========================================================================================
### 7. Dictionary dict {}
===========================================================================================
* A dictionary is an unordered collection of key-value pairs. It stores elements in pairs, where each key is associated with a value.
* data in dictionary stores in key, value pair {key, value} --> item

**Key Points:**
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
      print(d)       # Output: {}
      print(type(d)) # Output: <class 'dict'>
      
```

```
      capital_city = {'TS':'Hyd', 'AP':'AMV','TN':'CH'}
      print(capital_city)        # Output: {'TS': 'Hyd', 'AP': 'AMV', 'TN': 'CH'}
      print(capital_city['TS'])  # Output: Hyd
      print(capital_city['AP'])  # Output: AMV

```   
  

```
   *Duplicate Keys:*

      capital_city = {'TS':'Hyd', 'TS':'AMV','TN':'CH'}
      print(capital_city)    # Output: {'TS': 'AMV', 'TN': 'CH'}

```

  
```
   *Modifying Dictionary Values:*

      capital_city = {'TS':'Hyd', 'TG':'HYD','TN':'CH'}
      print(capital_city)     # Output: {'TS': 'Hyd', 'TG': 'HYD', 'TN': 'CH'}

```

```
   *Changing values in a dictionary*

      d = {1:'sai',2:'att'}
      print(d)         # Output: {1: 'sai', 2: 'att'}
      print(type(d))   # Output: <class 'dict'>
      d[2] = 'ramesh'  # Changing the value for key 2 
      print(d)         # Output: {1: 'sai', 2: 'ramesh'}

```

``` 
  *Adding key-value pairs at runtime:*
  *Get user input for key-value pairs*

      person = {}
      name = input("Enter person's name:")
      age = int(input("Enter person's age:"))
      city = input("Enter person's city:")

  *Add key-value pairs to the dictionary*
      
      person['name'] = name
      person['age'] = age
      person['city'] = city

      print("Dictionary after adding runtime values:", person)
      print(type(person))   # Output: <class 'dict'>
```


===========================================================================================
**8. range()**
========================================================================================
* The range() function in Python is used to generate a sequence of numbers. It's typically used in for loops to iterate over a specific range of values.
   
**Key Points:**
* **1.Start, Stop, Step:**
   * *Start:* The number where the range begins (inclusive).
   * *Stop:* The number where the range ends (exclusive).
   * *Step:* The interval between each number in the range.
   * If the step is not specified, it defaults to 1.
   * If the start is not specified, it defaults to 0.

**Immutability:**
   * range() objects are immutable, meaning you cannot modify the values in a range once it’s created.

**Use Cases:**
   * The range() function is often used in loops (like for loops) to repeat actions a certain number of times.

* #Examples

      r = range(10)
      print(r)            # Output: range(0, 10)
      print(type(r))      # Output: <class 'range'>
      print(list(r))      # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      print(type(r))      # Output: <class 'range'>

   * range(10) generates a sequence starting from 0 up to (but not including) 10.
   * We can convert it to a list using list(r) to see the actual values in the range.
   * range() itself does not store the sequence in memory; it generates the numbers on demand, which is why it shows as range(0, 10) when printed.
      
      r = range(2, 10, 2)  # start=2, stop=10, step=2
      print(tuple(r))      # Output: (2, 4, 6, 8)
      print(type(r))       # Output: <class 'range'>

   * range(2, 10, 2) starts from 2, goes up to (but not including) 10, and increments by 2 each time.
   * We can convert the range to a tuple to see the sequence of numbers: (2, 4, 6, 8).

     
      for i in range(5):
      print(i)


===========================================================================================
**9. bytes**
========================================================================================
   *the bytes data type represents sequences of bytes, which are immutable sequences of integers, each representing a byte value from 0 to 255

   #Examples

      b = bytes([65, 66, 67])  # ASCII values for 'A', 'B', 'C'
      print(b)  # Output: b'ABC'


===========================================================================================
**10. bytearray**
========================================================================================
   *In Python, bytearray is a mutable sequence of integers in the range 0 <= x <= 255. It is similar to bytes, but unlike bytes, bytearray objects can be modified after creation.


* #Examples

      ba = bytearray([65, 66, 67])  # ASCII values for 'A', 'B', 'C'
      print(ba)  # Output: bytearray(b'ABC')

===========================================================================================
**11. frozenset**
========================================================================================
   *frozenset is an immutable version of a set, which means once it is created, its elements cannot be changed or modified.

   #Examples

      frozen_set = frozenset([1, 2, 3, 4, 5])
      print(frozen_set)  # Output: frozenset({1, 2, 3, 4, 5})



![alt text](https://github.com/acmarpu/images/blob/main/Python/Python.png)
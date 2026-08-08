![alt text](https://github.com/acmarpu/images/blob/main/Python/03_python_datatypes.png)

- [Data Types](#-data-types-in-python)
  - [Mutable vs Immutable Types](#-mutable-vs-immutable-types)
  - [Basic Data Types](#-basic-data-types)
      - [none](#-1-none)
  - [Sequence & Collection Types](#sequence--collection-types)
      - [Numeric Data Type](/01_Python_Basics/04_numeric_data_type.ipynb)
      - [String Data Type](/01_Python_Basics/05_string_data_type.ipynb)
      - [List Data Type](/01_Python_Basics/06_list_data_type.ipynb)
      - [Tuple Data Type](/01_Python_Basics/07_tuple_data_type.ipynb)
      - [Set Data Type](/01_Python_Basics/08_set_data_type.ipynb)
      - [Dictionary Data Type](/01_Python_Basics/09_dictionary_data_type.ipynb)
      - [Range Data Type](/01_Python_Basics/10_range_data_type.ipynb)
      - [bytes_bytearray_frozenset](/01_Python_Basics/11_bytes_and_bytearray_data_type.ipynb)


----------------------------------------------------------------------------------------------
### 👉 Data Types in Python
----------------------------------------------------------------------------------------------
* Python Data Types are used to define the type of a variable.
* They represent the kind of value a variable holds (e.g., numbers, strings, etc.).
* Data types determine the **operations** that can be performed on a value.
* Python is a **dynamically typed** language (no need to declare data types explicitly).

* None
* Numeric Data Types
* String 
* List
* Tuple
* Set Data Type
* Dictionary Data Type
* Range Data Type
* bytes
* bytearray
* frozenset

----------------------------------------------------------------------------------------------
##### 🔹 Mutable vs Immutable Types
----------------------------------------------------------------------------------------------
- **Mutable:** Data types whose values **can be changed** after creation.  
- **Immutable:** Data types whose values **cannot be changed** after creation.  

----------------------------------------------------------------------------------------------
## 📘 **_Basic Data Types_**
----------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------
### 🔹 1. none
----------------------------------------------------------------------------------------------

* nothing is there in the variable

| **Data Type**   | **Category**   | **Example**     | **Definition** |
|-----------------|----------------|-----------------|----------------|
| **None**        | NoneType       |   a = None      | Represents the absence of a value or null. |

 ```     
    my_none = 'none'
    print("none value:", my_none, type(my_none))    # Outpu none value: none <class 'str'>
    
```

----------------------------------------------------------------------------------------------
## **_Sequence & Collection Types_**
----------------------------------------------------------------------------------------------
* Meaning: access elements using indexing, slicing, or keys. string, list , tuple 
* Dictionary, set - do not support indexing 

|                        |   |   |   |   |   |   |   |   |
|------------------------|---|---|---|---|---|---|---|---|
|**Positive Indexing**   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|**Element**             | W | E | L |   | C | O | M | E |
|**Negative indexing**   |-8 |-7 |-6 |-5 |-4 |-3 |-2 |-1 |

<br>

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

<br>

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
#### Data Types introduction Completed 

📖 **Next Topic:**
👉 [Numeric Data Type](/01-python-fundamentals/04_numeric_data_type.ipynb)
----------------------------------------------------------------------------------------------
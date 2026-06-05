--------------------------------------------------------------------------------------------------
### 📦 Tuple
--------------------------------------------------------------------------------------------------
#### 1. what is tuple: 

* A **tuple** is a built-in data structure in Python, very similar to a **list**. However, unlike lists, **tuples are immutable** — their elements cannot be changed after creation.
   
📌 **Key Points:**
  * **Immutable:** Once a tuple is created, its elements cannot be modified, added, or removed.
  * **Ordered:** Like lists, tuples maintain the order of elements.
  * **Different Data Types:** A tuple can store elements of various data types (e.g., integers, strings, floats, etc.).
  * **Duplicates Allowed:** Tuples can have multiple occurrences of the same element.
  * **Parentheses:** Tuples are usually created using () (parentheses), though they are optional in some cases (e.g., creating a single element tuple requires a trailing comma).


* If you want to create a **tuple with only one element**, you must add a **trailing comma**.  
* Without the comma, Python will treat it as a normal value inside parentheses, not a tuple.
   

#### 2. creating tuple : ()

```   
   t = (10, 20, 30, 40)
   print(t)

```
```
   # Tuple with mixed data types (heterogeneous)
   t4 = (10, 3.5, "python", True)
   print(t4)                            # Output: (10, 3.5, 'python', True)

```

#### 3. creating tuple with one element:
* Must include a comma ( , ) after the element.

```
   t = (10,)
   print(t)

```

#### 4. accessing elements from tuple

```
   t = (10, 20, 30, 40)
   print(t[1])                         # Output: 20
   print(t[-1])                        # Output: 40

```
#### 5. tuple slicing
```
   t = (10, 20, 30, 40, 50, 60)
   print(t[1:4])                       # Output: (20, 30, 40)

```

#### 6. tuple immutable
* Tuples cannot be modified (no item assignment).

```
   t = ("mac",10,3.5,10,10)
   print(t)                            # ('mac', 10, 3.5, 10, 10)
   print(type(t))                      # <class 'tuple'>

   t[1] = 33
   print(t)                           # Output : ❌ TpyeError: tuple object does not support item assignment

```
#### 7. tuple concatenation and multiplication
* adding one or more tuples in to single concatenation

```
   t1 = (10, 20)
   t2 = (30, 40)
   print(t1 + t2)                     # Concatenation → (10, 20, 30, 40)
   print(t1 * 2)                      # Multiplication → (10, 20, 10, 20)

```
   
#### 8. deleting a tuple

```
   t = (10, 20, 30)
   del t
```

#### 9. count and index

```
   t = (10, 20, 10, 30, 10)
   print(t.count(10))                    # Output: 3
   print(t.index(30))                    # Output: 3

```

```
   t = ("mac",10,3.5,10,10,"mac","mac",10,10)
   print(t.count(mac))                   # Outpit: 5
   print(t.index(3.5))                   # Output: 2

```
   
#### 10. tuple membership test

```
   t = (10, 20, 30)  
   print(20 in t)                        # Output: True
   print(40 not in t)                    # Output: True

```

```
   t = ("mac",10,3.5,10,10,"mac","mac",10,10)
   print(100 in t)                               # False

```
#### 11. len(),max(),min(),sum()

```
   t = ("mac",10,3.5,10,10,"mac","mac",10,10)
   print(len(t))                                 # Output 6

   t = (10,3.-5,10,10,10,10)
   print(max((t)))                               # Output 10
   print(min((t)))                               # Output -2.0
   print(sum((t)))                               # Output 48.0      

```  
#### 12. converting a string into tuple

```
   s = "python"
   t = tuple(s)
   print(t)                     # Output: ('p', 'y', 't', 'h', 'o', 'n')

```
#### 13. converting a list into tuple

```
   l = [10, 20, 30]
   t = tuple(l)
   print(t)                     # Output: (10, 20, 30)

```
#### 14. converting a tuple into string

```
   t = ('p', 'y', 't', 'h', 'o', 'n')
   s = ''.join(t)
   print(s)                     # Output: python

```
#### 15. packing and unpacking

```
  t = (10, 20, 30)
  a, b, c = t
  print(a, b, c)                # Output: 10 20 30

```


* A nested tuple means a tuple inside another tuple
```
      nested_tuple = (1, 2, (3, 4), 5)

      print(nested_tuple[0])           # Output: 1

      print(nested_tuple[1])           # Output: 2

      print(nested_tuple[2])           # Output: (3, 4) ← (this itself is another tuple)

      print(nested_tuple[3])           # Output: 5
``
----------------------------------------------------------------------------------------------
✅ End of tuple_data_type.md
----------------------------------------------------------------------------------------------

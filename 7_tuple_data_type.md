--------------------------------------------------------------------------------------------------
### 📦 Tuple
--------------------------------------------------------------------------------------------------
#### 1. what is tuple: 
* A **tuple** is an *ordered collection of elements*, similar to a list.  
* Unlike lists, **tuples are immutable**, meaning their elements **cannot be changed** after creation.

#### 2. creating tuple : ()

```
   
   t = (10, 20, 30, 40)
   print(t)

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
   print(t[1])             # Output: 20
   print(t[-1])            # Output: 40

```
#### 5. tuple slicing
```
   t = (10, 20, 30, 40, 50, 60)
   print(t[1:4])           # Output: (20, 30, 40)

```

#### 6. tuple immutable
* Tuples cannot be modified (no item assignment).

```
   t = ("mac",10,3.5,10,10)
   print(t)                 # ('mac', 10, 3.5, 10, 10)
   print(type(t))           # <class 'tuple'>

   t[1] = 33
   print(t)                 # Output : ❌ TpyeError: tuple object does not support item assignment

```
#### 7. tuple concatenation and multiplication
* adding one or more tuples in to single concatenation

```
   t1 = (10, 20)
   t2 = (30, 40)
   print(t1 + t2)          # Concatenation → (10, 20, 30, 40)
   print(t1 * 2)           # Multiplication → (10, 20, 10, 20)

```
   
#### 8. deleting a tuple


```
   t = (10, 20, 30)
   del t
```

#### 9. count and index

```
   t = (10, 20, 10, 30, 10)
   print(t.count(10))         # Output: 3
   print(t.index(30))         # Output: 3

```

```
   t - ("mac",10,3.5,10,10,"mac","mac",10,10)
   print(t.count(mac))
   print(t.index(3.5))

```
   
#### 10. tuple membership test

```
   t = (10, 20, 30)  
   print(20 in t)             # Output: True
   print(40 not in t)         # Output: True

```

```
   t - ("mac",10,3.5,10,10,"mac","mac",10,10)
   print(100 in t)            # False

```
#### 11. len(),max(),min(),sum()

```
   t = ("mac",10,3.5,10,10,"mac","mac",10,10)
   print(len(t))              # Output 6

   t = (10,3.-5,10,10,10,10)
   print(max((t)))            # Output 10
   print(min((t)))            # Output -2.0
   print(sum((t)))            # Output 48.0      

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

----------------------------------------------------------------------------------------------
✅ End of tuple_data_type.md
----------------------------------------------------------------------------------------------

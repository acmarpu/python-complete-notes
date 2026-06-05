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


----------------------------------------------------------------------------------------------
✅ End of bytes & bytearray and frozenset
----------------------------------------------------------------------------------------------
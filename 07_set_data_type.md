--------------------------------------------------------------------------------------------------
### 🧾 Set
--------------------------------------------------------------------------------------------------
#### 1. What is a Set
* A **set** is an **unordered collection of unique elements**.
* It automatically **ignores duplicate elements**.
* Sets are **mutable**.
* Sets do **not support indexing or slicing** (because they are unordered).
* Sets are created using **curly braces `{}`** or the `set()` function.

#### 2. creating set 

```
   s = set()
   print(s)         
   print(type(s))                    # Output <class 'set'>

```
```
   s = {10,20,30,"mac",34.5}
   print(s)                         # Output {34.5, 20, 'mac', 10, 30}
   print(type(s))                   # Output <class 'set'>
   s.add(99)
   print(s)                         # Output {34.5, 99, 'mac', 20, 10, 30}

```   

#### 3. creating an empty set
* Note: Using {} creates a dictionary, not a set.
   
```
   s = {}
   print(s)
   print(type(s))                  # Output    <class 'dict'>

```    
#### 4. how to change set (add and update)

```
   s = {10,20,30,"mac",34.5}
   print(s)                        # Output {34.5, 'mac', 20, 10, 30}
   print(type(s))                  # Output <class 'set'>
   s.add(99)                
   print(s)                        # Output {34.5, 99, 'mac', 20, 10, 30}

```

```
   s = {10,20,30,"mac",34.5}
   print(s)                       # Output {34.5, 'mac', 20, 10, 30}
   print(type(s))                 # Output <class 'set'>
   s.update([36,"mac",True]) 
   print(s)                       # Output {True, 34.5, 99, 20, 36, 10, 'mac', 30}

```
#### 5. remove elements from set(discard and remove), clear(), del
* Methods: discard(), remove(), clear(), del

```
   s = {10,20,30,"mac",34.5}
   s.discard(10)
   print(s)                 # Output {20, 30, 'mac', 34.5}

```

```
   s.remove(10)
   print(s)                # Output {10, 30, 'mac', 34.5}

```

```
   s = {10, 20, 30}
   s.clear()
   print()                 # Output: set()

```

```
   s = {10, 20, 30}
   del s

```

#### 6. set operation -- union (|)
* Operations: Union (|), Intersection (&), Difference (-), Symmetric Difference (^)
* All results contain only unique elements.

```
   a = {1,2,3,4,5}
   b = {4,5,6,7,8}
   print(a|b)                # Output {1, 2, 3, 4, 5, 6, 7, 8}
   print(a.union(b))         # Output {1, 2, 3, 4, 5, 6, 7, 8}

```

* intersection
```
   A = {1,2,3,4,5}
   B = {4,5,6,7,8}
   print(A&B)                # Output {4,5}
   print(A.intersection(B))  # Output {4,5}

```
* difference

```
   print(a-b)               # Output {1,2,3}
   print(a.difference(b))   # Output {1,2,3}
   print(b.difference(a))   # Output {8, 6, 7}

```
* symmetric difference
* common values will not print
```
   print(a^b)                        # Output {1, 2, 3, 6, 7, 8}                       
   print(a.symmetric_difference(b))  # Output {1, 2, 3, 6, 7, 8}

```
#### 7. membership test
```
   a = {1,2,3,4,"mac",5}
   print(10 in a)                    # Output False

```
#### 8. len

```
   a = {1,2,3,4,"mac",5}
   print(len(a))                    # Output 6

```
#### 9. max and min

```
   a = {1,2,3,4,5}
   print(max(a))                   # Output 5

```

```
   a = {1,2,3,4,5}
   print(min(a))                   # Output 1

```

#### 10. sum

```
   a = {1,2,3,4,5}
   print(sum(a))                  # Output 15         

```
----------------------------------------------------------------------------------------------
✅ End of set_data_type.md
----------------------------------------------------------------------------------------------
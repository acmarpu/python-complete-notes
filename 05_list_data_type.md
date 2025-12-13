--------------------------------------------------------------------------------------------------
### 🧾 List
--------------------------------------------------------------------------------------------------
* A list is an **ordered collection of elements**.
* It can store **heterogeneous elements** (different data types).
* When a data structure contains more than one data type, it is called heterogeneous.

#### 1. creating a list
   
```
   l = [10,20,30,40,50,60]
   print(l)                               # Output: 10,20,30,40,50,60
   print(type(l))                         # Output: <class 'list'>

```
* # List with mixed data types (heterogeneous)
```
  l3 = [10, 3.5, "python", True]
  print (l3)

```

#### 2. nested list (one or more list)
* A list can contain another list (nested structure).

```
   l = [ 10,20,[30,40],1.0 ]
   print(l[2])                            # Access nested list # Output [30,40]
   print(type(l))                         # Output: <class 'list'>
   print(l[2][0])                         # Access element from nested list # Output 30

```

#### 3. access elements from a list
   
```
   l = [10,20,30,40,50,60]
   print(l[1])                            # Output 20
   print(type(l))

```

#### 4. list slicing (perticulear part of the string)
⚠️ Note: Negative indexing is supported, but “backward slicing” (like l[-1:-4]) won’t work unless step is -1.
   
```
   l = [10,20,30,40,50,60]
   print(l)
   print(l[1:4])                           # Output: [20, 30, 40]

```

#### 5. changing or adding elements

```
   l = [10,20,30,40,1.0]
   print(l)
   l[1] =33                               # 1 is index and 33 is element
   print(l)                               # Output: [10, 33, 30, 40, 1.0]
   l.insert(1,33)                         # 1 is index and 33 is value
   print(l)                               # Output: [10, 33, 33, 30, 40, 1.0]

```

#### 6. append and extend methods
* Both append() and extend() are used to add elements to a list.
* append method : Adds a single element to the end of the list
* extend method : Adds multiple elements (iterable) to the end of the list


```
   l = [10,20,30,40,50,60]
   print(l)                   # Output: [10, 20, 30, 40, 50, 60]
   l.append(33)               # Adds one element at the end
   print(l)                   # Output: [10, 20, 30, 40, 50, 60, 33]


   l.extend([34,"mac",56])    # Adds multiple elements 
   print(l)                   #Output:[10, 20, 30, 40, 50, 60, 33, 34, 'mac', 56]

```

#### 7. inser method in list

```
   l = [1, 2, 3]
   l.insert(1, 99)
   print(l)                   # Output: [1, 99, 2, 3]

```

#### 8.. list concatenation and multiplication

```
   l1 = ["mac","tecj","travel"]
   l2 = ["att","ms","tcs"]
   l3 = l1+l2
   print(l3)                    # Output: ['mac', 'tech', 'travel', 'att', 'ms', 'tcs']
   
   print(l1*2)                  # Output: ['mac', 'tech', 'travel', 'mac', 'tech', 'travel']

```

#### 9. Remove elements remove(), pop(), clear(), del

```
   l = [10,20,30,40,50,60]
   print(l)                     # Output: [10, 20, 30, 40,50,60]

   l.remove(20)                 # remove elements
   print(l)                     # Output: [10, 30, 40,50,60]


   l.pop(2)                     # remove index
   print(l)                     # Output: [10, 30, 50, 60]

   l.clear()
   print(l)                     # Output: []

   del l                        # Delete list completely

```  

#### 10. list sort

```
   l = [2,10,4,8,6,7,8]
   print(l)

   l.sort()                     # Ascending
   print(l)

   l.sort(reverse=True)         # Descending
   print(l)

```  
#### 11. list copy
* Shallow copy = new list, same elements.
* Deep copy = truly independent copy (requires copy module).

```
   l = [2,10,4,8,6,7,8]
   print(l)

   l1 = l.copy()                # Shallow copy
   print(l1)

   l.append(33)
   l1.remove(10)
   print(l1)
   print(l)

```

#### 12. list count

```
   l = [2,10,4,8,6,7,8,5,5,5,5]
   print(l.count(5))             # Output 4

```
  
#### 13. list index

```
   l = [10, 20, 30, 40]
   print(l.index(30))           # Output: 2

```
----------------------------------------------------------------------------------------------
✅ End of Python list_data_type
----------------------------------------------------------------------------------------------
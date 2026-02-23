--------------------------------------------------------------------------------------------------
### 🧾 4. List ["mutable"]
--------------------------------------------------------------------------------------------------
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

#### 1. creating a list   
```
   my_list = [1, 2, 3.5, 4, 5, "apple", True]
   print("List value:", my_list)                 # Output: List value: [1, 2, 3.5, 4, 5, 'apple', True]
   print("List type:", type(my_list))            # Output: List type: <class 'list'>

```

#### 2. nested list (one or more list)
* A list can contain another list (nested structure).

```
   my_list = [1, 2, [3, 4], 5.5, "apple", True]
   print("List value:", my_list)                 # Output: List value: [1, 2, [3, 4], 5.5, 'apple', True]
   print("List type:", type(my_list))            # Output: List type: <class 'list'>

```

#### 3. Access elements in a list
```
   my_list = [1, 2, [3, 4], 5.5, "apple", True]
   print("First element:", my_list[0])           # Output: First element: 1

```

#### 4. list slicing (perticulear part of the string)
⚠️ Note: Negative indexing is supported, but “backward slicing” (like l[-1:-4]) won’t work unless step is -1.  
```
   my_list = [10,20,30,40,50,60]
   print(my_list)                    # Output: [10, 20, 30, 40, 50, 60]
   print(my_list[1:4])               # Output: [20, 30, 40]

```

#### 5. changing or adding insert elements
```
   my_list = [10,20,30,40,50,60]
   print(my_list)                    # Output: [10, 20, 30, 40, 50, 60]
   my_list[2] = 35
   print(my_list)                    # Output: [10, 20, 35, 40, 50, 60]

   my_list.insert(2, 25)
   print(my_list)                    # Output: [10, 20, 25, 35, 40, 50, 60]

```

#### 6. append and extend methods
* Both append() and extend() are used to add elements to a list.
* append method : Adds a single element to the end of the list
* extend method : Adds multiple elements (iterable) to the end of the list

```
   my_list = [10,20,30,40,50,60]
   print(my_list)                    # Output: [10, 20, 30, 40, 50, 60]
   my_list.append(70)  
   print(my_list)                    # Output: [10, 20, 30, 40, 50, 60, 70]


   my_list.extend([80, 90, "apple"])
   print(my_list)                    # Output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 'apple']

```

#### 7. list concatenation and multiplication

```
   my_list1 = ["apple", "banana", "cherry" ]
   my_list2 = ["potato", "tomato", "onion"]

   my_list3 = my_list1 + my_list2
   print(my_list3)                    # Output: ['apple', 'banana', 'cherry', 'potato', 'tomato', 'onion']
   
   print(my_list1 * 2)                # Output: ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']

```

#### 8. Remove elements remove(), pop(), clear(), del

```
   my_list = [10,20,30,40,50,60]
   print(my_list)                    # Output: [10, 20, 30, 40, 50, 60]

   my_list.remove(30)
   print(my_list)                    # Output: [10, 20, 40, 50, 60]

   my_list.pop(2)
   print(my_list)                    # Output: [10, 20, 50, 60]


   my_list.clear()
   print(my_list)                    # Output: []

   del my_list
   print(my_list)                    # Output: NameError: name 'my_list' is not defined

```  

#### 10. list sort
```
   my_list = [10,30,50,20,40,60]
   print("Original list:", my_list)      # Output: Original list: [10, 30, 50, 20, 40, 60]

   my_list.sort()
   print("Sorted list:", my_list)        # Output: Sorted list: [10, 20, 30, 40, 50, 60]

   my_list.sort(reverse=True)
   print("Sorted list in reverse order:", my_list)  # Output: Sorted list in reverse order: [60, 50, 40, 30, 20, 10]

```  
#### 11. list copy
* Shallow copy = new list, same elements.
* Deep copy = truly independent copy (requires copy module).

```
   my_list = [10,30,50,20,40,60]
   print("Original list:", my_list)      # Output: Original list: [10, 30, 50, 20, 40, 60]

   my_list2 = my_list.copy()
   print("Copied list:", my_list2)      # Output: Copied list: [10, 30, 50, 20, 40, 60]

```

#### 12. list count

```
   my_list = [10,30,50,30,20,40,60,30]
   print(my_list.count(30))                    # Output: 3
   print(my_list.count(100))                   # Output: 0

```
  
#### 13. list index

```
   my_list = [10,30,50,30,20,40,60,30]
   print(my_list.index(30))                    # Output: 1

```
----------------------------------------------------------------------------------------------
✅ End of Python list_data_type
----------------------------------------------------------------------------------------------
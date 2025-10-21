--------------------------------------------------------------------------------------------------
### List : 
--------------------------------------------------------------------------------------------------
is order collection of elements
      heterogeneous elements (diffrent types of data types)

#### 1. creating a list
   l = [10,20,30,40,50,60]
   print(l)    # Output 10,20,30,40,50,60
   print(type(l))

#### 2. nested list (one or more list)
   l = [ 10,20,[30,40],1.0 ]
   print(l[2])      # Output 30,40
   print(type(l))
   print(l[2][0])   # Output 30

#### 3. access elements from a list
   l = [10,20,30,40,50,60]
   print(l[1])    # Output 20
   print(type(l))

#### 4. list slicing (perticulear part of the string)
* backward slicing not possible 
   l = [10,20,30,40,50,60]
   print(l)
   printl[1:4]  # Output [10,20,30]

#### 5. changing or adding elements to list

   l = [10,20,[30],40,1.0]
   print(l)
   l[1] =33       # 1 is index and 33 is element
   print(l)       #Output [10,33,30,40,50,60]
   l.insert(1,33) # 1 is index and 33 is value
   print(l)       #Output [10,33,20,30,40,50,60]

#### 6. append and extend methods in list
* append method by default values added last for the list 
* extend method will expect one object 
* append extend values added last for the list 
   l = [10,20,30,40,50,60]
   print(l)
   l.append(33) # last of the list and one element to the list
   print(l) # Output [10,20,30,40,50,60,33]

   l.extend([34,"mac",56]) # multipile elements to the list 
   print(l)       #Output [10,20,30,40,50,60,34,"mac",56]


#### 7. inser method in list
#### 8.. list concatenation and multiplication
   l1 = ["sai","manoj","jaideep"]
   l2 = ["att","ms","tcs"]
   l3 = l1+l2
   print(l3)
   print(l1*2)

#### 9. delete or remove elements form a list
#### 10. remove(), pop(), clear(), del

   l = [10,20,30,40,60]
   print(l)
   l.remove(20) # elements
   print(l)
   l.pop(2) # index
   print(l)
   l.clear()
   print(l)
   del l
   print(l)

#### 11. list sort

   l = [2,10,4,8,6,7,8]
   print(l)
   l.sort()
   print(l)
   l.sort(reverse=True)
   print(l)
  
#### 12. list copy
   shallow copy is normal copy

   deep copy
   l = [2,10,4,8,6,7,8]
   print(l)
   l1 = l.copy()
   print(l1)
   l.append(33)
   l1.remove(10)
   print(l1)
   print(l)
   
#### 13. list count
  l = [2,10,4,8,6,7,8,5,5,5,5]
  print(l.count(5))
  
#### 14. list index

----------------------------------------------------------------------------------------------
✅ End of Python list_data_type
----------------------------------------------------------------------------------------------
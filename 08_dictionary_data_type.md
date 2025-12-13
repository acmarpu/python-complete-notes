--------------------------------------------------------------------------------------------------
### 🔑 Dictionary
--------------------------------------------------------------------------------------------------
#### 1. what is dictionary : 
* A **dictionary** is a **collection of key–value pairs**.  
* Each item is represented as `{key: value}`.  
* **Keys** are *immutable* and *must be unique*.  
* **Values** can be *mutable* and *can have duplicates*.  
* Keys can be of any immutable data type.

#### 2. creating dictonary

```
   d = {'id':'mac', 'name':'tech', 'insta':'travel'}
   print(d)                                     # Output  {'id':'mac', 'name': 'tech', 'insta': 'travel'}
```
#### 3. accessing value from dictionary

```
   d = d = {'id':'mac', 'name':'tech', 'insta':'travel'}
   print(d['name'])                             # Output tech
   print(d.get('name'))                         # Output tech

   print(d['age'])                              # Output KeyError
   print(d.get('age'))                          # Output None
    
```      

####  4. change or add values

```
   d = {'id':'mac', 'name':'tech', 'insta':'travel'}
   print(d)                                    # Output {'id':'mac', 'name':'tech', 'insta':'travel'}
   d['insta'] = 'explorer'
   print(d)                                    # Output {'id':'mac', 'name':'tech', 'insta':'explorer'}
   d['age'] = 16
   print(d)                                    # Output {'id': 'mac', 'name': 'tech', 'insta': 'explorer', 'age': 16}

```
#### 5. delete or remove values

```
   d = {'id':'mac', 'name':'tech', 'insta':'travel'}
   del d['name']
   print(d)                                   # Output {'id': 'mac', 'insta': 'travel'}

```

#### 6. copy (Shallow Copy)

```
   d = {'id':'mac', 'name':'tech', 'insta':'travel'}
   print(d)                                   # Output {'id': 'mac', 'name': 'tech', 'insta': 'travel'}
   d1 = d
   print(d1)                                  # Output {'id': 'mac', 'name': 'tech', 'insta': 'travel'}
   d['name'] = 'journey'
   print(d)                                   # Output {'id': 'mac', 'name': 'journey', 'insta': 'travel'}
   print(d1)                                  # Output {'id': 'mac', 'name': 'journey', 'insta': 'travel'}

```

#### 7. items and keys and values


```
   d = {'id':'mac', 'name':'tech', 'insta':'travel'}
   print(d.items())                          # Output dict_items([('id', 'mac'), ('name', 'tech'), ('insta', 'travel')])
   print(d.keys())                           # Output dict_keys(['id', 'name', 'insta'])
   print(d.values())                         # Output dict_values(['mac', 'tech', 'travel'])

```

#### 8. membership test
* Membership test applies only to keys.

```
   d = {'id':'mac', 'name':'tech', 'insta':'travel'}
   print(123 in d)                           # Output False
   print('name' in d)                        # Output: True

``` 
#### 9. len

```
   d = {'id':'mac', 'name':'tech', 'insta':'travel'}
   print(len(d))                                        # Output 3

```

#### 10. pop

```
   d = {'id':'mac', 'name':'tech', 'insta':'travel'}
   value= d.pop('name')
   print(value)                                         # Output tech
   print(d)                                             # Output {'id': 'mac', 'insta': 'travel'}

```
#### 11. popitem

```
   d = {'id':'mac', 'name':'tech', 'insta':'travel'}
   d.popitem()
   print(d)                                           # Output  {'id': 'mac', 'name': 'tech'}

```

----------------------------------------------------------------------------------------------
✅ End of dictionary_data_type.md
----------------------------------------------------------------------------------------------
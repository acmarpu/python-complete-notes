----------------------------------------------------------------------------------------------
### 🧵 3. String ("Immutable")
----------------------------------------------------------------------------------------------
#### 1. What is a String?
* In Python, strings are an essential data type used to represent textual data.
* Definition: A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' / """ """).
 - Example: 'hello', "python", """world"""
* String Methods: Python provides many built-in methods to manipulate strings.
 - Examples: .replace(), .split(), .lower(), .upper(), .strip(), etc.
* String Immutability: Strings are **immutable**, meaning once created, they cannot be modified.
 - Operations like concatenation or .replace() return a new string instead of changing the original one.
* String supports to Indexing 



```  
   my_string = "Hello, Apple!"
   print("String value:", my_string)           #Output: String value: Hello, Apple!
   print("Type of string:", type(my_string))   #Output: Type of string: <class 'str'>


   # With single quotes (' ') → may need escape \'.
   my_string = 'Hello, Apple!\'s'
   print("String value:", my_string)          #Output: String value: Hello, Apple!'s

```

#### 2. String Indexing and Slicing
* Indexing means accessing characters in a string using position numbers.
* String indices start at 0 (for the first character).



|Positive Indexing   | 0 | 1 | 2 | 3 | 4 | 5 |6  |7  |
|--------------------|---|---|---|---|---|---|---|---|
|                    | W | E | L |   | C | O | M | E |
|Negative indexing   |-8 |-7 |-6 |-5 |-4 |-3 |-2 |-1 |



* a) Indexing Examples

```
   my_string = "helloapple!"

   print("First character:", my_string[0])          # Output: h

   print("Second character:", my_string[1])         # Output: e 

   print("Last character:", my_string[-1])          # Output: !

   print("Second last character:", my_string[-3])   # Output: e

```

* b) Slicing

* Slicing means extracting a part of the string.
* string[start:end]   # end index is excluded

```
   print("Substring (0 to 4):", my_string[0:5])     # Output: hello

   print("Substring (6 to end):", my_string[6:])    # Output: apple!

   print("Substring (start to 5):", my_string[:6])  # Output: hello

```

* reverese the string without reverese function
* We can reverse a string easily using slicing with a step value of -1.

```
   my_string = "helloapple!"

   reversed_string = my_string[::-1]

   print("Reversed string:", reversed_string)        # Output: !elppaolleh

```

#### 3. String Concatenation and String Multiplication
* Concatenation →    The process of joining two or more strings using the + operator.
* Multiplication →   Used to repeat a string multiple times using the * operator.

```
   str1 = "red"
   str2 = "apple"

   print("Concatenated string:", str1 + " " + str2)   # Output: red apple

   print(str1 + " " + str2)                           # Output: redapple

   print(str1 * 3)                                    # Output: redredred

   print((str1 + " " + str2 + " ") * 3)               # Output: red red apple red apple red apple

```

#### 4. String Split and Max Split
* The `split()` method in Python divides a string into a list based on a specified **separator**.
* separator → The delimiter to split the string (default: whitespace).
* maxsplit → (optional): The maximum number of splits. Remaining string is returned as the last element.

```
   str1 = " Python is very easy to learn."

   print("Original string:", str1)              # Output: Original string:  Python is very easy to learn.

   
   words = str1.split()

   print("Words in the string:", words)         # Output: ['Python', 'is', 'very', 'easy', 'to', 'learn.']

   maxsplit = str1.split(" ", 3)

   print("Max 3 splits:", maxsplit)             # Output: ['Python', 'is', 'very', 'easy to learn.']


   isappears = str1.split("is")

   print("Split by 'is':", isappears)           # Output: [' Python ', ' very easy to learn.']


```

#### 5. capitalize() Method
* The capitalize() method returns a new string where the first character is converted to uppercase, and the rest of the string is converted to lowercase.

```
   str1 = " Python is Very Easy To Learn."

   print(str1)                   # Output:  Python is Very Easy To Learn.

   str2 = str1.capitalize()

   print(str2)                   # Output:  python is very easy to learn.

```

#### 6. String title() Method
The title() method returns a new string where the first character of every word is capitalized, and all other letters are lowercase.

```
   str1 = " python is very easy to learn."

   str3 = str1.title()

   print(str3)                   # Output:  Python Is Very Easy To Learn.

```

#### 7. String count() Method
The count() method returns the number of occurrences of a specified substring within a given string.

```
   str1 = "Python is very Easy and Anyone can learn"

   print(str1)                                       # Output: Python is very Easy and Anyone can learn

   print(str1.count(""))                             # Output: 7 space 

   print(str1.count('is'))                           # Output: 1

   s2 = str1.count("a")

   print(s2)                                       # Output: 3
              
```

#### 8. String replace() Method
The replace() method returns a new string where all occurrences of a specified substring are replaced with another substring.

```
   str1 = " python is very easy to learn."

   print(str1.replace("easy", "hard"))             # Output:  python is very hard to learn.           

```

#### 9. String upper() and lower() Methods
These methods convert the case of characters in a string.

```
   str1 = "python is very easy and Anyone can learn"

   print(str1.upper())                   # Output:  PYTHON IS VERY EASY AND ANYONE CAN LEARN.

   str2 = str1.upper()

   print(str2)                           # Output:  PYTHON IS VERY EASY AND ANYONE CAN LEARN.

   print(str2.lower())                   # Output:  python is very easy and anyone can learn. 

```

#### 10. string swapcase() Method
The swapcase() method returns a new string where uppercase letters become lowercase and lowercase letters become uppercase

```
   str1 = "Python Is Very Easy To Learn."

   str2 = str1.swapcase()

   print(str2)                   # Output:  pYTHON iS vERY eASY tO lEARN.

```

#### 11. String Reverse
* There is no direct reverse() method for strings since they are immutable.
* We can reverse using slicing [::-1].

```
   str1 = "python"

   print(str1[::-1])                               # Output nohtyp

```

#### 12. String Immutability
* Strings in Python cannot be changed after creation.
* Any operation that seems to modify a string actually creates a new string.

```
   str1 = "python"

   print(id(str1))

   s = s + "language"

   print(s)

   print(id(s))                                # Different ID → new string created

```

#### 13. String Sort
* You can split a string into words and then sort them alphabetically.

```
   s = "python is very easy"

   str1 = s.split()

   print(str1)                                   # Output ['python', 'is', 'very', 'easy']

   str1.sort()

   print(str1)                                   # Output ['easy', 'is', 'python', 'very']

   str1.sort(reverse=True)
   
   print(str1)                                   # Output ['very', 'python', 'is', 'easy']

```

#### 14. join() Function
* The join() method combines elements of an iterable (like a string or list) into a single string.

```

   s = "hyderabad"
   str1 = ':'.join(s)
   print(str1)                                   # Output: h:y:d:e:r:a:b:a:d

   s2 = ''.join(reversed(str1))
   print(s2)                                   # Output: d:a:b:a:r:e:d:y:h

   print("".join(reversed("SAI")))             # Output: IAS

   l = ["sai", "raj", "ram"]
   s = ','.join(l)
   print(s)                                    # Output sai,raj,ram


```
#### 15–17. strip(), lstrip(), and rstrip()
* These methods remove whitespace or specified characters from a string.
* They return a copy of the string with leading and/or trailing characters removed

```
   s = "  mactechtravel "
   print(s.strip())                          # Removes spaces on both sides
   print(s.rstrip())                         # Removes spaces on the right
   print(s.lstrip())                         # Removes spaces on the left

   str1 = s.strip()
   print(str1)


   # Output:
   mactechtravel
     mactechtravel
   mactechtravel  
   mactechtravel

```


#### 18. len()
Returns the length of the string.

```
   s = "python"
   print(len(s))                             # Output 6

```


#### 19. find()
* Returns the index of the first occurrence of a substring.
* Returns -1 if not found.

```
   s = "python"
   print(s.find("b"))                        # Not found
   print(s.find("t"))                        # Found at index 2

```
#### 21–22. max() and min()
Return the highest and lowest alphabetical characters.

```
   s = "python"
   print(max(s))
   print(min(s))

```

#### 23. index()
* Returns the index of the first occurrence of a substring.
* Raises an error if the substring is not found.

```
   s = "python"
   print(s.index("b"))                       # ValueError: substring not found

```

#### 24. rindex()
Returns the highest index of the substring.

```
   s = "python is very easy"
   print(s.rindex("y"))

```
#### 25. partition()
* Splits the string at the first occurrence of the separator and returns a tuple.

```
   s = "python is very easy and it is opp and it is interpreted is"
   print(s.split(" "))
   print(s.partition("is"))

   #Output

   ['python', 'is', 'very', 'easy', 'and', 'it', 'is', 'opp', 'and', 'it', 'is', 'interpreted', 'is']
   ('python ', 'is', ' very easy and it is opp and it is interpreted is')


```

#### 26. startswith()
Returns True if the string starts with the given prefix.

```
   s = "python is easy"
   print(s.startswith("python"))                # Output: True
   print(s.startswith("is"))                    # Output:False

```

#### 27. endswith()
Returns True if the string ends with the given suffix.

```
   s = "python is easy"
   print(s.endswith("easy"))                     # Output: True
   print(s.endswith("is"))                       # Output:False

```

### 28. isdigit()
Returns True if all characters in the string are digits.

```
   s = "12345"
   print(s.isdigit())                            # Output True

```
#### 29. isalpha()
Returns True if all characters in the string are alphabets.

```
   s = "Python"
   print(s.isalpha())                            #Output:  True

```

#### 30. isalnum()
Returns True if all characters are alphanumeric (letters and digits only).


```
   s = "Python123"
   print(s.isalnum())

```

* Reverse Each Word in a String

```
   s = "python is very easy"
   str1 = s.split(" ")
   print(str1)

   for i in str1:
      print(i[::-1], end=" ")

   #Output

   ['python', 'is', 'very', 'easy']
   nohtyp si yrev ysae


```



**To get a list of all available functions for string operations, you can use the dir() function:**
* This will return a list of all the methods and attributes associated with the string class.

```
   print(dir(str))
   __add_                                     #also called descriptors
```


```    
  * description    
  help(str)

```

----------------------------------------------------------------------------------------------
✅ End of Python string_data_type
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
### 🧵 String Data Type
----------------------------------------------------------------------------------------------
#### 1. What is a String?
* A string is a sequence of characters enclosed in quotes.
* It can be defined using:

* Single quotes → 'hello'
* Double quotes → "hello"
* Triple quotes → '''hello''' or """hello""" (for multiline strings)

👉 Strings are immutable, meaning their content cannot be changed after creation.

#### 2. String Indexing and Slicing
* Indexing means accessing characters in a string using position numbers.
* String indices start at 0 (for the first character).

```
     0 1 2 3 4 5 6 7 8   → Positive index
     h y d e r a b a d
    -9-8-7-6-5-4-3-2-1   → Negative index
```

🔹 Indexing Examples

```
   s = "hyderabad"

    print(s)            # Output: hyderabad
    print(s[3])         # Output: e
    print(s[-3])        # Output: a

```
🔹 Slicing
* Slicing means extracting a part of the string.
* string[start:end]   # end index is excluded

```
   s = "hyderabad"

   print(s[1:6])     # Output: yderab  (characters from index 1 to 5)
   print(s[-7:-1])   # Output: deraba  (negative slicing)

``` 
* reverese the string without reverese function
* We can reverse a string easily using slicing with a step value of -1.
```
   s = "hyderabad"
   print(::-1)

```

#### 3. String Concatenation and String Multiplication
* Concatenation → The process of joining two or more strings using the + operator.
* Multiplication → Used to repeat a string multiple times using the * operator.

```
   s1 = "read"
   s2 = "apple"

   print(s1 + s2)                    # Output: readapple
   print(s1 + " " + s2)              # Output: read apple  (adds space between)
   print(s1 * 3)                     # Output: readreadread
   print((s1 + " " + s2 + " ") * 3)  # Output: read apple read apple read apple

```

#### 4. String Split and Max Split
* The `split()` method in Python divides a string into a list based on a specified **separator**.
* separator → The delimiter to split the string (default: whitespace).
* maxsplit → (optional): The maximum number of splits. Remaining string is returned as the last element.

```
   s1 = "python is very easy and anyone can learn"
   print(s1)

   # Split the string using space as a separator
   s2 = s1.split(" ")
   print(s2)

   # Split the string using space, but only into 4 parts (max 3 splits)
   s3 = s1.split(" ", 3)
   print(s3)

   # Split the string wherever the word 'is' appears
   s4 = s1.split("is")
   print(s4)

   # Output

   python is very easy and anyone can learn
   ['python', 'is', 'very', 'easy', 'and', 'anyone', 'can', 'learn']
   ['python', 'is', 'very', 'easy and anyone can learn']
   ['python ', ' very easy and anyone can learn']


```

#### 5. capitalize() Method
* The capitalize() method returns a new string where the first character is converted to uppercase, and the rest of the string is converted to lowercase.

```
   s1 = "python is very easy and anyone can learn"
   print(s1)                  # Output python is very easy and anyone can learn
   s2 = s1.capitalize()
   print(s2)                  # Output Python is very easy and anyone can learn

   s3 = "Python Is very Easy and Anyone can learn"
   print(s3)                  # Output Python Is very Easy and Anyone can learn
   s4 = s3.capitalize()
   print(s4)                  # Output Python is very easy and anyone can learn

```

#### 6. String title() Method
The title() method returns a new string where the first character of every word is capitalized, and all other letters are lowercase.

```
   s1 = "Python Is very Easy and Anyone can learn"
   print(s1)                    # Output Python Is very Easy and Anyone can learn

   s2 = s1.title()
   print(s2)                    # Output Python Is Very Easy And Anyone Can learn

```

#### 7. String count() Method
The count() method returns the number of occurrences of a specified substring within a given string.

```
   s1 = "Python is very Easy and Anyone can learn"
   print(s1)                    # Output: Python is very Easy and Anyone can learn
   print(s1.count(""))          # Output: 7 space 

   print(s1.count('is'))        # Output: 1

   s2 = s1.count("a")
   print(s2)                    # Output: 3
              
```

#### 8. String replace() Method
The replace() method returns a new string where all occurrences of a specified substring are replaced with another substring.

```
   s1 = "python is very easy and anyone can learn"
   print(s1.replace("easy", "hard"))    # Output python is very hard and anyone can learn

   s2 = s1.replace("easy", "hard")      
   print(s2)                            # Output python is very hard and anyone can learn                   

```

#### 9. String upper() and lower() Methods
These methods convert the case of characters in a string.

```
   s1 = "python is very easy and Anyone can learn"

   print(s1.upper())    # Convert all letters to uppercase

   s2 = s1.upper()
   print(s2.lower())    # Convert all letters back to lowercase

```

#### 10. string swapcase() Method
The swapcase() method returns a new string where uppercase letters become lowercase and lowercase letters become uppercase

```
   s = "HyDerAbaD"
   print(s)
   print(s.swapcase())

```

#### 11. String Reverse
* There is no direct reverse() method for strings since they are immutable.
* We can reverse using slicing [::-1].

```
   s = "python"
   print(s[::-1])     #Output nohtyp

```

#### 12. String Immutability
* Strings in Python cannot be changed after creation.
* Any operation that seems to modify a string actually creates a new string.

```
   s = "python"
   print(id(s))
   s = s + " language"
   print(s)
   print(id(s))   # Different ID → new string created

```

#### 13. String Sort
* You can split a string into words and then sort them alphabetically.

```
   s = "python is very easy"
   s1 = s.split()
   print(s1)                # Output ['python', 'is', 'very', 'easy']

   s1.sort()
   print(s1)                # Output ['easy', 'is', 'python', 'very']

   s1.sort(reverse=True)
   print(s1)                # Output ['very', 'python', 'is', 'easy']

```

#### 14. join() Function
* The join() method combines elements of an iterable (like a string or list) into a single string.

```

   s = "hyderabad"
   s1 = ':'.join(s)
   print(s1)                           # Output h:y:d:e:r:a:b:a:d

   s2 = ''.join(reversed(s1))
   print(s2)                           # Output d:a:b:a:r:e:d:y:h

   print("".join(reversed("SAI")))     # Output IAS

   l = ["sai", "raj", "ram"]
   s = ','.join(l)
   print(s)                            # Output sai,raj,ram


```
#### 15–17. strip(), lstrip(), and rstrip()
* These methods remove whitespace or specified characters from a string.
* They return a copy of the string with leading and/or trailing characters removed

```
   s = "  macitexplorer  "
   print(s.strip())    # Removes spaces on both sides
   print(s.rstrip())   # Removes spaces on the right
   print(s.lstrip())   # Removes spaces on the left

   s1 = s.strip()
   print(s1)


    # Output
   macitexplorer
     macitexplorer
   macitexplorer  
   macitexplorer

```


#### 18. len()
Returns the length of the string.

```
   s = "python"
   print(len(s))    # Output 6

```


#### 19. find()
* Returns the index of the first occurrence of a substring.
* Returns -1 if not found.

```
   s = "python"
   print(s.find("b"))   # Not found
   print(s.find("t"))   # Found at index 2

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
   print(s.index("b"))  # ValueError: substring not found

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
   print(s.startswith("python"))
   print(s.startswith("is"))


   #Output 

   True
   False


```

#### 27. endswith()
Returns True if the string ends with the given suffix.

```
   s = "python is easy"
   print(s.endswith("easy"))
   print(s.endswith("is"))

   #Output
   True
   False


```

### 28. isdigit()
Returns True if all characters in the string are digits.

```
   s = "12345"
   print(s.isdigit())

   # Output

   True


```
#### 29. isalpha()
Returns True if all characters in the string are alphabets.

```
   s = "Python"
   print(s.isalpha())

   #Output

   True


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
   s1 = s.split(" ")
   print(s1)

   for i in s1:
      print(i[::-1], end=" ")

   #Output

   ['python', 'is', 'very', 'easy']
   nohtyp si yrev ysae


```

----------------------------------------------------------------------------------------------
✅ End of Python string_data_type
----------------------------------------------------------------------------------------------
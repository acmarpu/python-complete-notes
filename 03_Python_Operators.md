----------------------------------------------------------------------------------------------
### 👉 Operators
----------------------------------------------------------------------------------------------
* In Python, **operators** are symbols (or keywords) used to perform operations on variables and values.  
* They allow us to manipulate data, perform calculations, compare results, and control logic flow. 

```
    import operator

    print("All operators in the operators module:", dir(operator))
    print("All operators in the operators module:", operator.__all__)

    👉 So, __all__ is basically the official list of functions/objects that the operator module wants you to use

```

----------------------------------------------------------------------------------------------
#### ➕ 1. Arithmetic Operators
----------------------------------------------------------------------------------------------
* Arithmetic operators are used to perform basic mathematical operations.

```
    a = 5
    b = 3

```

| Operator | Description           | Example                    | Output|
|----------|-----------------------|----------------------------|-------|
| `+`      | Addition              | print(a + b)               | `8`    |
| `-`      | Subtraction           | print(a - b)               | `2`    |
| `*`      | Multiplication        | print(a * b)               | `15`    |
| `/`      | Division (float)      | print(a / b)               | `1.666666..` |
| `//`     | Floor Division        | print(a //b)               | `1`     |
| `%`      | Modulus (remainder)   | print(a % b)              | `2`   |
| `**`     | Exponentiation (power)| print(2 ** 3)              | `125`   |




#### Second way

```
    import operator
    a = 5
    b = 3

```

| Operator | Description           | Example                                | Output       |
|----------|-----------------------|----------------------------------------|--------------|
| `+`      | Addition              | print("Addition:", operator.add(a, b)) |  # Output: 8 |
| `-`      | Subtraction           | print("Subtraction:", operator.sub(a, b)) | # Output: 2 |
| `*`      | Multiplication        | print("Multiplication:", operator.mul(a, b)) |  # Output: 15 |
| `/`      | Division (float)      | print("Division:", operator.truediv(a, b)) |  # Output: 1.6666666666666667 |
| `//`     | Floor Division        | print("Floor Division:", operator.floordiv(a, b))  | # Output: 1 |            
           
       
         
         


----------------------------------------------------------------------------------------------
#### ⚖️ 2. Relational (Comparison) Operators
----------------------------------------------------------------------------------------------
* Relational operators are used to **compare two values**.  
* The result of these operations is always a **Boolean value** **(`True` or `False`)**.
* Commonly applied in data validation and filtering

```
    a = 5
    b = 3

```

| Operator | Description                      | Example        | Output  |
|----------|----------------------------------|----------------|---------|
| `==`     | Equal to                         | `print(a == b)`| `False`  |
| `!=`     | Not equal to                     | `print(a != b)` | `True`  |
| `<`      | Less than                        | `print(a < b)` | `False` |
| `<=`     | Less than or equal to            | `print(a <= b)`| `False` |
| `>`      | Greater than                     | `print(a > b)` | `True`  |
| `>=`     | Greater than or equal to         | `print(a > b)` | `True`  |



#### Second way

```
   import operator
   a = 5
   b = 3

```

| Operator | Description                      | Example                  | Output  |
|----------|----------------------------------|--------------------------|---------|
| `==`     | Equal to                         | print("equal:", operator.eq(a,b))| #Output: equal: False  |
| `!=`     | Not equal to                     | print("Not equal:", operator.ne(a,b)) | #Output: Not equal: True |
| `>`      | Greater than                     | print("Greater than:", operator.gt(a, b))   | #Output: Greater than: True  |
| `>=`     | Greater than or equal to         | print("Greater than or Equal to:", operator.ge(a,b)) | #Output: Greater than or Equal to: True  |
| `<`      | Less than                        | print("Less than:", operator.lt(a, b))  | #Output: Less than: False |
| `<=`     | Less than or equal to            | print("Less than or Equal to:", operator.le(a,b))|  #Output: Less than or Equal to: False |
              
                  
    
       




----------------------------------------------------------------------------------------------
#### 📝 3. Assignment Operator
----------------------------------------------------------------------------------------------
* Assignment operators are used to **assign values** to variables.  
* Some operators also perform an operation and then assign the result to the variable.
* When combined with arithmetic operators, they perform two actions at once (calculation + assignment)

| Operator | Description               | Example        | Equivalent To               | Result  |
|----------|---------------------------|----------------|-----------------------------|---------|
| `=`      | Assign                    | `a = 5`        | –                           | `a = 5` |
| `+=`     | Add and assign            | `a += 2`       | print(a) → 7 (a = a + 2)    | `a = 7` |
| `-=`     | Subtract and assign       | `a -= 2`       | print(a) → 5 (a = a - 2)    | `a = 5` |
| `*=`     | Multiply and assign       | `a *= 3`       | print(a) → 15 (a = a * 3)   | `a = 15`|
| `/=`     | Divide and assign         | `a /= 5`       | print(a) → 3.0 (a = a / 5)  | `a = 3.0`|
| `//=`    | Floor divide and assign   | `a //= 2`      | print(a) → 1 (a = a // 2)   | `a = 1` |
| `**=`    | Exponent and assign       | `a **= 2`      | print(a) → 2 (a = a % 3)    | 'a = 2' |

#### Second way
```
  
    import operator
    m = 5
    n = 2
    
    print("Initial m:", m)
    m = operator.iadd(m, n)      
    print("After m += n:", m)    # same as m += n → 7

    m = operator.isub(m, n)      # same as m -= n → 5
    print("After m -= n:", m)

    m = operator.imul(m, n)      # same as m *= n → 10
    print("After m *= n:", m)

    m = operator.truediv(m, n)   # same as m /= n → 5.0
    print("After m /= n:", m)

    m = operator.floordiv(m, n)  # same as m //= n → 2
    print("After m //= n:", m)

```

----------------------------------------------------------------------------------------------
#### 🔗 4 . Logical Operators
----------------------------------------------------------------------------------------------
* Logical operators are used to perform **logical operations** (mainly in conditional statements).
• They deal with Boolean inputs ( or ) and return a Boolean result.
• Useful for decision-making, validations, and combining multiple conditions.


| Operator | Description                              | Example            | Result  |
|----------|------------------------------------------|--------------------|---------|
| `and`    | Returns True if **both** conditions are True, print(True and True) | print(5 > 3 and 10 > 5)  | `True` |
|          | Returns False if any one conditions is False, print(True and False)| print(5 < 3 and 10 > 5)  |  False |               
| `or`     | Returns True if **at least one** condition is True,print(True or False)| print(5 < 3 and 10 > 5)  | `True` |
|          | Returns false if both of them false, print(False or False)         | print(5 < 3 and 10 < 5)  |  False |   
| `not`    | Reverses the boolean value                                         | `not(5 > 3)`             | False  |
|          | print(not True)                                                    |                          | False  |
|          | print(not False)                                                   |                          | True   | 



```
        print(20 < 3 and 1 < 4)           # Output: False
   
        # 20 < 3 is False, 1 < 4 is True **False and True gives False**
```
                                    

* The or operator returns True if at least one condition is true. If both are false, it returns False.*
```   
        print(20 < 3 or 1 < 4)            # Output: True
    
        # 20 < 3 is False, 1 < 4 is True  So, False or True gives True

```    

* The not operator reverses the boolean value of the condition: if the condition is True, it returns False, and if the condition is False, it returns True.

```
        print(not(20 < 3))                # Output: True
        #20 < 3 is False, so not False is True

```      

* Additional Examples:
```
       #Using and
       x = 5
       y = 10
       print(x > 3 and y < 15)            # Output: True
       #True and True = True

```      

```
       x = 5
       y = 10
       print(x < 3 or y > 5)             # Output: True
       # False or True = True

```

```
       x = 10
       print(not(x < 5))                  # Output: True
       # not False = True

```

----------------------------------------------------------------------------------------------
#### 📦 5 . Membership
----------------------------------------------------------------------------------------------

* Membership operators are used to **test whether a value is present in a sequence** (like list, tuple, string, or dictionary).

| Operator   | Description                                        | Example             | Result  |
|------------|----------------------------------------------------|---------------------|---------|
| `in`       | Returns True if the value exists in the sequence   | `10 in [10, 20, 30]`| `True`  |
| `not in`   | Returns True if the value does not exist           | `100 not in [10,20]`| `True`  |


* with List data types examples

```      
    l = [10, 20, 30]
    print(100 not in l)         
    # Output : True 
    # Explanation: 100 is in the list, so "in" returns True

```

```

    print(10 not in l)          
    # Output : False 
    # Explanation: 10 is in the list, so "in" returns False.

```

* with string data types examples

```
    print("x" in "hyd")      # "x" is not in the string "hyd", so it returns False
    #Output: False

```

----------------------------------------------------------------------------------------------
#### 🆔 6. Identity
----------------------------------------------------------------------------------------------

* Identity operators are used to **check if two variables refer to the same object in memory**.

| Operator   | Description                                                                 | Example     | Result  |
|------------|-----------------------------------------------------------------------------|-------------|---------|
| `is`       | Returns True if both variables refer to the same object (same memory)       | `x is y`    | True/False |
| `is not`   | Returns True if both variables do not refer to the same object              | `x is not y`| True/False |

```
    i = 10
    j = 20

    # Checking if i and j refer to the same object
    print(i is j)                       # Output: False → because i and j are pointing to different objects


    # Checking if i and j do not refer to the same object
    print(i is not j)                   # Output: True → because i and j are different objects

    # Using id() to get the memory address of the variables
    # id(): built-in function that returns the memory address of an object
    
    print(id(i))             # Unique memory address for i
    print(id(j))             # Unique memory address for j

```

```
    # Assigning same value to two variables
    x = [1, 2, 3]
    y = x                    # y points to the same object as x

    # Checking if both x and y are the same object in memory
    print(x is y)  
    # Output: True → because both refer to the same object in memory

    # Checking the memory address of both variables
    print(id(x))             # Memory address of x
    print(id(y))             # Memory address of y

```

```
    a = [1, 2, 3]
    b = [1, 2, 3]            # A new list, even though it has the same values as 'a'

    # Checking if a and b refer to the same object
    print(a is b)  
    # Output: False → they are different objects in memory even though values are the same

    # Checking if a and b do not refer to the same object
    print(a is not b)  
    # Output: True → because a and b are different objects

    # Memory addresses will be different for different objects
    print(id(a))              # Memory address of a
    print(id(b))              # Memory address of b

```         

----------------------------------------------------------------------------------------------
#### 🧮 7. Bitwise
----------------------------------------------------------------------------------------------
* Bitwise operators in Python perform operations on individual bits of integers

| Operator | Symbol | Description |
|----------|---------|-------------|
| AND      | `&`     | 1 if both bits are 1 |
| OR       | `\|`    | 1 if at least one bit is 1 |
| XOR      | `^`     | 1 if bits are different |
| NOT      | `~`     | Inverts all bits (`-(n+1)`) |
| Left Shift | `<<`  | Shifts bits left (multiplies by 2) |
| Right Shift | `>>` | Shifts bits right (divides by 2) |


**1. Bitwise AND (`&`)**

```
    a = 5                    # 0101 in binary
    b = 3                    # 0011 in binary
    result = a & b           # 0001 in binary → 1 in decimal
    print(result)            # Output: 1

```

**2. Bitwise OR (|)**
* Compares each bit of two integers, returning 1 if at least one of the bits is 1.

```
    a = 5  # 0101
    b = 3  # 0011
    result = a | b           # 0111 → 7
    print(result)            # Output: 7

```

**3. Bitwise XOR (^)**
* Compares each bit of two integers, returning 1 if the bits are different, otherwise 0.

```
    a = 5                   # 0101
    b = 3                   # 0011
    result = a ^ b          # 0110 → 6
    print(result)           # Output: 6

```

**4. Bitwise NOT (~)**
* Inverts all the bits of the integer, which is equivalent to -(n + 1) (two's complement form).

```
    a = 5  # 0101
    result = ~a            # 1010 (two’s complement) → -6
    print(result)          # Output: -6

```

**5. Bitwise Left Shift (<<)**
* Shifts the bits of the number to the left by a specified number of positions. Each shift to the left multiplies the number by 2.

```
    a = 5  # 0101
    result = a << 1       # 1010 → 10
    print(result)         # Output: 10

```

**6. Bitwise Right Shift (>>)**
* Shifts the bits of the number to the right by a specified number of positions. Each shift to the right divides the number by 2 (and truncates the result).  

```
    a = 5  # 0101
    result = a >> 1       # 0010 → 2
    print(result)         # Output: 2

```

----------------------------------------------------------------------------------------------
✅ End of Python Operators
----------------------------------------------------------------------------------------------
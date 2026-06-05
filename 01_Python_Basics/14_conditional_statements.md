     
----------------------------------------------------------------------------------------------
### 1.❓Conditional Statements
----------------------------------------------------------------------------------------------

#### 🔀 if & if-else

* Based on the condition. it decides whether the block of code will allows for execution or not.
* The `if` keyword is used to test specific conditions.  
  - If the condition evaluates to **True**, the control enters the `if` block.  
  - If the condition evaluates to **False**, the control skips the `if` block and continues with the rest of the code.  

* The `if-else` block is used when you want to execute one block of code if the condition is **True**, and a different block of code if the condition is **False**.  

* whereever performing checks and validations 
* All conditional statemnt boolen output
* Whenever working with conditionals statement we will use Logical statement and Comparison


*  **if:**
  * if it is very hot, i will skip exercise.

* **if else**
  * if i have to buy groceries, i will go left. else i will go stright
  * if there is an exam tomorrow. i will first study and then sleep, otherwise i will sleep

* **elif**
  * if i'm committed, i will achive finish my goal.
  * if i'm 50% commited, i will give try and leave my Goal.
   else, i will no start at all 

* **nested if**
  * if it is holiday
  * and if it is Sunday, you feel that one holiday has missed.
   
* Ternary operations and Precedence 



* General form of the if-else statement

```

   if condation:
      statement1
   else:
      statement2

   statement3

``` 
* **Execution of if-else statement**
  * first the expression is evaluated.
  * if it evaluates to a true value, then statement1 executed and then control moves to statement3.
  * if expression evaluates to false, then statement2 is executed and then control moves to statement3 
  * statement1/statement2 can be blocks of statements!

```
   i = 10

   if i == 10:
   
       print("f{i} this is the currect")

```


```

   i = 10
   if i == 100:
       print("f{i} this is the currect")        # This won't be printed because i is not 100

   else:
       print("f{i} this is not the currect")    # This will be printed because i is 10, not 100

``` 

##### if with list and tuple and string

```
    #string

    course = "Python for devops"
    if "devops" in course:
        print("This course is about devops.")

    else:
        print("This course is not about devops.")

```

```
    # list
    course_list = ["Python", "Devops", "Cloud", "AI", "ML"]
    if "AI" in course_list:
        print("This course is about AI.")

    else:
        print("This course is not about AI.")

```

```
    # tuple
    course_tuple = ("Python", "Devops", "Cloud", "AI", "ML")
    if "Cloud" in course_tuple:
        print("This course is about Cloud.")

    else:
        print("This course is not about Cloud.") 

```

```
    # Single line if statement

    age = 18

    if age >=18: print("You are eligible to vote.")

    # Single line if-else statement

    age = 17
    print("You are eligible to vote.") if age >= 18 else print("You are not eligible to vote.")

    # if the condation is true execute the first statement otherwise execute the second statement

```

```

   i = int(input("Enter a number: "))   # Get user input as an integer
   if i % 2 == 0:                       # Check if the number is divisible by 2
       print(i, "is even")
   else:
       print(i, "is odd")

```

```
    # WAP that takes the number running containers as input and prints whether it is odd or even

    # input
    number_containers = int(input("Enter the number of running containers:"))

    # Driving Factor
    # Check if the number of container is odd or even using module operator

    # condition: even

    if number_containers % 2 == 0:
        container_status = "even"

    # condation: odd

    else: 
        container_status = "odd"

    #Output
    # print container status message: even or odd

    print(f"the number of running containers ({number_containers}) is {container_status}")
    
```

``` 

    i = int(input("Enter a number: "))
    j = int(input("Enter another number: "))

    if i > j:
        print(f"{i} is greater than {j}.")

    else:
        print(f"{j} is greater than {i}.")

    # expected output: 20 is greater than 10.

```

```
# conditional statement with dictionary

    user_roles = {
        "alice": "admin",
        "bob": "editor",
        "charlie": "viewer"
    }


    username = "bob"
    if username in user_roles:
        role = user_roles[username]
        if role == "admin":
            print(f"{username} has admin privileges.")
    
        elif role == "editor":
            print(f"{username} has editor privileges.")
    
        elif role == "viewer":
            print(f"{username} has viewer privileges.")
    
        else:
            print(f"{username} has an unknown role.")

```

```
    # Boolean logic with and, or and not

    age = 25
    membership = "premium"

    if age >= 18 and membership == "premium":
        print("You have access to premium content.")

    else:
        print("You do not have access to premium content.") 

```

**🐞 Debug Mode in PyCharm**
* Debug mode is used to trace how the control flow moves through your program step by step.
* You can set a breakpoint (🔴) in your code — this is a marker that tells the debugger to pause execution at that specific line.
* When the program pauses, you can inspect variables, check conditions, and understand logic flow.
* To start debugging:
* Set a breakpoint (🔴) on the line you want to stop.
* Select Debug option in your IDE (e.g., VS Code → Run > Start Debugging).
* Keyboard Shortcut:
* Fn + F8: Step out of the current function and return to the caller (i.e., go back one level in the call stack).



#### 🪜 Nested if

* Nested `if` is used to test **multiple conditions**.  
* If the outer `if` condition is `True`, then the inner `if` condition(s) will be tested.  
* If any condition fails, Python skips that inner block.  
* In simple terms: **`if` inside another `if`** is called a **nested if statement**.


```
   username = "admin"
    password = "securepasssword"

    if username == "admin":
        if password == "securepasssword":
            print("Login successful.")
    
    else:
        print("Incorrect password.")

```

```
   # idetity operator

    username = "admin"
    password = "securepasssword"

    if username is "admin":                 # this is identity operator
        if password is "securepasssword":   # this is identity operator
            print("Login successful.")
    
        else:
            print("Incorrect password.")

    else:                                   # this condition check the username is not "admin"            
        print("Invalid username.")

```
```
   i = int(input("enter first number:"))  # 10
   j = int(input("enter second number:")) # 20
   k = int(input("enter third number:"))  # 30

   if i > j and i > k:
       print(i,"is big")
   else:
       if j > k:
          print(j,"is big")
        else:
           print(k,"is big")               # Output 30 is big

```

```
   name   = input("enter the name:")             # ashoka       
   age    = int(input("enter the age number:"))  # Convert input to integer 19
   gender = input("enter the gender (m/f):")     # m      

   if age >= 18:
       if gender == "m":
            print("hello Mr.", name, "welcome")
        else:
             print("hello Mrs.", name, "welcome")
   else:
        print("you are not eligbile")             # Output hello Mr. ashoka welcome

```

```
      
   var = int(input("Enter the expression value:"))
   if var < 150:
       print("expression value is less than 150")

       if var < 200:
           print("expression value is less than 200")

           if var < 300:
               print("expression value is less than 300")

           else:
               print("could not fine the Expression value")

```

#### 🔂 elif

* If one of the conditions is true, the remaining conditions will not be tested.  
* The `elif` statement allows you to check multiple conditions. As soon as one condition is true, its block of code executes, and the rest are skipped.


* Using nested if statements (first example) makes the code longer and harder to read.
```
    i = int(input("enter the number"))
    if i == 1:
        print("one")
    else:
        if i == 2:
            print("two")
        else:
            if i == 3:
                print("three)
            else:
                if i == 4:
                    print("four")
                else:
                    print("inval if number")

```

* The elif ladder checks conditions one by one — once a condition is True, the rest are skipped.
```
    i = int(input("Enter a number: "))   # Define i before using it

    if i == 1:
        print("one")
    elif i == 2:
        print("two")
    elif i == 3:
        print("three)
    elif i == 4:
        print("four")
    else:
        print("invalid number")

```

```
   marks = int(input("Enter the Marks:"))
   if marks >= 95:
         print("Grade A")
   elif marks >= 90:
         print("Grade B")
   elif marks >= 85:
         print("Grade C")
   elif marks >= 80:
         print("Grade D")
   else:
      print("not achived")
``` 

```

   var = 100
   or
   var = int(input("Enter the Expression value:")) #we can enter the runtime value
   if var < 150:
       print("Expression value is less than 150")
   elif var < 200:
       print("Expression value is less than 200")
   elif var < 300:
       print("Expression value is less than 300")
   else:
       print("invalid expression value")

```
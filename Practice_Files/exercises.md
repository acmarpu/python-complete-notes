
1. Program: Find the Sum of First n Numbers using for loop and while loop?

```
   n = int(input("Enter number: "))   # n is the input (the limit)
   s = 0                              # s is used to store the result (sum)
   for i in range(1, n + 1):          # loop runs from 1 to n
       s += i                         # add each number to s
   print("The sum of first", n, "numbers is:", s)

```

```
   n = int(input("Enter number: "))   # n is the input (the limit)
   s = 0                              # stores the sum
   i = 1                              # counter variable starts from 1
   while i <= n:                      # loop until i reaches n
       s += i                         # add i to s
       i += 1                         # increment i
   print("The sum of first", n, "numbers is:", s)

```

2. Print Multiplication Table of a Given Number

```
   n = int(input("Enter the number: "))  # take user input
   for i in range(1, 11):                # loop from 1 to 10
   print(n, "X", i, "=", n * i)

```

3. s = "hyderabad" # print eeven index and odd index positoon characters
s = "hyderabad"
print("Even index position characters:,s[0::2]")
print("odd index position characters:",[1::2])




#### 15. creating list from user input values

   creating list from user input value
   l = []
   v1 = int(input("Enter a integer value:"))
   v2 = float(input("Enter a float value:"))
   v3 = input("enter a string value:")
   l.append(v1)
   l.append(v2)
   l.append(v3)
   print(l)

#### 16. creating list using range function
   l = []
   n = int(input("Enter the length of list:"))
   for i in range(n):
        x = int(input("enter the element:"))
        l.append(x)
   print(l)


   l = []
   n = int(input("Enter the length of list:"))
   for i in range(n):
        x = input("enter the element:")
        l.append(x)
    print(l)

#### 17. Creating list using range function
   print(list(range(2,10,2)))


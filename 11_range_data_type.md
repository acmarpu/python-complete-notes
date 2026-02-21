----------------------------------------------------------------------------------------------
### ✨ 8.range (immutable)
----------------------------------------------------------------------------------------------
* The `range()` function in Python is used to generate a sequence of numbers.  
* It's typically used in **for loops** to iterate over a specific range of values.
   
📌 **Key Points:**
  - **Start, Stop, Step:**
  - **Start:** The number where the range begins (**inclusive**).
  - **Stop:** The number where the range ends (**exclusive**).
  - **Step:** The interval between each number in the range.
  - If `step` is not specified, it defaults to `1`.
  - If `start` is not specified, it defaults to `0`.

**Immutability:**
- `range()` objects are **immutable**, meaning you cannot modify the values once it’s created.

**Use Cases:**
- The range() function is often used in loops (like for loops) to repeat actions a certain number of times.


```
   r = range(10)
   print(r)                # Output: range(0, 10)
      
   print(list(r))          # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   
   print(type(r))          # Output: <class 'range'>

```

- range(10) generates a sequence starting from 0 up to (but not including) 10.
- You can convert it to a list or tuple to see the actual values.
- `range()` itself does **not store all values in memory**. It generates numbers on demand (lazy evaluation), which is why printing it directly shows `range(0, 10)` instead of the numbers


```    
   r = range(2, 10, 2)  # start=2, stop=10, step=2

   print(tuple(r))      # Output: (2, 4, 6, 8)

   print(type(r))       # Output: <class 'range'>

```

- `range(2, 10, 2)` starts from `2`, goes up to (but not including) `10`, and increments by `2` each time.  
- We can convert the range to a tuple to see the sequence of numbers: `(2, 4, 6, 8)`.

```     
   for i in range(5):
   print(i)

      # Output:
      # 0
      # 1
      # 2
      # 3
      # 4

```
--------------------------------------------------------------------------------------------------
### bytes & bytearray
--------------------------------------------------------------------------------------------------
* **bytes**:  
  Used to represent a sequence of byte numbers (0–255).  
  It is **immutable**, meaning values cannot be changed.

* **bytearray**:  
  Similar to `bytes`, but **mutable** — values can be modified.  
  Only allowed values are also between **0–255**.

#### create bytes

```
    b = [10,20,30,40,50]
    print(b)               # Output [10, 20, 30, 40, 50]
    print(type(b))         # Output <class 'list'>

    b1 = bytes(b)
    print(b1)              # Output b'\n\x14\x1e(2'
    print(type(b1))        # Output <class 'bytes'>

    print(b[1])            # Output 20
    b[1] = 99              # Output ❌ TpyeError: tuple object does not support item assignment             

    for i in b:
        print(i)

```

```
    b1 = bytesarray(b)
    print(b1)              # Output b'\n\x14\x1e(2'
    print(type(b1))        # Output <class 'bytes'>

    print(b[1])            # Output 20
    b[1] = 99              # Output 10,99.20,30,40,50

```

--------------------------------------------------------------------------------------------------
### frozenset
--------------------------------------------------------------------------------------------------
* frozenset is an immutable version of a set — elements cannot be added, removed, or changed once created.

```
   s = {10,20,30,40,50}
    print(s)                # Output {50, 20, 40, 10, 30}
    print(type(s))          # Output <class 'set'>
    fs = frozenset(s)
    print(fs)               # Output frozenset({50, 20, 40, 10, 30})
    print(type(fs))         # <class 'frozenset'>

    fs.add(99)
    print(fs)               # Output AttributeError: 'frozenset' object has no attribute 'add'

```


----------------------------------------------------------------------------------------------
✅ End of bytes & bytearray and frozenset
----------------------------------------------------------------------------------------------
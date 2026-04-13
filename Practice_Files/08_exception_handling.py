#-----------------------------------------------------------------------
# exception_handling
#-----------------------------------------------------------------------

# Simple exception handling comparison with compiler and run time error

l = [1,2,3,4]
print("hi")
print ("Provide the index of element to be printed")
i = int(input())
try:
    print(l[i])
except Exception as e:
    print("Error: ", e)
# if enter input greater than 3, it will throw an error and program will stop executing and bye will not be printed
print("bye")



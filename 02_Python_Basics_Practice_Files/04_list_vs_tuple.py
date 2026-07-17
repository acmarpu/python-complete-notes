
# List vs tuple in python 


# Mutability of list and tuple


course_list = ["Python", "Java", "C++", "javaScript"]
print("list before modification:", course_list)
print("before change address of list:", id(course_list))

course_list[0] = "Golang"

print("list after change modification:", course_list)
print("list after modification:", id(course_list))



course_tuple = ("Python", "Java", "C++", "javaScript")
print("tuple before modification:", course_tuple)
print("before change address of tuple:", id(course_tuple))

course_tuple[0] = "Golang"

print("list after change modification:", course_tuple)
print("list after modification:", id(course_tuple))

# Output  course_tuple[0] = "Golang" TypeError: 'tuple' object does not support item assignment


#---------------------------------------------------------------
# Syntax of list Comprehension in Python
#---------------------------------------------------------------

# Comprehension will be supported by list, set and dictionary in python
# Comprehension will not be supported by str, int, bool, tuple in python

# conditional statement  and for loop in one line of code is called comprehension in python


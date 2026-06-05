----------------------------------------------------------------------------------------------
### Modules
----------------------------------------------------------------------------------------------

* A module is just a Python file (.py)
* Contains code (functions, classes, or variables) which you can import into another file.
* it's like a single tool you can reuse



----------------------------------------------------------------------------------------------
### Packages
----------------------------------------------------------------------------------------------

* A package is a collection of modules organized in folder.
* The folder must contain a special file named __init__.py (can be empty or contain initialization code).
* it's like a toolbox that holds multiple tools (modules).

* **__init__.py**
* the __init__.py files are required to make Python treat directories containing the file as packages.
* __init__.py can just be an empty file. 
* it can also execute initialization code for the package.
* This prevents directories with a common name.
* such as string, unintentionally hiding valid modules that occur later on the module search path ().


import package_util.math_utils as math_utils       # first way of calling package

from package_util import string_utils # second way of calling package

from package_util import *            # third way of calling package

from package_util import math_utils, string_utils     # fourth way of calling package


# Calling the functions from the math_utils module
print("Upper case operation:", string_utils.uc("pythonfordevops"))
print("Lower case operation:", string_utils.lc("pythonfordevops"))
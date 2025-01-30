#module is python script/file with a predefined task
#user defined and built-in modules are available

## built in modules
# import time
# print(time.time())#time in seconds since the Epoch (January 1, 1970, 00:00:00 UTC).
# print(time.localtime())
# print(time.timezone)

# from datetime import datetime
# current_time = datetime.now()
# print("Current Time:", current_time)

# import random
# print(random.randint(1,100))
# random_numbers = [random.randint(1, 100) for _ in range(10)]
# print(random_numbers)

# import math as m #another method to import
# print(m.pi)
# print(m.e)#exponential

# #to import pi only
# from math import pi
# print(pi)
# print(e)

#to import all
# from math import *
# print(pi)
# print(e)

import test_modules
test_modules.some_fn()
print(test_modules.a)

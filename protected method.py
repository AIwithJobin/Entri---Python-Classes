class ProtectedExample:
    def __init__(self):
        self._protected_var = "I am a protected variable"

    def _protected_method(self):
        return "I am a protected method"

# Accessing protected members
obj = ProtectedExample()
print(obj._protected_var)           # Technically accessible, but not recommended
print(obj._protected_method())      # Technically accessible, but not recommended

# Private Methods and Variables
class PrivateExample:
    def __init__(self):
        self.__private_var = "I am a private variable"

    def __private_method(self):
        return "I am a private method"

    def access_private_members(self):
        # Accessing private members within the class
        print(self.__private_var)
        print(self.__private_method())

# Accessing private members
obj = PrivateExample()
obj.access_private_members()

# Trying to access private members directly
# print(obj.__private_var)        # AttributeError
# print(obj.__private_method())   # AttributeError

# Accessing private members using name mangling (not recommended)
print(obj._PrivateExample__private_var)
print(obj._PrivateExample__private_method())
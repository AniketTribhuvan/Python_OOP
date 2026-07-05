# Access Modifiers control how attributes and methods are intended to be accessed.
# 1. Public
# 2. Protected
# 3. Private
#
# Unlike languages such as C++ or Java, Python does not strictly enforce access control.
# Public, protected and private are mainly naming conventions that programmers are expected to respect.

# As I have studied C++. In C++:
# 1. Public members can be accessed from anywhere.
# 2. Protected members can be accessed inside the class and its subclasses.
# 3. Private members can be accessed only inside the class.

# Python follows the same idea, but access is indicated by the naming convention of the member.


# 1. Public : Can be accessed from anywhere.
# Syntax of member: name (normal)

class employee:
    def __init__(self, name):
        self.name = name


emp1 = employee("Aniket")
print(emp1.name)        # Can be accessed outside the class.

# Output :
# Aniket


# 2. Protected : Intended to be accessed only inside the class and its subclasses.
# Syntax of member: _name (single underscore)

class employee:
    def __init__(self, name):
        self._name = name      # "_" means this member is intended to be protected.


emp2 = employee("Aniket")
print(emp2._name)      # Then how can we still access it outside the class?

# Output :
# Aniket

# Python does not prevent access to protected members.
# The single underscore is only a convention that tells other programmers:
# "This member is for internal use. Don't access it directly outside the class."
# That's why in practice we usually use getters, setters or properties instead of
# accessing protected members directly.

# Remember:
# Python is often called a language of trust.
# It does not strictly enforce these rules, but expects programmers to follow them.


# 3. Private : Intended to be accessed only inside the class.
# Syntax of member: __name (double underscore)

class employee:
    def __init__(self, name):
        self.__name = name      # "__" makes this member private using name mangling.


emp3 = employee("Aniket")

# print(emp3.__name)
# This raises an AttributeError because Python changes the attribute name internally.

# Private members are not truly private.
# Python internally stores them as:
# _ClassName__variableName
# This technique is called Name Mangling.

print(emp3._employee__name)

# Output :
# Aniket

# Although this works, it should only be used when absolutely necessary.
# Accessing private members this way is considered bad practice.


# Name Mangling:
# Name mangling is a technique used by Python to reduce accidental access
# or accidental overriding of private members.
# Python internally changes:
# __name
# into:
# _employee__name
#
# So, private and protected members in Python are mainly conventions,
# with name mangling providing some additional protection for private members.
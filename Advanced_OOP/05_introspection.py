# Introspection is a feature used to get information about objects or class.
# Following are the functions & attribute used for introspection.

# 1. dir() : A function which returns a list of all attributes & methods available on an object or class.
# dir() tells What can this object do.

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = student("Aniket", 16)
print(dir(s1))      # Returns all attributes & methods of s1 object.
# Output :
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__',
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__',
# '__subclasshook__', '__weakref__', 'age', 'name']

# The methods like '__class__', '__delattr__', '__dict__', '__dir__', '__doc__'..... are built-in methods.

# 2. __dict__ : A attribute which contains an object's or class's writable attributes with their values.
# It doesn't built-in methods like dir().

print(s1.__dict__)
# Output :
# {'name': 'Aniket', 'age': 16}

# 3. help() : A function which displays the documentation of an object, class, function, or module.

class Student:

    """Represents a student."""

    def introduce(self):
        """Print student's name."""

print(help(Student))
# Output :
# Help on class Student in module __main__:                                                                                                     

# class Student(builtins.object)
#  |  Represents a student.
#  |
#  |  Methods defined here:
#  |
#  |  introduce(self)
#  |      Print student's name.
#  |
#  |  ----------------------------------------------------------------------                                                                    
#  |  Data descriptors defined here:                                                                                                            
#  |                                                                                                                                            
#  |  __dict__                                                                                                                                  
#  |      dictionary for instance variables                                                                                                     
#  |                                                                                                                                            
#  |  __weakref__                                                                                                                               
#  |      list of weak references to the object 
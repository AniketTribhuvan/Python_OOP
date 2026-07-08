# We have a class1 which includes attributes & methods. Now we create another class2 and inherit class1.
# Now class2 can access all public methods and attributes of class1.
# It can also access protected members, although they are intended for internal use.
# This is called Inheritance.
#
# Inheritance allows a class to reuse attributes and methods of another class
# without writing everything again.
#
# class1 is called the Parent (Base) class.
# class2 is called the Child (Derived) class.
#
# There are various types of inheritance which we will study later.
# Here we are learning Single Inheritance.
#
# Syntax:
# class ClassName(ParentClass):


# Without inheritance

class dog:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


dog1 = dog("Shiro")
cat1 = cat("Jerry")

dog1.eat()
cat1.eat()

# Output:
# Shiro is eating.
# Jerry is eating.


# With inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class dog(Animal):          # Child class

    # Child class can also have its own methods.
    def bark(self):
        print(f"{self.name} is barking.")


class cat(Animal):
    pass


# Since dog doesn't have its own __init__(),
# Python automatically calls the parent's constructor.
dog2 = dog("Tommy")
dog2.eat()          # Parent class method
dog2.bark()         # Child class method

cat2 = cat("Micky")
cat2.eat()

# Output :
# Tommy is eating.
# Tommy is barking.
# Micky is eating.
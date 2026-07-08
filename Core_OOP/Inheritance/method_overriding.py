# Method Overriding is when a child class creates a method with the same name
# as a method in the parent class to provide its own implementation.


# Without overriding

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes sound")


class dog(Animal):
    pass


class cat(Animal):
    pass


class lion(Animal):
    pass


dog1 = dog("Tom")
cat1 = cat("Jerry")
lion1 = lion("Shera")

dog1.sound()
cat1.sound()
lion1.sound()

# Output :
# Animal makes sound
# Animal makes sound
# Animal makes sound


# We want different sounds for different animals.
# So we override the parent's sound() method in the child classes.
#
# Note:
# Overriding means the parent and child methods must have the same name.

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes sound")


class dog(Animal):
    def sound(self):            # Overrides parent's sound()
        print(f"{self.name} barks")


class cat(Animal):
    def sound(self):            # Overrides parent's sound()
        print(f"{self.name} meows")


class lion(Animal):
    pass                        # Uses parent's sound()


dog1 = dog("Tom")
cat1 = cat("Jerry")
lion1 = lion("Shera")

dog1.sound()        # Child class method
cat1.sound()        # Child class method
lion1.sound()       # Parent class method

# Output :
# Tom barks
# Jerry meows
# Animal makes sound


# How Python searches for methods:
# First, Python looks in the child class.
# If the method isn't found there, it searches the parent class.


# What if we want to execute both the parent class method
# and the overridden child class method?
#
# We use super().
#
# super() returns a temporary object that allows us to access
# methods of the parent class.
#
# Syntax:
# super().method_name(arguments)

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes sound")


class dog(Animal):
    def sound(self):
        super().sound()         # Calls the parent's sound() method.
        print(f"{self.name} barks")


dog2 = dog("Leo")
dog2.sound()

# Output :
# Animal makes sound
# Leo barks


# Constructor Overriding
#
# If both the parent and child class have their own constructors,
# we use super().__init__() to call the parent's constructor.

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show_name(self):
        print(f"Name of employee {self.id} is {self.name}")


class salary(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name)      # Calls the parent's constructor.
        self.salary = salary

    def show_salary(self):
        print(f"Salary of employee {self.id} is {self.salary}")


emp1 = salary(101, "Aniket", 30000)
emp1.show_name()
emp1.show_salary()

# Output :
# Name of employee 101 is Aniket
# Salary of employee 101 is 30000
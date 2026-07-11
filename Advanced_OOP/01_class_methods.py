# In OOP, there are 3 types of methods.
# 1. Instance method : First parameter is self. These methods belong to an instance.
# 2. Class method : First parameter is cls. These methods belong to the class.
# 3. Static method : No self or cls parameter. These methods belong to neither the class nor an instance.

# Class methods are used when the operation is related to the class itself
# instead of any particular object.
#
# Since class variables belong to the class, class methods are commonly used
# to access or modify them.
#
# Syntax:
# Use the @classmethod decorator and cls as the first parameter.

# Example:
# We have a Student class with a class variable "school".
# To print the school name, we don't need to create an object.

class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)


Student.show_school()

# Output :
# ABC School


# Why use @classmethod?
#
# Without @classmethod, Python treats the method as an instance method.
# When called using an object, Python automatically passes the object as the first argument.
#
# The @classmethod decorator tells Python to pass the class instead.
#
# Why use cls?
#
# Just like self refers to the current object,
# cls refers to the current class.
#
# You can technically use any name instead of cls,
# but cls is the standard convention.


# Example:
# We want to change the class variable "school".

class Student:
    school = "ABC School"

    # Without @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


s1 = Student()

print(s1.school)

# Output :
# ABC School


# Student.change_school("XYZ School")
#
# This raises a TypeError because Python expects an instance
# as the first argument for an instance method.


# Calling through an object works because Python passes s1 as the first argument.
# This creates an instance variable named school instead of changing the class variable.

s1.change_school("XYZ School")

print(s1.school)

# Output :
# XYZ School

print(Student.school)

# Output :
# ABC School


# Now with @classmethod

class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


s1 = Student()

print(s1.school)

# Output :
# ABC School

Student.change_school("XYZ School")

print(s1.school)
print(Student.school)

# Output :
# XYZ School
# XYZ School
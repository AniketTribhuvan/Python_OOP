# Static methods are methods that belong to neither the class nor an instance.
# They are simply utility functions placed inside a class because they are
# logically related to that class.
#
# Syntax:
# Use the @staticmethod decorator.

# Example:
# We want a utility function is_age_valid() for the Student class.
# It only needs an age value.
# It doesn't require an object or the class itself.

class Student:
    @staticmethod
    def is_age_valid(age):
        return age >= 0


print(Student.is_age_valid(11))

s1 = Student()
print(s1.is_age_valid(11))

# Output :
# True
# True


# Why use @staticmethod?
#
# Without @staticmethod, Python treats the method as an instance method.
# When called through an object, Python automatically passes the object
# as the first argument.

class Student:
    def is_age_valid(age):
        return age >= 0


print(Student.is_age_valid(11))

# Calling through the class works because Python treats it like a normal function.

s1 = Student()

# print(s1.is_age_valid(18))
#
# This raises a TypeError because Python automatically passes s1
# as the first argument, so the method receives two arguments:
# (s1, 18), but it expects only one.


# Can we define these methods outside the class?
#
# Yes. It will work perfectly.
# However, if a function is closely related to a class but doesn't need
# self or cls, placing it inside the class as a static method improves
# organization and readability.
# When a class inherits more than one classes then it's called Multiple Inheritance.

class A:
    def show_A(self):
        print("A")
class B:
    def show_B(self):
        print("B")

class C(A, B):      # Class C inherits class A & class B.
    pass

obj = C()
obj.show_A()
obj.show_B()
# Output :
# A
# B

# MRO (Method Resolution Order)
# The problem occurs when both parent class have same method name. Python confuses while executing method.

class A:
    def show(self):
        print("A")
class B:
    def show(self):
        print("B")

# Now both parent class contains show(). The question is python will execute which show() ?
# Python executes method according to MRO.
# MRO is a order by which python searches for class, attributes & methods.
# The parent class which is listed first is searched first by python.

class C(A, B):      # Class A then Class B
    pass

obj = C()
obj.show()
# Output :
# A             # Python search first in Class A, It founds show(). It calls it.
# In this code Python search in following order :
# class C
# class A
# class B
# objects (Every class inherits built-in object class)
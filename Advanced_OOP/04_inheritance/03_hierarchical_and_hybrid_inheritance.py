# Hierarchical Inheritance
# When multiple child classes inherits from same parent class then it's Hierarchical Inheritance.

class A:        # Parent Class
    pass
class B(A):     # Child Class of A
    pass
class C(A):     # Child Class of A
    pass

# Visual representation of Hierarchy :
#         Parent
#        /   |   \
#       /    |    \
#  Child1 Child2 Child3

# Hybrid Inheritance
# Combination of two or more inheritance types is called Hybrid Inheritance.

class BaseClass:
    pass
class Derived1(BaseClass):
    pass
class Derived2(BaseClass):
    pass
class Derived3(Derived1, Derived2):
    pass
# Above Example contains Single Inheritance, Multiple inheritance, Hierarchical inheritance
# Therefore it's called Hybrid Inheritance.
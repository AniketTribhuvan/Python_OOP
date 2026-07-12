# When a class inherits another class & then a third class inherits the child class is called as Multilevel Inheritance.
# That means : Class1 inherits class2 & then class3 inherits class1 i.e indirectly class3 also inherits class2.
# class3 can access class1 as well as class2 methods.
# Here class3 is a child class, class1 is a parent class & class2 is a grandparent class.

class Animal():         # Grandparent class
    def eat(self):
        print("eating")
class mammal(Animal):         # Parent class which inherits grandparent class
    def walk(self):
        print("Walks")
class dog(mammal):      # Child class inherits parent class & also inherits grandparent class indirectly
    pass
dog1 = dog()
dog1.walk()
dog1.eat()      # dog1 indirectly access eat() from Animal class because mammal inherits Animal class
# Output :
# Walks
# eating
# MRO works here also.
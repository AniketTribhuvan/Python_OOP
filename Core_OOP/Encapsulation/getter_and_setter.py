# getters & setters are used to get & set data securely.
# They allow us to validate or control how data is accessed or modified.
# Without them, invalid values can be assigned directly.

# without getters & setters

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = student("Aniket", 16)

# Here s1 has name = "Aniket" & age = 16.
s1.age = -10    # Age becomes negative without any validation.
print(s1.age)   # -10


# with getters & setters

class student:
    def __init__(self, name, age):
        # A single underscore (_) is a convention that says:
        # "This attribute is intended for internal use."
        self._name = name
        self._age = age

    # Getter methods
    def name(self):
        return self._name

    def age(self):
        return self._age

    # Setter method
    def set_age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age can't be negative")


s2 = student("John", 17)

# Access attributes using getter methods.
print(s2.name())        # John
print(s2.age())         # 17

# Update age using setter method.
s2.set_age(18)
print(s2.age())         # 18


# We aren't going to study decorators deeply yet.
# Just understand the basic idea.

# Without decorators we have to call methods like:
# s2.name(), s2.age()

# With decorators we can access them like normal attributes:
# s3.name, s3.age

# @property creates a read-only property.
# @property_name.setter defines what happens when a value is assigned.
# @property_name.deleter defines what happens when the property is deleted.

# Note:
# The getter, setter and deleter methods must have the same name.
# they must have the same name so Python knows they are all defining the read, write, and delete behavior of that single property

class student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age can't be negative")

    @age.deleter
    def age(self):
        del self._age


s3 = student("David", 20)

print(s3.name)      # David
print(s3.age)       # 20

s3.age = -10        # Validation prevents invalid age.
s3.age = 21
print(s3.age)       # 21

del s3.age          # Deletes the _age attribute.

# print(s3.age)     # This will raise an AttributeError because _age no longer exists.

# Output :
# David
# 20
# Age can't be negative
# 21
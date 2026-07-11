class Student:
    # Alternative Constructors & @classmethod
    #
    # An alternative constructor is another way of creating objects.
    # The normal constructor (__init__) expects separate arguments:
    # Student(name, age)
    #
    # But sometimes data comes in a different format, such as:
    # - Dictionary
    # - CSV file
    # - JSON
    # - Database records
    #
    # Instead of changing __init__() every time, we create an
    # alternative constructor using @classmethod.
    #
    # The classmethod receives the class (cls), extracts the required
    # data, and finally creates the object by calling:
    # cls(...)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name is {self.name} & age is {self.age}")

    # Alternative constructor for dictionary data.
    @classmethod
    def from_dict(cls, data):
        name = data["name"]
        age = data["age"]

        # cls(name, age) is equivalent to Student(name, age).
        # Using cls makes this constructor work correctly even if
        # the Student class is inherited later.
        return cls(name, age)


# Data is available in dictionary format.
data = {
    "name": "Aniket",
    "age": 17
}

# Create the object using the alternative constructor.
s1 = Student.from_dict(data)

s1.show()

# Output:
# Name is Aniket & age is 17
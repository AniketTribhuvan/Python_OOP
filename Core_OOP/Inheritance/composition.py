# Composition (Has-A Relationship)
#
# Composition is an OOP principle where one class contains an object of another
# class to use its functionality.
#
# Instead of writing everything inside one class, we divide responsibilities
# into multiple classes and connect them using objects.

# Composition is useful when one class contains another object that has
# its own attributes and methods.
#
# Example:
# A Car has an Engine.
# An Engine has its own properties like horsepower and fuel type,
# so it should be represented by its own class.

class Engine:       # Component class
    def __init__(self, horsepower, fuel):
        self.horsepower = horsepower
        self.fuel = fuel

    def start(self):
        print(f"{self.fuel} engine with {self.horsepower} HP started.")


class Car:          # Composite class
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine      # Engine object is stored inside Car.

    def drive(self):
        print(f"{self.brand} is driving.")


petrol_engine = Engine(200, "Petrol")     # Engine object

# We pass the Engine object to the Car object.
car1 = Car("Toyota", petrol_engine)

car1.drive()            # Method of Car class.
car1.engine.start()     # Accessing Engine's method through the Car object.

# Output :
# Toyota is driving.
# Petrol engine with 200 HP started.

# A developer-friendly way of accessing attributes and methods of the component class.
# Instead of accessing the component object directly, we delegate the work through
# the composite class.
#
# This approach is commonly used when the component object is protected or private.
# It also keeps the internal implementation hidden from the user.

class Engine:       # Component class
    def __init__(self, horsepower, fuel):
        self.horsepower = horsepower
        self.fuel = fuel

    def start(self):
        print(f"{self.fuel} engine with {self.horsepower} HP started.")


class Car:          # Composite class
    def __init__(self, brand, engine):
        self.brand = brand
        self._engine = engine      # Protected Engine object

    # Delegate the Engine's start() method.
    def start(self):
        self._engine.start()

    # Delegate the Engine's horsepower attribute.
    @property
    def horsepower(self):
        return self._engine.horsepower

    @horsepower.setter
    def horsepower(self, value):
        self._engine.horsepower = value

    def drive(self):
        print(f"{self.brand} is driving.")


diesel_engine = Engine(200, "Diesel")     # Engine object

# Pass the Engine object to the Car object.
car2 = Car("Ford", diesel_engine)

car2.start()              # Instead of car2._engine.start()

car2.horsepower = 150     # Instead of car2._engine.horsepower = 150
print(car2.horsepower)    # Instead of print(car2._engine.horsepower)

# Output :
# Diesel engine with 200 HP started.
# 150
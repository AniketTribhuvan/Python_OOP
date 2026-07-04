# instance variables : Variables which are different for each object.
# class variables : Variables which are common for all objects.

class student:
    school = "ABC school"       # Class variable

    def __init__(self, name):
        self.name = name        # Instance variable

    def show_details(self):
        print(f"Name : {self.name}\nSchool : {self.school}")

s3 = student("Aniket")
s4 = student("John")
s3.show_details()
s4.show_details()
# Output :
# Name : Aniket
# School : ABC school
# Name : John
# School : ABC school

# Instance variables vs Class variables.
# Now let's see what happens if we try to change the school of one student.

s5 = student("John")
s6 = student("David")
s5.school = "XYZ school"    # Python creates a new instance variable for s5. It does not change the class variable.

# Does s5 have 2 school variables?
# Not exactly.
# The class still has one class variable: school = "ABC school".
# s5 now has its own instance variable named school = "XYZ school".
# Python first searches for an instance variable. If it doesn't find one,
# then it searches for a class variable.

s5.show_details()
s6.show_details()
# Output :
# Name : John
# School : XYZ school
# Name : David
# School : ABC school

# 3. Bank Account Simulator
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Current balance : {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance : {self.balance}")
        else:
            print("Insufficient balance.")

acc1 = BankAccount("Aniket", 2000)
acc1.deposit(2000)
acc1.withdraw(10000)

# Output :
# Deposit successful. Current balance : 4000
# Insufficient balance.
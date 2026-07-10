# Library Membership System

class Member:
    # Class variable shared by all members.
    member_count = 0

    def __init__(self, name, membership_id):
        self.name = name
        self._membership_id = membership_id      # Protected attribute
        self.__borrowed_books = 0                # Private attribute

        # Increase total member count whenever a new member is created.
        Member.member_count += 1

    # Getter for borrowed books.
    @property
    def borrowed_books(self):
        return self.__borrowed_books

    # Setter with validation.
    @borrowed_books.setter
    def borrowed_books(self, quantity):
        if 0 <= quantity <= 5:
            self.__borrowed_books = quantity
        else:
            print("A member can borrow only 0 to 5 books.")

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Membership ID : {self._membership_id}")
        print(f"Borrowed books : {self.borrowed_books}")


class PremiumMember(Member):
    def __init__(self, name, membership_id, premium_points):
        super().__init__(name, membership_id)
        self.premium_points = premium_points

    # Override display_info() to include premium details.
    def display_info(self):
        print("Premium Member")
        super().display_info()
        print(f"Premium points : {self.premium_points}")


member1 = Member("Aniket", 121)
member1.borrowed_books = 3

member2 = Member("John", 122)
member2.borrowed_books = 6      # Invalid

member3 = PremiumMember("David", 130, 40)
member3.borrowed_books = 5

member1.display_info()
print()

member2.display_info()
print()

member3.display_info()
print()

print(f"Member count : {Member.member_count}")
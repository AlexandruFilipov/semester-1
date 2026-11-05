# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    def __init__(self,name,birth):
        self.name = name 
        self.birth = birth
            
        if type(self.name) != str:
            raise TypeError("Name must be a string")
        if self.name == "":
            raise ValueError("Name cannot be empty")
        if type(self.birth) != date:
            raise TypeError("Birth must be a date object")
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def is_birthday(self):
        """Checks if its the persons birthday"""
        today = date.today()
        if today.month == self.birth.month and today.day == self.birth.day:
            return True
        else:
            return False


    def initials(self):
        """Find the initials of a person"""
        initials = []
        for letter in self.name:
            if letter.isalpha and letter.isupper():
                initials.append(letter)
        return initials

    

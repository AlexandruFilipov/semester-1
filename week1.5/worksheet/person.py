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
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials():
        initials = []
        for letter in name:
            if letter == letter.upper():
                initials.append(letter)
        print(initials)

    

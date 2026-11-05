# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.height = height
        self.width = width

        if type(self.height) != int:
            raise TypeError("height must be an integer")
        if self.height <= 0:
            raise ValueError("Height must be more than 0")

        if type(self.width) != int:
            raise TypeError("width must be an integer")
        if self.width <= 0:
            raise ValueError("width must be more than 0")

        
                
    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        """Checks if the object is a square by checking if width and height are equal."""
        if self.width == self.height:
            return True 
        else:
            return False

    def area(self):
        return self.height*self.width
        

    def perimeter(self):
        return (self.height*2)+(self.width*2)
         
    # (See README.md for details of what they should do)

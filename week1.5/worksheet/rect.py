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
        self.width = width
        self.height = height
        try:
            if type(self.width) != int or type(self.height) != int:
                raise TypeError("Width and height must be integers")
            if self.width <= 0 or self.height <= 0:
                raise ValueError("Width and height must be positive")
                
    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        if self.width == self.height:
            return True 
        else:
            return False

    def area(self):
        area = self.height*self.width
        return area

    def perimeter(self):
        perimeter = (self.height*2)+(self.width*2)
        return perimeter
    # (See README.md for details of what they should do)

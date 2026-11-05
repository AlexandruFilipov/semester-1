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
        try:
            self.width = width
        except TypeError:
            print("Wrong Value")
        if self.width <= 0:
            raise ValueError("Cant be 0 or less")
        except TypeError:
            print("Wrong Value")
        finally if self.width <= 0:
            raise ValueError("Cant be 0 or less")

        try:
            self.height = height
        except TypeError:
            print("Wrong Value")
        if self.height <= 0:
            raise ValueError("Cant be 0 or less")
        except TypeError:
            print("Wrong Value")
        finally if self.height <= 0:
            raise ValueError("Cant be 0 or less")
        
                
    # Implement methods is_square(), area() & perimeter() here
    def is_square(self,width,height):
        if self.width == self.height:
            return True 
        else:
            return False

    def area(self,width,height):
        area = self.height*self.width
        return area

    def perimeter(self,width,height):
        perimeter = (self.height*2)+(self.width*2)
        return perimeter
    # (See README.md for details of what they should do)

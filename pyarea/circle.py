import math

def area(radius):
    """
    Function to calculate the area of a circle given the radius.
    
    Parameters:
    radius (float or int): Radius of the circle.
    
    Returns:
    float: Area of the circle.
    """
    return math.pi * radius ** 2

#  Example usage:
# radius = float(input("Enter the radius of the circle: "))
# area = area(radius)
# print("Area of the circle:", area)

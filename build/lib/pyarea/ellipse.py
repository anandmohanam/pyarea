import math

def area(major_axis, minor_axis):
    """
    Function to calculate the area of an ellipse given the lengths of its major and minor axes.
    
    Parameters:
    major_axis (float or int): Length of the major axis of the ellipse.
    minor_axis (float or int): Length of the minor axis of the ellipse.
    
    Returns:
    float: Area of the ellipse.
    """
    return math.pi * major_axis * minor_axis

# Example usage:
# major_axis = float(input("Enter the length of the major axis of the ellipse: "))
# minor_axis = float(input("Enter the length of the minor axis of the ellipse: "))
# area = area(major_axis, minor_axis)
# print("Area of the ellipse:", area)

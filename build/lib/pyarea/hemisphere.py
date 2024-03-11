import math

def area(radius):
    """
    Function to calculate the surface area of a hemisphere given its radius.
    
    Parameters:
    radius (float or int): Radius of the hemisphere.
    
    Returns:
    float: Surface area of the hemisphere.
    """
    return 2 * math.pi * radius ** 2

# Example usage:
# radius = float(input("Enter the radius of the hemisphere: "))
# surface_area = area(radius)
# print("Surface area of the hemisphere:", surface_area)
